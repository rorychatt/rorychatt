#!/usr/bin/env python3
"""Regenerate assets/data.js from the GitHub API.

Requires the `gh` CLI, authenticated as the profile owner (private-repo
contribution counts need the token). Run from the repo root:

    python3 scripts/build-data.py
"""
import collections
import json
import subprocess
import datetime
import pathlib

USER = "rorychatt"
START_YEAR = 2023
TODAY = datetime.date.today().isoformat()
ROOT = pathlib.Path(__file__).resolve().parent.parent

QUERY = """query{ user(login:"%s"){ contributionsCollection(from:"%d-01-01T00:00:00Z", to:"%d-12-31T23:59:59Z"){
  contributionCalendar{ weeks{ contributionDays{ date contributionCount } } }
  commitContributionsByRepository(maxRepositories:100){
    repository{ nameWithOwner isPrivate primaryLanguage{name} }
    contributions{ totalCount }
  }
}}}"""


def fetch(year):
    q = QUERY % (USER, year, year)
    r = subprocess.run(["gh", "api", "graphql", "-f", "query=" + q],
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)["data"]["user"]["contributionsCollection"]


def main():
    contrib = {y: fetch(y) for y in range(START_YEAR, datetime.date.today().year + 1)}

    days = {}
    for c in contrib.values():
        for w in c["contributionCalendar"]["weeks"]:
            for d in w["contributionDays"]:
                days[d["date"]] = d["contributionCount"]
    days = {k: v for k, v in sorted(days.items()) if k <= TODAY}

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

    # Curated top projects — edit the narrative here, commit counts come from the API.
    curated = json.loads((ROOT / "scripts" / "projects.json").read_text())
    projects = [dict(p, commits=tot.get(p["full"], 0)) for p in curated]

    timeline = [
        {"full": n, "commits": c, "lang": meta[n]["lang"] or "",
         "from": first[n], "to": last[n], "priv": meta[n]["private"]}
        for n, c in sorted(tot.items(), key=lambda x: (first[x[0]], -x[1]))
        if c >= 8
    ]

    data = {
        "days": days,
        "yearly": {str(y): sum(d["contributionCount"]
                               for w in c["contributionCalendar"]["weeks"]
                               for d in w["contributionDays"])
                   for y, c in contrib.items()},
        "langCommits": dict(langc),
        "projects": projects,
        "timeline": timeline,
        "totals": {"contributions": sum(days.values()), "repos": len(tot), "generated": TODAY},
    }
    out = ROOT / "assets" / "data.js"
    out.write_text("window.GH = " + json.dumps(data, separators=(",", ":")) + "\n")
    print(f"wrote {out} — {len(days)} days, {len(tot)} repos, "
          f"{sum(days.values()):,} contributions")


if __name__ == "__main__":
    main()
