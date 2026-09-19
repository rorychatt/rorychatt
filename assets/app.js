/* Portfolio renderer — all data comes from window.GH (assets/data.js),
   generated from the GitHub API by scripts/build-data.py */
(function () {
  'use strict';
  var GH = window.GH;
  if (!GH) return;

  var LANG_COLOR = {
    'C#': '#8b5cf6', 'TypeScript': '#3b82f6', 'Rust': '#f97316',
    'JavaScript': '#eab308', 'Python': '#22c55e', 'Fortran': '#ec4899',
    'Shell': '#64748b', 'HTML': '#ef4444', 'Jupyter Notebook': '#f59e0b',
    'Dart': '#06b6d4', 'Java': '#f43f5e', 'C': '#94a3b8', 'TeX': '#a3a3a3'
  };
  function lc(l) { return LANG_COLOR[l] || '#6b7a90'; }
  function num(n) { return n.toLocaleString('en-US'); }
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    return e;
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  /* ---------- stat strip (counts up) ---------- */
  var STATS = [
    [GH.totals.contributions, 'Contributions since 2023'],
    [GH.projects.reduce(function (s, p) { return s + p.commits; }, 0), 'Commits in top projects'],
    [GH.totals.repos, 'Repositories touched'],
    [GH.projects.reduce(function (s, p) { return s + p.stars; }, 0), 'Stars on shipped work'],
    [3, 'Years of history shown']
  ];
  var statsEl = document.getElementById('stats');
  STATS.forEach(function (s) {
    var d = el('div', 'stat');
    // render the real value up front so it is correct without JS animation
    var b = el('b', null, num(s[0]));
    b.dataset.to = s[0];
    d.appendChild(b);
    d.appendChild(el('span', null, s[1]));
    statsEl.appendChild(d);
  });
  function countUp(b) {
    var to = +b.dataset.to, t0 = performance.now(), dur = 1100;
    function step(t) {
      var p = Math.min(1, (t - t0) / dur);
      var e = 1 - Math.pow(1 - p, 3);
      b.textContent = num(Math.round(to * e));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /* ---------- top projects ---------- */
  var grid = document.getElementById('projects-grid');
  GH.projects.forEach(function (p, i) {
    var c = el('article', 'proj reveal');
    var stars = p.stars > 0 ? '<span class="pill star">★ ' + p.stars + '</span>' : '';
    c.innerHTML =
      '<div class="proj-top"><span class="rank">' + String(i + 1).padStart(2, '0') + '</span>' +
      '<h3><a href="' + p.url + '" target="_blank" rel="noopener">' + esc(p.name) + '</a></h3></div>' +
      '<div class="slug">' + esc(p.full) + '</div>' +
      '<p class="desc">' + esc(p.desc) + '</p>' +
      '<p class="role">' + esc(p.role) + '</p>' +
      '<div class="proj-meta">' +
        '<span class="pill commits">' + num(p.commits) + ' commits</span>' +
        stars +
        '<span class="pill lang" style="--d:' + lc(p.lang) + '">' + esc(p.lang) + '</span>' +
        '<span class="pill">' + esc(p.period) + '</span>' +
      '</div>';
    grid.appendChild(c);
  });

  /* ---------- contribution heatmap ---------- */
  var days = GH.days;
  var dates = Object.keys(days).sort();
  var counts = dates.map(function (d) { return days[d]; }).filter(function (n) { return n > 0; })
    .sort(function (a, b) { return a - b; });
  function q(p) { return counts[Math.floor(counts.length * p)] || 1; }
  var T = [q(0.25), q(0.5), q(0.75), q(0.92)];
  function level(n) {
    if (!n) return 0;
    if (n <= T[0]) return 1;
    if (n <= T[1]) return 2;
    if (n <= T[2]) return 3;
    return 4;
  }

  var byYear = {};
  dates.forEach(function (d) { (byYear[d.slice(0, 4)] = byYear[d.slice(0, 4)] || []).push(d); });

  var hm = document.getElementById('heatmap');
  Object.keys(byYear).sort().forEach(function (y) {
    var list = byYear[y];
    var total = list.reduce(function (s, d) { return s + days[d]; }, 0);
    var active = list.filter(function (d) { return days[d] > 0; }).length;

    var box = el('div', 'hm-year');
    box.appendChild(el('div', 'hm-year-head',
      '<b>' + y + '</b><span>' + num(total) + ' contributions · ' + active + ' active days</span>'));

    var g = el('div', 'hm-grid');
    // pad so each column is a real Sun–Sat week
    var pad = new Date(list[0] + 'T00:00:00Z').getUTCDay();
    for (var i = 0; i < pad; i++) g.appendChild(el('span', 'hm-d'));
    list.forEach(function (d) {
      var n = days[d];
      var s = el('span', 'hm-d');
      s.dataset.l = level(n);
      s.title = d + ' — ' + n + (n === 1 ? ' contribution' : ' contributions');
      g.appendChild(s);
    });
    box.appendChild(g);
    hm.appendChild(box);
  });
  // start scrolled to the most recent activity
  requestAnimationFrame(function () { hm.scrollLeft = hm.scrollWidth; });

  /* ---------- language bar ---------- */
  var langs = Object.keys(GH.langCommits)
    .map(function (k) { return [k, GH.langCommits[k]]; })
    .sort(function (a, b) { return b[1] - a[1]; });
  var langTotal = langs.reduce(function (s, l) { return s + l[1]; }, 0);
  var bar = document.getElementById('langbar'), keys = document.getElementById('langkeys');
  langs.forEach(function (l) {
    var pct = l[1] / langTotal * 100;
    if (pct < 0.4) return;
    var i = el('i');
    i.style.cssText = 'width:' + pct + '%;background:' + lc(l[0]);
    i.title = l[0] + ' — ' + num(l[1]) + ' commits (' + pct.toFixed(1) + '%)';
    bar.appendChild(i);
    keys.appendChild(el('span', null,
      '<i style="background:' + lc(l[0]) + '"></i><b>' + esc(l[0]) + '</b> ' + pct.toFixed(1) + '%'));
  });

  /* ---------- chronological timeline ---------- */
  var MILESTONES = {
    '2022': ['Joined University of Tartu Institute of Technology as engineer &amp; researcher'],
    '2023': ['Founded SpaceCorps Technology OÜ', 'First-author paper at IEEE IVNC 2023', 'Joined Nixor EE AS'],
    '2024': ['Graduated BSc Chemistry, University of Tartu', 'Completed SALT full-stack C# programme', 'Joined Scania as Solutions Architect'],
    '2025': ['Became 1st Founding Engineer at Ivy'],
    '2026': ['Ivy raising $5M seed · SpaceCorps launching summer 2026']
  };

  var tlEl = document.getElementById('timeline-list');
  var groups = {};
  GH.timeline.forEach(function (r) { (groups[r.from] = groups[r.from] || []).push(r); });
  // milestone-only years (e.g. 2022) still deserve a row
  Object.keys(MILESTONES).forEach(function (y) { groups[y] = groups[y] || []; });
  var years = Object.keys(groups).sort();
  var maxCommits = Math.max.apply(null, GH.timeline.map(function (r) { return r.commits; }));

  years.forEach(function (y) {
    var items = groups[y].sort(function (a, b) { return b.commits - a.commits; });
    var yTotal = items.reduce(function (s, r) { return s + r.commits; }, 0);

    var sub = items.length
      ? items.length + ' repos started · ' + num(yTotal) + ' commits'
      : 'before the git history shown here';
    tlEl.appendChild(el('div', 'tl-year', y + '<small>' + sub + '</small>'));

    (MILESTONES[y] || []).forEach(function (m) {
      var row = el('div', 'tl-row');
      row.innerHTML = '<div class="tl-name"><span class="tl-tag" style="border-color:rgba(240,171,252,.4);' +
        'color:#f0abfc">milestone</span><span style="color:#e8edf5">' + m + '</span></div><div class="tl-right"></div>';
      tlEl.appendChild(row);
    });

    var wrap = el('div', 'tl-items');
    items.forEach(function (r) {
      var parts = r.full.split('/');
      var span = r.to !== r.from ? r.from + '–' + r.to : r.from;
      var row = el('div', 'tl-row');
      var nameHtml = r.priv
        ? '<span style="color:#e8edf5;font-weight:500">' + esc(parts[1]) + '</span>'
        : '<a href="https://github.com/' + esc(r.full) + '" target="_blank" rel="noopener">' + esc(parts[1]) + '</a>';
      row.innerHTML =
        '<div class="tl-name">' +
          '<span class="org">' + esc(parts[0]) + '/</span>' + nameHtml +
          (r.lang ? '<span class="tl-tag" style="border-color:' + lc(r.lang) + '55;color:' + lc(r.lang) + '">' + esc(r.lang) + '</span>' : '') +
          (r.priv ? '<span class="tl-tag">private</span>' : '') +
          (span !== r.from ? '<span class="tl-tag">' + span + '</span>' : '') +
        '</div>' +
        '<div class="tl-right">' +
          '<span class="tl-bar"><i style="width:' + Math.max(3, r.commits / maxCommits * 100) + '%"></i></span>' +
          '<span class="tl-n">' + num(r.commits) + '</span>' +
        '</div>';
      wrap.appendChild(row);
    });
    tlEl.appendChild(wrap);
  });

  /* ---------- footer note ---------- */
  document.getElementById('foot-note').textContent =
    'Built with no framework. Git data generated ' + GH.totals.generated + '.';

  /* ---------- reveal on scroll + stat count-up ---------- */
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('in');
      io.unobserve(e.target);
    });
  }, { rootMargin: '0px 0px -40px 0px' });
  document.querySelectorAll('.reveal').forEach(function (n) { io.observe(n); });

  var statsSeen = false;
  var io2 = new IntersectionObserver(function (entries) {
    if (statsSeen || !entries.some(function (e) { return e.isIntersecting; })) return;
    statsSeen = true;
    document.querySelectorAll('.stat b').forEach(countUp);
    io2.disconnect();
  });
  io2.observe(statsEl);
})();
