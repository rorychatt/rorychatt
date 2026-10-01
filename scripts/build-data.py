#!/usr/bin/env python3
"""Regenerate assets/data.js from the GitHub API.

Needs the `gh` CLI. Two modes:

    python3 scripts/build-data.py           # full
    python3 scripts/build-data.py --light   # calendar and public facts only

Full mode needs a token that can see your private repositories (locally: `gh`
signed in as the profile owner; in Actions: the STATS_TOKEN secret). It rebuilds
everything, including the per-repository timeline and language split.

Light mode works with any token, including the default Actions token. It
refreshes the contribution calendar (private contributions are included as
anonymous counts because the profile shows them), stars, and the public commit
and PR counts, and keeps the rest of the existing data.js untouched.
"""
import collections
import datetime
import json
import pathlib
import subprocess
import sys

USER = "rorychatt"
START_YEAR = 2023
TODAY = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "assets" / "data.js"

FULL_QUERY = """query{ user(login:"%s"){ contributionsCollection(from:"%d-01-01T00:00:00Z", to:"%d-12-31T23:59:59Z"){
  contributionCalendar{ weeks{ contributionDays{ date contributionCount } } }
  commitContributionsByRepository(maxRepositories:100){
    repository{ nameWithOwner isPrivate primaryLanguage{name} }
    contributions{ totalCount }
  }
}}}"""

LIGHT_QUERY = """query{ user(login:"%s"){ contributionsCollection(from:"%d-01-01T00:00:00Z", to:"%d-12-31T23:59:59Z"){
  contributionCalendar{ weeks{ contributionDays{ date contributionCount } } }
}}}"""

HISTORY = "defaultBranchRef{ target{ ... on Commit{ all: history{ totalCount } mine: history(author:{id:$uid}){ totalCount } } } }"


def gh(args):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    return r


def graphql(query, **variables):
    """Run a query. Partial errors (for example an inaccessible repo) are tolerated."""
    args = ["api", "graphql", "-f", "query=" + query]
    for k, v in variables.items():
        args += ["-f", f"{k}={v}"]
    r = gh(args)
    if not r.stdout.strip():
        raise SystemExit(f"GraphQL call failed: {r.stderr.strip()}")
    body = json.loads(r.stdout)
    if "data" not in body or body["data"] is None:
        raise SystemExit(f"GraphQL call failed: {body}")
    return body["data"]


def fetch(year, query):
    data = graphql(query % (USER, year, year))
    return data["user"]["contributionsCollection"]


def calendar(contrib):
    days = {}
    for c in contrib.values():
        for w in c["contributionCalendar"]["weeks"]:
            for d in w["contributionDays"]:
                days[d["date"]] = d["contributionCount"]
    days = {k: v for k, v in sorted(days.items()) if k <= TODAY}
    yearly = {str(y): sum(d["contributionCount"]
                          for w in c["contributionCalendar"]["weeks"]
                          for d in w["contributionDays"] if d["date"] <= TODAY)
              for y, c in contrib.items()}
    return days, yearly


def repo_stars(full):
    r = gh(["api", f"repos/{full}", "--jq", ".stargazers_count"])
    try:
        return int(r.stdout.strip())
    except ValueError:
        return None


def collect_facts(prior, private_ok):
    """Numbers the CV, README and portfolio quote. Keeps prior values when a call can't see them."""
    facts = dict(prior)
    uid = graphql('query{ user(login:"%s"){ id } }' % USER)["user"]["id"]
    q = """query($uid:ID!){
      fw: repository(owner:"Ivy-Interactive", name:"Ivy-Framework"){ stargazerCount %(h)s }
      te: repository(owner:"Ivy-Interactive", name:"Ivy-Tendril"){ stargazerCount %(h)s }
      fwpr: search(query:"repo:Ivy-Interactive/Ivy-Framework author:%(u)s type:pr", type:ISSUE, first:1){ issueCount }
      tepr: search(query:"repo:Ivy-Interactive/Ivy-Tendril author:%(u)s type:pr", type:ISSUE, first:1){ issueCount }
      %(extra)s
    }""" % {"h": HISTORY, "u": USER, "extra": (
        'orgpr: search(query:"org:Ivy-Interactive author:%s type:pr", type:ISSUE, first:1){ issueCount }\n'
        '      orgrev: search(query:"org:Ivy-Interactive reviewed-by:%s type:pr", type:ISSUE, first:1){ issueCount }'
        % (USER, USER)) if private_ok else ""}
    d = graphql(q, uid=uid)
    for key, alias in (("fw", "fw"), ("te", "te")):
        repo = d[alias]
        hist = repo["defaultBranchRef"]["target"]
        facts[f"{key}_stars"] = repo["stargazerCount"]
        facts[f"{key}_commits_all"] = hist["all"]["totalCount"]
        facts[f"{key}_commits_me"] = hist["mine"]["totalCount"]
    facts["fw_prs"] = d["fwpr"]["issueCount"]
    facts["te_prs"] = d["tepr"]["issueCount"]
    if private_ok:
        facts["org_prs"] = d["orgpr"]["issueCount"]
        facts["org_reviews"] = d["orgrev"]["issueCount"]
    tag = gh(["api", "repos/SpaceCorps/play/releases/latest", "--jq", ".tag_name"]).stdout.strip()
    if tag:
        facts["play_tag"] = tag
    return facts


def fresh_commits(fulls):
    """Your commit count on the default branch of each repo this token can see."""
    uid = graphql('query{ user(login:"%s"){ id } }' % USER)["user"]["id"]
    parts = []
    for i, full in enumerate(fulls):
        owner, name = full.split("/", 1)
        parts.append('r%d: repository(owner:"%s", name:"%s"){ defaultBranchRef{ target{ ... on Commit{ '
                     'mine: history(author:{id:$uid}){ totalCount } } } } }' % (i, owner, name))
    d = graphql("query($uid:ID!){ %s }" % "\n".join(parts), uid=uid)
    out = {}
    for i, full in enumerate(fulls):
        try:
            out[full] = d[f"r{i}"]["defaultBranchRef"]["target"]["mine"]["totalCount"]
        except (TypeError, KeyError):
            pass  # not visible to this token: keep the previous number
    return out


def load_existing():
    raw = DATA.read_bytes().decode("utf-8").strip().rstrip(";")
    return json.loads(raw[raw.index("=") + 1:].strip())


def write(data):
    DATA.write_bytes(("window.GH = " + json.dumps(data, separators=(",", ":")) + "\n").encode("utf-8"))


def curated_with_live_stars(curated):
    out = []
    for p in curated:
        stars = repo_stars(p["full"])
        out.append(dict(p, stars=p["stars"] if stars is None else stars))
    return out


def main_light():
    data = load_existing()
    contrib = {y: fetch(y, LIGHT_QUERY) for y in range(START_YEAR, datetime.date.fromisoformat(TODAY).year + 1)}
    days, yearly = calendar(contrib)
    data["days"], data["yearly"] = days, yearly
    data["facts"] = collect_facts(data.get("facts", {}), private_ok=False)

    curated = json.loads((ROOT / "scripts" / "projects.json").read_text())
    live = {p["full"]: p for p in curated_with_live_stars(curated)}
    old = {p["full"]: p for p in data["projects"]}
    fresh = fresh_commits([p["full"] for p in curated])
    projects = []
    for p in curated:
        cur = dict(live[p["full"]])
        before = old.get(p["full"], {}).get("commits", 0)
        cur["commits"] = max(before, fresh.get(p["full"], 0))  # never shrink on a partial view
        projects.append(cur)
    data["projects"] = projects
    data["totals"] = dict(data["totals"], contributions=sum(days.values()), generated=TODAY)
    write(data)
    print(f"light refresh: {len(days)} days, {sum(days.values()):,} contributions, stars and facts updated")


def main_full():
    contrib = {y: fetch(y, FULL_QUERY) for y in range(START_YEAR, datetime.date.fromisoformat(TODAY).year + 1)}
    days, yearly = calendar(contrib)

    tot = collections.Counter()
    langc = collections.Counter()
    first, last, meta = {}, {}, {}
    for y, c in contrib.items():
        for e in c["commitContributionsByRepository"]:
            r = e["repository"]
            n = r["nameWithOwner"]
            ct = e["contributions"]["totalCount"]
            tot[n] += ct
            lang = (r["primaryLanguage"] or {}).get("name")
            if lang:
                langc[lang] += ct
            meta[n] = {"lang": lang, "private": r["isPrivate"]}
            first[n] = min(first.get(n, "9999"), str(y))
            last[n] = max(last.get(n, "0"), str(y))

    # Curated top projects: edit the narrative in projects.json, numbers come from the API.
    curated = json.loads((ROOT / "scripts" / "projects.json").read_text())
    # Default-branch commit counts, the same measure the CV and README quote. Contribution-based
    # totals are the fallback for repos the token cannot read directly.
    fresh = fresh_commits([p["full"] for p in curated])
    projects = [dict(p, commits=fresh.get(p["full"], tot.get(p["full"], 0)))
                for p in curated_with_live_stars(curated)]

    timeline = [
        {"full": n, "commits": c, "lang": meta[n]["lang"] or "",
         "from": first[n], "to": last[n], "priv": meta[n]["private"]}
        for n, c in sorted(tot.items(), key=lambda x: (first[x[0]], -x[1]))
        if c >= 8
    ]

    try:
        prior = load_existing().get("facts", {})
    except (OSError, ValueError, KeyError):
        prior = {}

    data = {
        "days": days,
        "yearly": yearly,
        "langCommits": dict(langc),
        "projects": projects,
        "timeline": timeline,
        "facts": collect_facts(prior, private_ok=True),
        "totals": {"contributions": sum(days.values()), "repos": len(tot), "generated": TODAY},
    }
    write(data)
    print(f"full refresh: {len(days)} days, {len(tot)} repos, {sum(days.values()):,} contributions")


if __name__ == "__main__":
    main_light() if "--light" in sys.argv[1:] else main_full()
