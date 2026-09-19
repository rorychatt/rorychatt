# Hi, I'm Mikael Rinne 👋

**1st Founding Engineer [@Ivy-Interactive](https://github.com/Ivy-Interactive)** · **Founder & CEO [@SpaceCorps](https://github.com/SpaceCorps)**

Full-stack engineer from Estonia, based in Stockholm. Background in machine learning, chemistry and physics — first-author on an IEEE IVNC 2023 paper written with CERN collaborators. These days I build .NET/AI/Rust developer tooling at Ivy.

🌐 **[rorychatt.github.io/rorychatt](https://rorychatt.github.io/rorychatt/)** — portfolio, three years of git history, and a live contribution heatmap

---

<details>
<summary>About this repository</summary>

This repo is both my GitHub profile README and the source of my portfolio site, deployed to GitHub Pages.

```
index.html          the whole page
assets/style.css    styles
assets/app.js       renderers: heatmap, project cards, timeline, language bar
assets/data.js      generated — GitHub contribution data
scripts/build-data.py   regenerates assets/data.js from the GitHub API
scripts/projects.json   curated top-project narratives (commit counts come from the API)
```

To refresh the git history shown on the site:

```bash
python3 scripts/build-data.py   # needs the `gh` CLI, authenticated
```

No framework, no build step, no dependencies — it's three static files.

</details>
