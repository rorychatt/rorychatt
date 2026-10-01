#!/usr/bin/env python3
"""Bake the JS-rendered sections into index.html as static markup.

app.js still renders everything at runtime (it owns the animations and the
heatmap), but agents and crawlers that do not execute JavaScript need the
content in the initial HTML response. This writes the same markup app.js
would produce into the container elements, between BEGIN/END marker comments
so the next run can replace it cleanly.

    python3 scripts/prerender.py

It also fills the <!--f:key-->value<!--/f--> markers in index.html, README.md
and cv/index.html from the `facts` block of data.js, and draws the 365-day
activity graph in cv/index.html from the same daily calendar.
"""
import datetime
import hashlib
import html
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANG_COLOR = {
    "C#": "#8b5cf6", "TypeScript": "#3b82f6", "Rust": "#f97316",
    "JavaScript": "#eab308", "Python": "#22c55e", "Fortran": "#ec4899",
    "Shell": "#64748b", "HTML": "#ef4444", "Jupyter Notebook": "#f59e0b",
    "Dart": "#06b6d4", "Java": "#f43f5e", "C": "#94a3b8", "TeX": "#a3a3a3",
    "Swift": "#f05138", "Kotlin": "#a97bff",
}
MILESTONES = {
    "2022": ["Joined University of Tartu Institute of Technology as engineer &amp; researcher"],
    "2023": ["Founded SpaceCorps Technology OÜ", "First-author paper at IEEE IVNC 2023",
             "Joined Nixor EE AS"],
    "2024": ["Completed SALT full-stack C# programme", "Joined Scania as Solutions Architect"],
    "2025": ["Became 1st Founding Engineer at Ivy"],
}


def e(s):
    return html.escape(str(s), quote=True)


def lc(lang):
    return LANG_COLOR.get(lang, "#6b7a90")


def load():
    raw = read(ROOT / "assets" / "data.js").strip().rstrip(";")
    return json.loads(raw[raw.index("=") + 1:].strip())


def stats_html(gh):
    rows = [
        (gh["totals"]["contributions"], "Contributions since 2023"),
        (sum(p["commits"] for p in gh["projects"]), "Commits in top projects"),
        (gh["totals"]["repos"], "Repositories touched"),
        (sum(p["stars"] for p in gh["projects"]), "Stars on shipped work"),
        (3, "Years of history shown"),
    ]
    return "\n".join(
        f'      <div class="stat"><b data-to="{n}">{n:,}</b><span>{e(label)}</span></div>'
        for n, label in rows)


def projects_html(gh):
    out = []
    for i, p in enumerate(gh["projects"], 1):
        stars = f'<span class="pill star">★ {p["stars"]}</span>' if p["stars"] else ""
        out.append(
            f'      <article class="proj reveal">\n'
            f'        <div class="proj-top"><span class="rank">{i:02d}</span>\n'
            f'        <h3><a href="{e(p["url"])}" target="_blank" rel="noopener">{e(p["name"])}</a></h3></div>\n'
            f'        <div class="slug">{e(p["full"])}</div>\n'
            f'        <p class="desc">{e(p["desc"])}</p>\n'
            f'        <p class="role">{e(p["role"])}</p>\n'
            f'        <div class="proj-meta"><span class="pill commits">{p["commits"]:,} commits</span>'
            f'{stars}<span class="pill lang" style="--d:{lc(p["lang"])}">{e(p["lang"])}</span>'
            f'<span class="pill">{e(p["period"])}</span></div>\n'
            f'      </article>')
    return "\n".join(out)


def timeline_html(gh):
    groups = {}
    for r in gh["timeline"]:
        groups.setdefault(r["from"], []).append(r)
    for y in MILESTONES:
        groups.setdefault(y, [])
    mx = max(r["commits"] for r in gh["timeline"])

    out = []
    for y in sorted(groups, reverse=True):
        items = sorted(groups[y], key=lambda r: -r["commits"])
        total = sum(r["commits"] for r in items)
        sub = (f"{len(items)} repos started · {total:,} commits" if items
               else "before the git history shown here")
        out.append(f'      <div class="tl-year">{y}<small>{sub}</small></div>')
        for m in MILESTONES.get(y, []):
            out.append(
                '      <div class="tl-row"><div class="tl-name">'
                '<span class="tl-tag" style="border-color:rgba(240,171,252,.4);color:#f0abfc">milestone</span>'
                f'<span style="color:#e8edf5">{m}</span></div><div class="tl-right"></div></div>')
        rows = []
        for r in items:
            org, name = r["full"].split("/", 1)
            span = f'{r["from"]}–{r["to"]}' if r["to"] != r["from"] else r["from"]
            name_html = (f'<span style="color:#e8edf5;font-weight:500">{e(name)}</span>' if r["priv"]
                         else f'<a href="https://github.com/{e(r["full"])}" target="_blank" rel="noopener">{e(name)}</a>')
            tags = ""
            if r["lang"]:
                tags += (f'<span class="tl-tag" style="border-color:{lc(r["lang"])}55;'
                         f'color:{lc(r["lang"])}">{e(r["lang"])}</span>')
            if r["priv"]:
                tags += '<span class="tl-tag">private</span>'
            if span != r["from"]:
                tags += f'<span class="tl-tag">{span}</span>'
            width = max(3, r["commits"] / mx * 100)
            rows.append(
                f'        <div class="tl-row"><div class="tl-name">'
                f'<span class="org">{e(org)}/</span>{name_html}{tags}</div>'
                f'<div class="tl-right"><span class="tl-bar"><i style="width:{width}%"></i></span>'
                f'<span class="tl-n">{r["commits"]:,}</span></div></div>')
        out.append('      <div class="tl-items">\n' + "\n".join(rows) + "\n      </div>")
    return "\n".join(out)


def bust(src):
    """Stamp each local asset URL with a hash of its contents.

    GitHub Pages serves assets with max-age=600, so a returning visitor can
    hold a stale app.js against fresh HTML — which renders the pre-rendered
    sections twice. A content hash in the URL makes that impossible.
    """
    def sub(m):
        prefix, path = m.group(1), m.group(2)
        digest = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()[:10]
        return f'{prefix}{path}?v={digest}"'

    return re.sub(r'((?:href|src)=")(assets/[\w./-]+?)(?:\?v=[0-9a-f]+)?"', sub, src)


def splice(src, marker, inner):
    """Replace whatever sits inside the marked container with `inner`."""
    begin, end = f"<!-- BEGIN {marker} -->", f"<!-- END {marker} -->"
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    block = f"{begin}\n{inner}\n      {end}"
    if pat.search(src):
        return pat.sub(lambda _: block, src, count=1)
    raise SystemExit(f"marker {marker!r} not found in index.html")


# ---- live numbers and the CV activity graph ---------------------------------

FACT = re.compile(r"<!--f:(\w+)(?:\|(\w+))?-->.*?<!--/f-->", re.S)


def read(path):
    return path.read_bytes().decode("utf-8")


def write(path, text):
    path.write_bytes(text.encode("utf-8"))


def fact_values(gh):
    f = dict(gh["facts"])
    f["core_commits"] = f["fw_commits_me"] + f["te_commits_me"]
    f["fw_share"] = round(100 * f["fw_commits_me"] / f["fw_commits_all"])
    f["te_share"] = round(100 * f["te_commits_me"] / f["te_commits_all"])
    d = datetime.date.fromisoformat(gh["totals"]["generated"])
    f["generated_long"] = f"{d.day} {d.strftime('%B %Y')}"
    f["contrib_floor"] = gh["totals"]["contributions"] // 1000 * 1000
    return f


def phrase_rules(v):
    """Numbers that live in meta attributes and plain text, where comment markers can't go."""
    k = f"{v['contrib_floor']:,}"
    return [
        (r"[\d,]+\+ GitHub contributions", f"{k}+ GitHub contributions"),
        (r"Over [\d,]+ GitHub contributions", f"Over {k} GitHub contributions"),
        (r"— [\d,]+\+ contributions", f"— {k}+ contributions"),
        (r"(Ivy-Framework\)\s*\(C#, )\d+(★\))", rf"\g<1>{v['fw_stars']}\g<2>"),
        (r"(Ivy-Tendril\)\s*\(C#, )\d+(★\))", rf"\g<1>{v['te_stars']}\g<2>"),
        (r"\d+(★ — C# full-stack framework)", rf"{v['fw_stars']}\g<1>"),
    ]


def apply_phrases(src, v):
    for pat, repl in phrase_rules(v):
        src = re.sub(pat, repl, src)
    return src


def fmt_fact(value, how):
    if how == "floor100":
        return f"{value // 100 * 100:,}+"
    if how == "pct":
        return f"{value}%"
    if how == "raw":
        return str(value)
    return f"{value:,}" if isinstance(value, int) else str(value)


def fill_facts(src, values):
    def sub(m):
        key, how = m.group(1), m.group(2)
        if key not in values:
            raise SystemExit(f"unknown fact {key!r}")
        tag = f"{key}|{how}" if how else key
        return f"<!--f:{tag}-->{fmt_fact(values[key], how or 'int')}<!--/f-->"

    return FACT.sub(sub, src)


def activity_html(gh):
    """GitHub-style contribution graph for the last 365 days, as inline SVG."""
    end = datetime.date.fromisoformat(gh["totals"]["generated"])
    start = end - datetime.timedelta(days=364)
    grid_start = start - datetime.timedelta(days=(start.weekday() + 1) % 7)  # Sunday on or before
    counts = {}
    for i in range(365):
        d = start + datetime.timedelta(days=i)
        counts[d] = gh["days"].get(d.isoformat(), 0)

    nz = sorted(c for c in counts.values() if c)
    q = [nz[len(nz) // 4], nz[len(nz) // 2], nz[(3 * len(nz)) // 4]] if nz else [1, 2, 3]

    def level(c):
        return 0 if not c else 1 if c <= q[0] else 2 if c <= q[1] else 3 if c <= q[2] else 4

    pitch, cell, left, top = 11, 9, 22, 14
    cols = (end - grid_start).days // 7 + 1
    width, height = left + cols * pitch, top + 7 * pitch

    rects, months, last_month, last_col = [], [], None, -9
    for d, c in counts.items():
        col, row = (d - grid_start).days // 7, (d.weekday() + 1) % 7
        s = "" if c == 1 else "s"
        rects.append(f'<rect x="{left + col * pitch}" y="{top + row * pitch}" width="{cell}" height="{cell}" '
                     f'rx="2" class="l{level(c)}"><title>{d.isoformat()}: {c} contribution{s}</title></rect>')
        if row == 0 or d == start:
            if d.month != last_month and col - last_col >= 3:
                months.append(f'<text x="{left + col * pitch}" y="{top - 5}" class="mo">{d.strftime("%b")}</text>')
                last_month, last_col = d.month, col
    days_lbl = "".join(f'<text x="0" y="{top + r * pitch + cell - 1}" class="dw">{n}</text>'
                       for r, n in ((1, "Mon"), (3, "Wed"), (5, "Fri")))

    total = sum(counts.values())
    active = sum(1 for c in counts.values() if c)
    best = run = 0
    for c in counts.values():
        run = run + 1 if c else 0
        best = max(best, run)

    return (
        f'      <p class="act-sum"><b>{total:,}</b> contributions in the last 365 days &middot; '
        f'<b>{active}</b> active days &middot; longest streak <b>{best}</b> days</p>\n'
        f'      <svg class="act-graph" viewBox="0 0 {width} {height}" role="img" '
        f'aria-label="GitHub contributions per day, last 365 days, {total:,} in total">'
        f'{"".join(months)}{days_lbl}{"".join(rects)}</svg>\n'
        '      <div class="act-legend">Less <i class="l0"></i><i class="l1"></i><i class="l2"></i>'
        '<i class="l3"></i><i class="l4"></i> More</div>')


def main():
    gh = load()
    values = fact_values(gh)
    s = read(ROOT / "index.html")
    s = splice(s, "stats", stats_html(gh))
    s = splice(s, "projects", projects_html(gh))
    s = splice(s, "timeline", timeline_html(gh))
    s = re.sub(r'(Git data generated )[\d-]+', r"\g<1>" + gh["totals"]["generated"], s)
    s = apply_phrases(fill_facts(s, values), values)
    s = bust(s)
    write(ROOT / "index.html", s)

    readme = ROOT / "README.md"
    write(readme, apply_phrases(fill_facts(read(readme), values), values))

    llms = ROOT / "llms.txt"
    write(llms, apply_phrases(read(llms), values))

    cv = ROOT / "cv" / "index.html"
    write(cv, fill_facts(splice(read(cv), "activity", activity_html(gh)), values))
    print(f'pre-rendered {len(gh["projects"])} projects, {len(gh["timeline"])} timeline rows, '
          f'facts and the CV activity graph')


if __name__ == "__main__":
    main()
