# Profile data pipeline

Everything numeric on the portfolio, in the README and on the CV comes from one dataset,
`assets/data.js`, refreshed daily by `.github/workflows/refresh.yml`.

```
build-data.py  ->  assets/data.js  ->  prerender.py  ->  index.html, README.md, llms.txt, cv/index.html
                                                           cv/build-pdf.mjs  ->  cv/Mikael-Rinne-CV.pdf
```

- `build-data.py` pulls contributions, stars, commit and PR counts from the GitHub API.
- `prerender.py` writes them into the pages. Numbers in body text sit between markers such as
  `<!--f:fw_stars-->435<!--/f-->`; add a marker where you want a live number. Known keys are in
  `fact_values()`. The CV activity graph is drawn from the same daily calendar.
- `cv/build-pdf.mjs` prints `cv/index.html` to PDF with a local Chrome or Edge. The CV ships its
  own font (`cv/fonts`, Source Sans 3, SIL OFL) so every machine renders the same pages.

Run it by hand:

```bash
python scripts/build-data.py          # full: needs `gh` signed in as the profile owner
python scripts/prerender.py
vp node cv/build-pdf.mjs              # or: node cv/build-pdf.mjs
```

## The daily job and STATS_TOKEN

The job works without any secret. It then runs `build-data.py --light`, which refreshes the
contribution calendar, stars and public commit and PR counts, and keeps the private-repository
timeline and org-wide PR counts from the last full run.

For the full refresh, add a personal access token (classic) with the `repo` and `read:user`
scopes, authorised for SSO if your organisations require it:

```bash
gh secret set STATS_TOKEN -R rorychatt/rorychatt
```
