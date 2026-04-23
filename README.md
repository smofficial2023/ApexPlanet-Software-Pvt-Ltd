<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>SUBHAJIT MONDAL — Data Analyst Internship Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Syne:wght@400;500;600&display=swap" rel="stylesheet"/>
<style>
  :root {
    --ink: #1a1a2e;
    --ink2: #2d2d4e;
    --muted: #6b6b8a;
    --accent: #3d5a99;
    --accent2: #e76f51;
    --accent3: #2a9d8f;
    --accent4: #f4a261;
    --surface: #f8f7f4;
    --card: #ffffff;
    --border: rgba(26,26,46,0.1);
    --tag-bg: #eef1f8;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Syne', sans-serif;
    background: var(--surface);
    color: var(--ink);
    line-height: 1.6;
  }

  /* HERO */
  .hero {
    background: var(--ink);
    color: #fff;
    padding: 3.5rem 2.5rem 2.5rem;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 320px; height: 320px;
    border-radius: 50%;
    background: rgba(61,90,153,0.3);
  }
  .hero::after {
    content: '';
    position: absolute;
    bottom: -80px; left: 10%;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: rgba(231,111,81,0.15);
  }
  .hero-badge {
    display: inline-block;
    background: rgba(231,111,81,0.2);
    color: #f4a261;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.12em;
    padding: 5px 14px;
    border-radius: 20px;
    border: 1px solid rgba(231,111,81,0.3);
    margin-bottom: 1.25rem;
    text-transform: uppercase;
  }
  .hero h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 2.4rem;
    line-height: 1.15;
    color: #fff;
    margin-bottom: 0.75rem;
    position: relative;
    z-index: 1;
  }
  .hero h1 span { color: var(--accent4); }
  .hero-sub {
    font-size: 15px;
    color: rgba(255,255,255,0.6);
    max-width: 560px;
    margin-bottom: 2rem;
    position: relative;
    z-index: 1;
  }
  .hero-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    position: relative;
    z-index: 1;
  }
  .hero-chip {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    color: rgba(255,255,255,0.8);
    font-size: 12px;
    padding: 5px 14px;
    border-radius: 20px;
    font-family: 'DM Mono', monospace;
  }

  /* NAV */
  .nav-strip {
    background: var(--card);
    border-bottom: 1px solid var(--border);
    padding: 0 2.5rem;
    display: flex;
    gap: 0;
    overflow-x: auto;
  }
  .nav-btn {
    background: none;
    border: none;
    border-bottom: 2.5px solid transparent;
    color: var(--muted);
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 500;
    padding: 14px 18px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.2s;
  }
  .nav-btn:hover { color: var(--ink); }
  .nav-btn.active { color: var(--accent); border-bottom-color: var(--accent); }

  /* SECTIONS */
  .section {
    display: none;
    padding: 2.5rem 2.5rem 0;
    animation: fadeIn 0.3s ease;
  }
  .section.visible { display: block; }
  @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

  .sec-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.5rem;
  }
  .sec-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.8rem;
    color: var(--ink);
    margin-bottom: 1.5rem;
  }

  /* OVERVIEW CARDS */
  .overview-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px,1fr));
    gap: 14px;
    margin-bottom: 2rem;
  }
  .ov-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.25rem;
  }
  .ov-card-icon { font-size: 22px; margin-bottom: 10px; }
  .ov-card-title { font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
  .ov-card-val { font-family: 'DM Mono', monospace; font-size: 11px; color: var(--muted); }

  /* REPO CARDS */
  .repo-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px,1fr));
    gap: 16px;
    margin-bottom: 2rem;
  }
  .repo-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.4rem;
    position: relative;
    overflow: hidden;
    transition: box-shadow 0.2s;
  }
  .repo-card:hover { box-shadow: 0 4px 20px rgba(0,0,0,0.07); }
  .repo-num {
    font-family: 'DM Serif Display', serif;
    font-size: 3rem;
    color: rgba(61,90,153,0.08);
    position: absolute;
    top: 0.5rem; right: 1rem;
    line-height: 1;
  }
  .repo-tag {
    background: var(--tag-bg);
    color: var(--accent);
    font-size: 10px;
    font-family: 'DM Mono', monospace;
    padding: 3px 10px;
    border-radius: 20px;
    display: inline-block;
    margin-bottom: 10px;
  }
  .repo-title { font-size: 15px; font-weight: 600; margin-bottom: 6px; }
  .repo-desc { font-size: 13px; color: var(--muted); margin-bottom: 12px; line-height: 1.5; }
  .repo-tools { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
  .tool-chip {
    background: #f0f4ea;
    color: #3b6010;
    font-size: 10px;
    font-family: 'DM Mono', monospace;
    padding: 3px 9px;
    border-radius: 20px;
  }
  .repo-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 12px;
    color: var(--accent);
    text-decoration: none;
    font-weight: 500;
    background: var(--tag-bg);
    padding: 6px 14px;
    border-radius: 8px;
    border: 1px solid rgba(61,90,153,0.15);
    font-family: 'DM Mono', monospace;
  }
  .repo-link:hover { background: #dce5f5; }

  /* SKILLS */
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px,1fr));
    gap: 14px;
    margin-bottom: 2rem;
  }
  .skill-group {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.25rem;
  }
  .skill-group-title {
    font-size: 12px;
    font-weight: 600;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 10px;
  }
  .skill-item { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; font-size: 13px; }
  .skill-dot { width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0; }
  .dot-blue { background: var(--accent); }
  .dot-orange { background: var(--accent2); }
  .dot-teal { background: var(--accent3); }
  .dot-yellow { background: var(--accent4); }

  /* LEARNINGS */
  .learn-list { list-style: none; margin-bottom: 2rem; }
  .learn-item {
    background: var(--card);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent3);
    border-radius: 10px;
    padding: 1rem 1.25rem;
    margin-bottom: 10px;
    font-size: 14px;
    color: var(--ink2);
  }
  .learn-item strong { color: var(--ink); display: block; font-size: 13px; margin-bottom: 3px; }

  /* REAL WORLD PROBLEMS */
  .rwp-intro {
    background: #fff8f5;
    border: 1px solid rgba(231,111,81,0.2);
    border-left: 4px solid var(--accent2);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1.5rem;
    font-size: 13px;
    color: var(--muted);
  }
  .rwp-intro strong { color: var(--accent2); }

  .problem-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    margin-bottom: 16px;
    overflow: hidden;
  }
  .problem-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.25rem;
    background: #fafafa;
    border-bottom: 1px solid var(--border);
  }
  .problem-header-left { display: flex; align-items: center; gap: 10px; }
  .problem-num {
    width: 28px; height: 28px;
    background: var(--accent2);
    color: #fff;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 600;
    flex-shrink: 0;
  }
  .problem-title-input {
    font-family: 'Syne', sans-serif;
    font-size: 14px;
    font-weight: 600;
    color: var(--ink);
    border: none;
    background: none;
    outline: none;
    width: 280px;
  }
  .problem-title-input::placeholder { color: var(--muted); font-weight: 400; }
  .delete-btn {
    background: none;
    border: none;
    color: #ccc;
    font-size: 18px;
    cursor: pointer;
    line-height: 1;
    padding: 2px 6px;
  }
  .delete-btn:hover { color: #e53e3e; }

  .problem-body {
    padding: 1.25rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  .field-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 6px;
  }
  .field-tag {
    display: inline-block;
    font-size: 10px;
    font-family: 'DM Mono', monospace;
    padding: 2px 8px;
    border-radius: 20px;
    margin-bottom: 6px;
  }
  .tag-problem { background: #fde8e2; color: #c0392b; }
  .tag-solution { background: #e2f5f0; color: #1a7a5e; }
  .tag-impact { background: #fef6e2; color: #a0620a; }
  .tag-tools { background: #e8eef9; color: #2c52a0; }

  .editable-area {
    width: 100%;
    min-height: 80px;
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 10px 12px;
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    color: var(--ink);
    background: #fcfcfc;
    resize: vertical;
    outline: none;
    line-height: 1.6;
    transition: border-color 0.2s;
  }
  .editable-area:focus { border-color: var(--accent); background: #fff; }
  .editable-area::placeholder { color: #bbb; }

  .add-problem-btn {
    display: flex;
    align-items: center;
    gap: 8px;
    background: none;
    border: 1.5px dashed rgba(231,111,81,0.4);
    color: var(--accent2);
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 500;
    padding: 12px 20px;
    border-radius: 12px;
    cursor: pointer;
    width: 100%;
    justify-content: center;
    margin-bottom: 2rem;
    transition: all 0.2s;
  }
  .add-problem-btn:hover { background: #fff8f5; border-color: var(--accent2); }

  /* DECK */
  .deck-card {
    background: var(--ink);
    color: #fff;
    border-radius: 16px;
    padding: 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1.5rem;
    margin-bottom: 1.5rem;
    flex-wrap: wrap;
  }
  .deck-left h3 { font-family: 'DM Serif Display', serif; font-size: 1.4rem; margin-bottom: 0.5rem; }
  .deck-left p { font-size: 13px; color: rgba(255,255,255,0.55); max-width: 380px; }
  .deck-btn {
    background: var(--accent2);
    color: #fff;
    border: none;
    border-radius: 10px;
    padding: 12px 22px;
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    white-space: nowrap;
    flex-shrink: 0;
  }

  .slide-thumbs {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px,1fr));
    gap: 12px;
    margin-bottom: 2rem;
  }
  .slide-thumb {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
  }
  .slide-thumb-icon { font-size: 24px; margin-bottom: 8px; }
  .slide-thumb-title { font-size: 12px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
  .slide-thumb-sub { font-size: 11px; color: var(--muted); font-family: 'DM Mono', monospace; }

  /* COPY SECTION */
  .copy-section {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
  }
  .copy-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  .copy-header h3 { font-size: 14px; font-weight: 600; }
  .copy-btn {
    background: var(--tag-bg);
    border: 1px solid rgba(61,90,153,0.2);
    color: var(--accent);
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    padding: 5px 12px;
    border-radius: 8px;
    cursor: pointer;
  }
  .copy-btn:hover { background: #dce5f5; }
  .code-block {
    background: #1a1a2e;
    color: #a8d8a8;
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    padding: 1rem;
    border-radius: 8px;
    overflow-x: auto;
    line-height: 1.7;
    white-space: pre;
  }

  .divider { height: 1px; background: var(--border); margin: 2rem 0; }

  .footer {
    text-align: center;
    padding: 1.5rem 2.5rem;
    font-size: 12px;
    color: var(--muted);
    font-family: 'DM Mono', monospace;
  }
</style>
</head>
<body>

  <!-- HERO -->
  <div class="hero">
    <div class="hero-badge">Capstone Portfolio · Data Analytics Internship</div>
    <h1>SUBHAJIT MONDAL - DataAnalyst-<span>Internship-Portfolio</span></h1>
    <p class="hero-sub">A master repository integrating all four internship projects — from data wrangling to dashboarding — into one cohesive, career-ready showcase.</p>
    <div class="hero-meta">
      <span class="hero-chip">4 Projects</span>
      <span class="hero-chip">Python · SQL · Power BI · Advance Excel · Google Colab</span>
      <span class="hero-chip">Real-World Problems Solved</span>
      <span class="hero-chip">2026 Summer Internship</span>
    </div>
  </div>

  <!-- NAV -->
  <div class="nav-strip">
    <button class="nav-btn active" onclick="showTab('overview', this)">Overview</button>
    <button class="nav-btn" onclick="showTab('repos', this)">Part Repositories</button>
    <button class="nav-btn" onclick="showTab('problems', this)">Real World Problems Over Customer Attribution and Revenue Analysis in Zepto Pvt. Ltd.</button>
    <button class="nav-btn" onclick="showTab('skills', this)">Skills Demonstrated</button>
    <button class="nav-btn" onclick="showTab('learnings', this)">Key Learnings</button>
    <button class="nav-btn" onclick="showTab('deck', this)">Presentation Deck</button>
    <button class="nav-btn" onclick="showTab('readme', this)">README Code</button>
  </div>

  <!-- OVERVIEW TAB -->
  <div class="section visible" id="tab-overview">
    <p class="sec-label">Capstone Summary</p>
    <h2 class="sec-title">Internship at a Glance</h2>
    <div class="overview-grid">
      <div class="ov-card">
        <div class="ov-card-icon">📁</div>
        <div class="ov-card-title">Total Projects</div>
        <div class="ov-card-val">4 end-to-end data projects</div>
      </div>
      <div class="ov-card">
        <div class="ov-card-icon">🛠</div>
        <div class="ov-card-title">Tools Used</div>
        <div class="ov-card-val">Python, SQL, Excel, Power BI</div>
      </div>
      <div class="ov-card">
        <div class="ov-card-icon">🔍</div>
        <div class="ov-card-title">Domains Covered</div>
        <div class="ov-card-val">Sales · Operations · Finance · HR</div>
      </div>
      <div class="ov-card">
        <div class="ov-card-icon">📊</div>
        <div class="ov-card-title">Deliverables</div>
        <div class="ov-card-val">Dashboards, Reports, Cleaned Datasets, Decks</div>
      </div>
    </div>

    <div class="copy-section">
      <p style="font-size:14px;color:#2d2d4e;line-height:1.8;">
        This repository is the <strong>capstone integration</strong> of my Data Analyst internship. Across four structured parts, I worked on real business datasets — cleaning messy data, building SQL queries, designing dashboards, and presenting actionable insights. Each project tackled a domain-specific problem, and together they demonstrate a complete data analysis workflow from raw data to business decision support.
      </p>
    </div>

    <div class="divider"></div>

    <p class="sec-label">Project Timeline</p>
    <div style="position:relative;padding-left:2rem;border-left:2px solid rgba(26,26,46,0.1);margin-bottom:2rem;">
      <div style="margin-bottom:1.5rem;position:relative;">
        <div style="width:12px;height:12px;background:#3d5a99;border-radius:50%;position:absolute;left:-2.55rem;top:3px;"></div>
        <div style="font-size:11px;font-family:'DM Mono',monospace;color:#6b6b8a;margin-bottom:3px;">Part 01 — Week 1–2</div>
        <div style="font-size:14px;font-weight:600;">Data Cleaning & Wrangling</div>
        <div style="font-size:13px;color:#6b6b8a;">Handled nulls, duplicates, type mismatches, and standardised raw datasets using Python & Pandas.</div>
      </div>
      <div style="margin-bottom:1.5rem;position:relative;">
        <div style="width:12px;height:12px;background:#2a9d8f;border-radius:50%;position:absolute;left:-2.55rem;top:3px;"></div>
        <div style="font-size:11px;font-family:'DM Mono',monospace;color:#6b6b8a;margin-bottom:3px;">Part 02 — Week 3–4</div>
        <div style="font-size:14px;font-weight:600;">SQL Analysis & Reporting</div>
        <div style="font-size:13px;color:#6b6b8a;">Wrote complex queries — CTEs, window functions, joins — to extract KPIs from a relational database.</div>
      </div>
      <div style="margin-bottom:1.5rem;position:relative;">
        <div style="width:12px;height:12px;background:#e76f51;border-radius:50%;position:absolute;left:-2.55rem;top:3px;"></div>
        <div style="font-size:11px;font-family:'DM Mono',monospace;color:#6b6b8a;margin-bottom:3px;">Part 03 — Week 5–6</div>
        <div style="font-size:14px;font-weight:600;">Dashboard Development</div>
        <div style="font-size:13px;color:#6b6b8a;">Built interactive Power BI / Tableau dashboards with drill-down, slicers, and executive summaries.</div>
      </div>
      <div style="position:relative;">
        <div style="width:12px;height:12px;background:#f4a261;border-radius:50%;position:absolute;left:-2.55rem;top:3px;"></div>
        <div style="font-size:11px;font-family:'DM Mono',monospace;color:#6b6b8a;margin-bottom:3px;">Part 04 — Week 7–8</div>
        <div style="font-size:14px;font-weight:600;">Insights & Presentation</div>
        <div style="font-size:13px;color:#6b6b8a;">Synthesised findings into a stakeholder-ready presentation deck with recommendations.</div>
      </div>
    </div>
  </div>

  <!-- REPOS TAB -->
  <div class="section" id="tab-repos">
    <p class="sec-label">GitHub Links</p>
    <h2 class="sec-title">Four Part Repositories</h2>
    <div class="repo-grid">
      <div class="repo-card">
        <div class="repo-num">01</div>
        <div class="repo-tag">Data Wrangling</div>
        <div class="repo-title">Data Cleaning & Preparation</div>
        <div class="repo-desc">Transformed raw, inconsistent datasets into analysis-ready tables using Python and Pandas. Handled outliers, missing values, and schema normalization.</div>
        <div class="repo-tools">
          <span class="tool-chip">Python</span>
          <span class="tool-chip">Matplotlib</span>
          <span class="tool-chip">Pandas</span>
          <span class="tool-chip">NumPy</span>
          <span class="tool-chip">Scikit Learn</span>
        </div>
        <a class="repo-link" href="https://github.com/YourName/Part01-DataCleaning" target="_blank">→ github.com/YourName/Part01</a>
      </div>
      <div class="repo-card">
        <div class="repo-num">02</div>
        <div class="repo-tag">SQL Analysis</div>
        <div class="repo-title">SQL Queries & Data Extraction</div>
        <div class="repo-desc">Designed and executed advanced SQL queries to surface business KPIs from relational databases. Used CTEs, window functions, and subqueries.</div>
        <div class="repo-tools">
          <span class="tool-chip">SQL</span>
          <span class="tool-chip">MySQL</span>
          <span class="tool-chip">PostgreSQL</span>
          <span class="tool-chip">DBVisualizer</span>
        </div>
        <a class="repo-link" href="https://github.com/YourName/Part02-SQLAnalysis" target="_blank">→ github.com/YourName/Part02</a>
      </div>
      <div class="repo-card">
        <div class="repo-num">03</div>
        <div class="repo-tag">Visualization</div>
        <div class="repo-title">Dashboard Development</div>
        <div class="repo-desc">Built executive-level dashboards with dynamic filtering, drill-through pages, and automated refresh pipelines using Power BI and Tableau.</div>
        <div class="repo-tools">
          <span class="tool-chip">Power BI</span>
          <span class="tool-chip">Tableau</span>
          <span class="tool-chip">Excel</span>
          <span class="tool-chip">DAX</span>
        </div>
        <a class="repo-link" href="https://github.com/YourName/Part03-Dashboards" target="_blank">→ github.com/YourName/Part03</a>
      </div>
      <div class="repo-card">
        <div class="repo-num">04</div>
        <div class="repo-tag">Storytelling</div>
        <div class="repo-title">Insights & Final Presentation</div>
        <div class="repo-desc">Packaged all insights into a cohesive narrative deck and written report for stakeholders. Includes methodology, findings, and strategic recommendations.</div>
        <div class="repo-tools">
          <span class="tool-chip">PowerPoint</span>
          <span class="tool-chip">Canva</span>
          <span class="tool-chip">Matplotlib</span>
          <span class="tool-chip">Seaborn</span>
        </div>
        <a class="repo-link" href="https://github.com/YourName/Part04-Presentation" target="_blank">→ github.com/YourName/Part04</a>
      </div>
    </div>
    <p style="font-size:13px;color:#6b6b8a;font-family:'DM Mono',monospace;">⚑ Replace the GitHub links above with your actual repository URLs before publishing.</p>
  </div>

  <!-- REAL WORLD PROBLEMS TAB -->
  <div class="section" id="tab-problems">
    <p class="sec-label">Capstone Feature</p>
    <h2 class="sec-title">Real World Problems Solved</h2>
    <div class="rwp-intro">
      <strong>How to use this section:</strong> Click any field below to type in the problem you faced, the solution you implemented, the business impact, and the tools used. Click "Add New Problem" to document additional challenges.
    </div>
    <div id="problems-container"></div>
    <button class="add-problem-btn" onclick="addProblem()">+ Add New Problem</button>
  </div>

  <!-- SKILLS TAB -->
  <div class="section" id="tab-skills">
    <p class="sec-label">Technical Competencies</p>
    <h2 class="sec-title">Skills Demonstrated</h2>
    <div class="skills-grid">
      <div class="skill-group">
        <div class="skill-group-title">Data Engineering</div>
        <div class="skill-item"><span class="skill-dot dot-blue"></span>Data Cleaning (Pandas)</div>
        <div class="skill-item"><span class="skill-dot dot-blue"></span>ETL Pipeline Design</div>
        <div class="skill-item"><span class="skill-dot dot-blue"></span>Schema Normalization</div>
        <div class="skill-item"><span class="skill-dot dot-blue"></span>Handling Missing Data</div>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">SQL & Databases</div>
        <div class="skill-item"><span class="skill-dot dot-orange"></span>Complex JOINs & Subqueries</div>
        <div class="skill-item"><span class="skill-dot dot-orange"></span>Window Functions</div>
        <div class="skill-item"><span class="skill-dot dot-orange"></span>CTEs & Stored Procs</div>
        <div class="skill-item"><span class="skill-dot dot-orange"></span>Query Optimization</div>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Visualization</div>
        <div class="skill-item"><span class="skill-dot dot-teal"></span>Power BI (DAX, M Query)</div>
        <div class="skill-item"><span class="skill-dot dot-teal"></span>Tableau Dashboards</div>
        <div class="skill-item"><span class="skill-dot dot-teal"></span>Matplotlib & Seaborn</div>
        <div class="skill-item"><span class="skill-dot dot-teal"></span>Excel Charts & Pivot</div>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Analytics & Insight</div>
        <div class="skill-item"><span class="skill-dot dot-yellow"></span>Exploratory Data Analysis</div>
        <div class="skill-item"><span class="skill-dot dot-yellow"></span>KPI Definition & Tracking</div>
        <div class="skill-item"><span class="skill-dot dot-yellow"></span>Statistical Interpretation</div>
        <div class="skill-item"><span class="skill-dot dot-yellow"></span>Business Storytelling</div>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Python Ecosystem</div>
        <div class="skill-item"><span class="skill-dot dot-blue"></span>Pandas / NumPy</div>
        <div class="skill-item"><span class="skill-dot dot-blue"></span>Jupyter Notebooks</div>
        <div class="skill-item"><span class="skill-dot dot-blue"></span>Scikit-learn (basics)</div>
        <div class="skill-item"><span class="skill-dot dot-blue"></span>Openpyxl / XlsxWriter</div>
      </div>
      <div class="skill-group">
        <div class="skill-group-title">Soft Skills</div>
        <div class="skill-item"><span class="skill-dot dot-orange"></span>Stakeholder Communication</div>
        <div class="skill-item"><span class="skill-dot dot-orange"></span>Presentation Design</div>
        <div class="skill-item"><span class="skill-dot dot-orange"></span>Documentation</div>
        <div class="skill-item"><span class="skill-dot dot-orange"></span>Problem Decomposition</div>
      </div>
    </div>
  </div>

  <!-- LEARNINGS TAB -->
  <div class="section" id="tab-learnings">
    <p class="sec-label">Reflections</p>
    <h2 class="sec-title">Key Learnings</h2>
    <ul class="learn-list">
      <li class="learn-item"><strong>Data is never clean in the real world</strong>Real business datasets come with inconsistencies, duplicates, and missing logic. I learned to approach cleaning systematically — auditing before acting, documenting every transformation.</li>
      <li class="learn-item"><strong>SQL is the analyst's superpower</strong>Writing queries that answer business questions quickly changed how I think about data. Learning window functions unlocked a whole new level of insight generation without needing Python at all.</li>
      <li class="learn-item"><strong>Dashboards are conversations, not reports</strong>A great dashboard anticipates the questions a manager will ask and lets them drill down independently. Design and UX matter as much as the data behind it.</li>
      <li class="learn-item"><strong>Insights without context are noise</strong>Every number needs a "so what." I learned to connect data findings to business outcomes — framing results in terms of revenue impact, risk, or opportunity.</li>
      <li class="learn-item"><strong>Documentation is part of the deliverable</strong>Code without comments, dashboards without data dictionaries, and reports without methodology sections are incomplete. Good analysts make their work reproducible and explainable.</li>
      <li class="learn-item"><strong>Iteration beats perfection</strong>Showing a rough analysis early and refining based on feedback produced better outcomes than working in isolation for weeks. Stakeholder input caught assumptions I didn't know I was making.</li>
    </ul>
  </div>

  <!-- DECK TAB -->
  <div class="section" id="tab-deck">
    <p class="sec-label">Final Deliverable</p>
    <h2 class="sec-title">Presentation Deck</h2>
    <div class="deck-card">
      <div class="deck-left">
        <h3>Data Analyst Internship — Final Presentation</h3>
        <p>12-slide capstone deck covering methodology, findings across all four projects, real-world problem solutions, and strategic recommendations.</p>
      </div>
      <button class="deck-btn" onclick="alert('Replace this with a link to your actual deck.')">View Deck ↗</button>
    </div>
    <div class="slide-thumbs">
      <div class="slide-thumb"><div class="slide-thumb-icon">🏠</div><div class="slide-thumb-title">Title Slide</div><div class="slide-thumb-sub">Slide 01</div></div>
      <div class="slide-thumb"><div class="slide-thumb-icon">📋</div><div class="slide-thumb-title">Agenda</div><div class="slide-thumb-sub">Slide 02</div></div>
      <div class="slide-thumb"><div class="slide-thumb-icon">🧹</div><div class="slide-thumb-title">Data Cleaning</div><div class="slide-thumb-sub">Slides 03–04</div></div>
      <div class="slide-thumb"><div class="slide-thumb-icon">🗄️</div><div class="slide-thumb-title">SQL Analysis</div><div class="slide-thumb-sub">Slides 05–06</div></div>
      <div class="slide-thumb"><div class="slide-thumb-icon">📊</div><div class="slide-thumb-title">Dashboards</div><div class="slide-thumb-sub">Slides 07–08</div></div>
      <div class="slide-thumb"><div class="slide-thumb-icon">⚠️</div><div class="slide-thumb-title">Real Problems</div><div class="slide-thumb-sub">Slides 09–10</div></div>
      <div class="slide-thumb"><div class="slide-thumb-icon">💡</div><div class="slide-thumb-title">Recommendations</div><div class="slide-thumb-sub">Slide 11</div></div>
      <div class="slide-thumb"><div class="slide-thumb-icon">🎯</div><div class="slide-thumb-title">Conclusion</div><div class="slide-thumb-sub">Slide 12</div></div>
    </div>
  </div>

  <!-- README CODE TAB -->
  <div class="section" id="tab-readme">
    <p class="sec-label">Copy & Paste</p>
    <h2 class="sec-title">README.md Template</h2>
    <div class="copy-section">
      <div class="copy-header">
        <h3>GitHub README.md (Markdown)</h3>
        <button class="copy-btn" onclick="copyReadme()">Copy ↗</button>
      </div>
      <div class="code-block" id="readme-code"># [YourName] — Data Analyst Internship Portfolio

> A capstone integration of all four internship projects demonstrating
> end-to-end data analytics skills — from raw data to boardroom insights.

---

## Overview

This master repository consolidates my complete internship journey
as a Data Analyst. Each part below represents a standalone project
tackling a real business problem using industry-standard tools.

**Internship Period:** 2024–2025
**Domain Coverage:** Sales · Operations · Finance · HR
**Core Stack:** Python · SQL · Power BI · Excel · Tableau

---

## Part Repositories

| # | Project | Description | Link |
|---|---------|-------------|------|
| 01 | Data Cleaning & Wrangling | Raw to analysis-ready datasets | [→ Repo](https://github.com/YourName/Part01) |
| 02 | SQL Analysis & Reporting | KPI extraction via advanced SQL | [→ Repo](https://github.com/YourName/Part02) |
| 03 | Dashboard Development | Interactive Power BI / Tableau | [→ Repo](https://github.com/YourName/Part03) |
| 04 | Insights & Presentation | Stakeholder deck & recommendations | [→ Repo](https://github.com/YourName/Part04) |

---

## Real World Problems Solved

### Problem 1: [Title]
**Issue:** [Describe the business problem or data challenge]
**Solution:** [What you did to solve it]
**Impact:** [Quantified outcome or business value]
**Tools:** [Tools used]

### Problem 2: [Title]
**Issue:** [Describe the business problem or data challenge]
**Solution:** [What you did to solve it]
**Impact:** [Quantified outcome or business value]
**Tools:** [Tools used]

---

## Skills Demonstrated

- **Data Engineering:** Pandas, ETL design, schema normalization
- **SQL:** Window functions, CTEs, query optimization
- **Visualization:** Power BI (DAX), Tableau, Matplotlib
- **Analytics:** EDA, KPI definition, statistical interpretation
- **Communication:** Stakeholder presentations, documentation

---

## Key Learnings

1. Real-world data is always messier than textbook examples
2. SQL window functions unlock insights without Python overhead
3. Dashboards should anticipate questions, not just display data
4. Every insight needs business context to be actionable
5. Documentation and reproducibility are non-negotiable

---

## Presentation Deck

[View Final Capstone Presentation →](https://link-to-your-deck.com)

---

## Contact

**[YourName]** · [LinkedIn](https://linkedin.com/in/yourname)
· [Email](mailto:you@email.com)</div>
    </div>
  </div>

  <div class="footer">Built for [YourName] · Data Analyst Internship Portfolio · 2024–2025</div>

<script>
  let problemCount = 0;

  function showTab(id, btn) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('visible'));
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.getElementById('tab-' + id).classList.add('visible');
    btn.classList.add('active');
  }

  function addProblem() {
    problemCount++;
    const n = problemCount;
    const container = document.getElementById('problems-container');
    const card = document.createElement('div');
    card.className = 'problem-card';
    card.id = 'problem-' + n;
    card.innerHTML = `
      <div class="problem-header">
        <div class="problem-header-left">
          <div class="problem-num">${n}</div>
          <input class="problem-title-input" type="text" placeholder="Problem title (e.g. 'Duplicate Sales Records Inflating Revenue')">
        </div>
        <button class="delete-btn" onclick="removeProblem(${n})">×</button>
      </div>
      <div class="problem-body">
        <div>
          <div class="field-label"><span class="field-tag tag-problem">Issue</span></div>
          <textarea class="editable-area" placeholder="Describe the real-world problem or challenge you encountered. What was wrong? Who was affected?"></textarea>
        </div>
        <div>
          <div class="field-label"><span class="field-tag tag-solution">Solution</span></div>
          <textarea class="editable-area" placeholder="Explain what you did to solve it — specific steps, queries written, transformations applied, or analysis performed."></textarea>
        </div>
        <div>
          <div class="field-label"><span class="field-tag tag-impact">Impact / Outcome</span></div>
          <textarea class="editable-area" placeholder="What was the measurable result? (e.g. 'Reduced reporting errors by 40%', 'Saved 3 hours/week of manual work')"></textarea>
        </div>
        <div>
          <div class="field-label"><span class="field-tag tag-tools">Tools Used</span></div>
          <textarea class="editable-area" placeholder="List the tools, languages, or methods used (e.g. Python, Pandas, SQL CTEs, Power BI DAX)"></textarea>
        </div>
      </div>
    `;
    container.appendChild(card);
  }

  function removeProblem(n) {
    const el = document.getElementById('problem-' + n);
    if (el) el.remove();
  }

  function copyReadme() {
    const text = document.getElementById('readme-code').innerText;
    navigator.clipboard.writeText(text).then(() => {
      const btn = event.target;
      btn.textContent = 'Copied ✓';
      setTimeout(() => btn.textContent = 'Copy ↗', 2000);
    });
  }

  addProblem();
  addProblem();
</script>
</body>
</html>
