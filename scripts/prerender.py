#!/usr/bin/env python3
"""Bake the JS-rendered sections into index.html as static markup.

app.js still renders everything at runtime (it owns the animations and the
heatmap), but agents and crawlers that do not execute JavaScript need the
content in the initial HTML response. This writes the same markup app.js
would produce into the container elements, between BEGIN/END marker comments
so the next run can replace it cleanly.

    python3 scripts/prerender.py
"""
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
    raw = (ROOT / "assets" / "data.js").read_text().strip().rstrip(";")
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


def splice(src, marker, inner):
    """Replace whatever sits inside the marked container with `inner`."""
    begin, end = f"<!-- BEGIN {marker} -->", f"<!-- END {marker} -->"
    pat = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    block = f"{begin}\n{inner}\n      {end}"
    if pat.search(src):
        return pat.sub(lambda _: block, src, count=1)
    raise SystemExit(f"marker {marker!r} not found in index.html")


def main():
    gh = load()
    s = (ROOT / "index.html").read_text()
    s = splice(s, "stats", stats_html(gh))
    s = splice(s, "projects", projects_html(gh))
    s = splice(s, "timeline", timeline_html(gh))
    s = re.sub(r'(Git data generated )[\d-]+', r"\g<1>" + gh["totals"]["generated"], s)
    (ROOT / "index.html").write_text(s)
    print(f'pre-rendered {len(gh["projects"])} projects, {len(gh["timeline"])} timeline rows')


if __name__ == "__main__":
    main()
