"""Builds every page in site/ from tools/content.py.  Run:  python3 tools/build.py"""
import os
from pathlib import Path

from art import svg
from content import CATEGORIES, GALLERIES, PROJECTS, TEACHING, TOOLS, VIDEOS

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CAT_NAMES = dict(CATEGORIES)
BY_SLUG = {p["slug"]: p for p in PROJECTS}

NAV = [
    ("Instructional Design", "/instructional-design/"),
    ("Teaching", "/teaching/"),
    ("Studio", "/studio/"),
    ("Cultural Projects", "/cultural-projects/"),
    ("AI Projects", "/ai-projects/"),
]
EMAIL = "jeff@jeffreymaggard.com"
LINKEDIN = "https://www.linkedin.com/in/jeff-maggard-a01181b3"
LEAD = "I design courses, materials and programs that help students learn by doing real work. I use AI to speed up design, while students keep their own voice."


SCENE_FOR_CAT = {"courses": "blocks", "video": "dunes", "ai": "network", "cultural": "paper", "teaching": "rings"}
CANVAS = '<canvas class="hero3d" aria-hidden="true"></canvas>'


def band_head(body, scene):
    """Move the first page-head into a full-width 3D header band."""
    start = '  <div class="container">\n    <section class="page-head">'
    if not scene or start not in body:
        return body
    i = body.index(start)
    j = body.index("</section>", i) + len("</section>")
    head = body[i + len('  <div class="container">\n'):j]
    return (body[:i] + f'  <div class="hero3d-band" data-scene="{scene}">{CANVAS}\n  <div class="container">\n' + head
            + '\n  </div>\n  </div>\n  <div class="container">' + body[j:])


def page(title, body, current="", description=LEAD, scene="rings"):
    body = band_head(body, scene)
    nav = "".join(
        f'<li><a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a></li>'
        for label, href in NAV
    )
    cta_current = ' aria-current="page"' if current == "/contact/" else ""
    full_title = "Jeffrey Maggard · Instructional Design, Teaching and AI" if not title else f"{title} · Jeffrey Maggard"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#FFFFFF">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&amp;display=swap">
<link rel="stylesheet" href="/css/tokens.css">
<link rel="stylesheet" href="/css/site.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="site-header-bar">
  <header class="site-header container">
    <a class="wordmark" href="/" aria-label="Jeffrey Maggard, home">jeffrey<span class="dot">.</span>maggard</a>
    <nav class="site-nav" aria-label="Main">
      <ul>{nav}<li class="nav-cta"><a href="/contact/"{cta_current}>Let’s talk</a></li></ul>
    </nav>
  </header>
</div>

<main id="main">
{body}
  <section class="cta" aria-labelledby="cta-title">
    <div class="cta-inner container">
      <h2 id="cta-title">Have a learning project? <span class="accent">Let’s talk.</span></h2>
      <div class="cta-links">
        <a class="button button-primary" href="mailto:{EMAIL}">Email me</a>
        <a class="link-plain" href="{LINKEDIN}" rel="noopener">LinkedIn</a>
      </div>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="container"><p>© Jeffrey Maggard</p><p><a href="mailto:{EMAIL}">Email me</a> · <a href="{LINKEDIN}" rel="noopener">LinkedIn</a></p></div>
</footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js" defer></script>
<script src="/js/hero3d.js" defer></script>
</body>
</html>
"""


def thumb(p, label=None):
    label = label or f"Illustration for {strip(p['title'])}"
    if p.get("image"):
        return f'<img src="{p["image"]}" alt="" loading="lazy" width="800" height="500" style="width:100%;height:100%;object-fit:cover">'
    return svg(p["art"], label)


def strip(html):
    import re
    return re.sub(r"<[^>]+>", "", html).replace("&amp;", "&")


def card(p):
    cats = " ".join(p["cats"])
    return f"""
      <article class="card" data-cats="{cats}">
        <div class="thumb">{thumb(p)}</div>
        <div class="card-body">
          <p class="label">{p['tag']}</p>
          <h3><a href="/work/{p['slug']}/">{p['title']}</a></h3>
          <p class="summary">{p['summary']}</p>
          <p class="more" aria-hidden="true">Read case study →</p>
        </div>
      </article>"""


def grid(projects):
    return '<div class="grid">' + "".join(card(p) for p in projects) + "\n    </div>"


def video_exists(key):
    return key in VIDEOS and (SITE / VIDEOS[key]["src"].lstrip("/")).exists()


def video(key, heading_level=None):
    if not video_exists(key):
        return ""
    v = VIDEOS[key]
    poster = f' poster="{v["poster"]}"' if (SITE / v["poster"].lstrip("/")).exists() else ""
    tall = " video-tall" if v.get("ratio") == "4 / 5" else ""
    return f"""
      <figure class="video{tall}">
        <video controls playsinline preload="none"{poster} style="aspect-ratio:{v['ratio']}">
          <source src="{v['src']}" type="video/mp4">
        </video>
        <figcaption><b>{v['title']}</b>{v['caption']}</figcaption>
      </figure>"""


def gallery(key):
    items = "".join(
        f'<a class="shot" href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{alt}" loading="lazy"><span>{alt}</span></a>'
        for src, alt in GALLERIES[key]
    )
    return f'<div class="gallery">{items}</div>'


def expand(block):
    if block.startswith("@gallery:"):
        return gallery(block.split(":", 1)[1])
    if block.startswith("@video:"):
        return video(block.split(":", 1)[1])
    return block


# ---------------------------------------------------------------- pages

SKILLS = ["Course design", "Curriculum", "Assessment", "Textbooks", "Animation", "Launch videos", "AI tutors", "Claude Code", "Storytelling", "Virtual exchange", "Accessibility", "Teacher training"]


def home():
    skills = "".join(f"<span>{k}</span>" for k in SKILLS)
    filters = '<li><button type="button" aria-pressed="true" data-filter="all">All work</button></li>' + "".join(
        f'<li><button type="button" aria-pressed="false" data-filter="{k}">{v}</button></li>' for k, v in CATEGORIES
    )
    body = f"""
  <div class="hero3d-band home-band" data-scene="globe">{CANVAS}
  <section class="hero container" aria-labelledby="hero-title">
    <p class="label">// Instructional Design · Teaching · AI</p>
    <div class="hero-top">
      <h1 id="hero-title">Curriculum designer. Program builder. Teacher.</h1>
      <div class="portrait-frame">
        <img class="portrait" src="/img/jeff-maggard-portrait-560.jpg" srcset="/img/jeff-maggard-portrait-560.jpg 560w, /img/jeff-maggard-portrait-840.jpg 840w" sizes="300px" width="560" height="700" alt="Portrait of Jeffrey Maggard" fetchpriority="high">
      </div>
    </div>
    <span class="bar" aria-hidden="true"></span>
    <div class="hero-bottom">
      <p class="lead">{LEAD}</p>
      <div class="actions">
        <a class="button button-primary" href="mailto:{EMAIL}">Contact me</a>
        <a class="button button-secondary" href="#work">Projects <span aria-hidden="true">↓</span></a>
      </div>
    </div>
  </section>
  </div>

  <div class="alt">
  <section class="section container" id="studio-reel" aria-labelledby="reel-title">
    <div class="section-head">
      <div><p class="label">Studio</p><h2 id="reel-title">Media production</h2></div>
      <p>Animation, launch videos and course websites I design and produce.</p>
    </div>
    <div class="reel">
      <a class="reel-3d hero3d-band" data-scene="animation" href="/studio/" aria-label="Cartoon production: see the studio">{CANVAS}<span class="reel-3d-label"><span class="label">Animation</span><b>From story to screen</b><span>Storyboards, a locked Character Guide and AI animation for my Qatari folktale series.</span></span></a>
      <div class="reel-side">
        {video("portfolio-video")}
        <a class="button button-primary" href="/studio/">See the studio <span aria-hidden="true">→</span></a>
      </div>
    </div>
  </section>
  </div>

  <section class="section container" id="work" aria-labelledby="work-title">
    <div class="section-head">
      <div><p class="label">Featured projects</p><h2 id="work-title">Selected work</h2></div>
      <p>{len(PROJECTS)} projects. Each one opens a case study.</p>
    </div>
    <ul class="filters" aria-label="Filter projects">{filters}</ul>
    {grid(PROJECTS)}
  </section>
<script>
(function () {{
  var buttons = document.querySelectorAll('[data-filter]');
  var cards = document.querySelectorAll('.grid .card');
  buttons.forEach(function (b) {{
    b.addEventListener('click', function () {{
      var f = b.getAttribute('data-filter');
      buttons.forEach(function (x) {{ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }});
      cards.forEach(function (c) {{
        c.hidden = f !== 'all' && c.getAttribute('data-cats').split(' ').indexOf(f) < 0;
      }});
    }});
  }});
}})();
</script>
"""
    return page("", body, "/", scene=None)


def case_study(p, i):
    f = p["facts"]
    tools = "".join(f"<li>{t}</li>" for t in f["tools"])
    hero = (
        f'<div class="cs-hero"><img src="{p.get("hero", p.get("image"))}" alt="" style="width:100%;height:100%;object-fit:cover"></div>'
        if p.get("hero") or p.get("image") else f'<div class="cs-hero">{svg(p["art"], "Illustration for " + strip(p["title"]))}</div>'
    )
    sections = []
    if p.get("video") and video_exists(p["video"]):
        sections.append(("Watch", [video(p["video"])]))
    sections += p["sections"]
    toc = "".join(f'<li><a href="#s{n}">{t}</a></li>' for n, (t, _) in enumerate(sections, 1))
    secs = "".join(
        f'\n      <section class="cs-section" id="s{n}"><h2><span class="n">{n:02d}</span>{t}</h2>{"".join(expand(b) for b in blocks)}</section>'
        for n, (t, blocks) in enumerate(sections, 1)
    )
    status = f'<p class="note" style="margin-top:40px">{p["status"]}</p>' if p.get("status") else ""
    prev_p = PROJECTS[i - 1]
    next_p = PROJECTS[(i + 1) % len(PROJECTS)]
    body = f"""
  <div class="container">
    <section class="page-head">
      <p class="breadcrumb"><a href="/#work">← All work</a></p>
      <p class="label">{p['tag']}</p>
      <h1>{p['title']}</h1>
      <span class="bar" aria-hidden="true"></span>
      <p class="intro">{p['hook']}</p>
    </section>
    {hero}
    <dl class="facts">
      <div><dt class="label">The challenge</dt><dd>{f['context']}</dd></div>
      <div><dt class="label">Audience</dt><dd>{f['audience']}</dd></div>
      <div><dt class="label">My role</dt><dd>{f['role']}</dd></div>
      <div><dt class="label">Tools</dt><dd><ul class="chips">{tools}</ul></dd></div>
    </dl>
    <div class="cs-body">
      <nav class="cs-toc" aria-label="On this page"><p class="label">On this page</p><ol>{toc}</ol></nav>
      <div>{secs}
        {status}
      </div>
    </div>
    <nav class="next-up" aria-label="More case studies">
      <a class="button button-secondary" href="/work/{prev_p['slug']}/"><span aria-hidden="true">←</span> {strip(prev_p['title'])}</a>
      <a class="button button-secondary" href="/work/{next_p['slug']}/">{strip(next_p['title'])} <span aria-hidden="true">→</span></a>
    </nav>
  </div>
"""
    return page(strip(p["title"]), body, "", strip(p["summary"]), SCENE_FOR_CAT[p["cats"][0]])


def category_page(cat, title, intro, extra=""):
    projects = [p for p in PROJECTS if cat in p["cats"]]
    body = f"""
  <div class="container">
    <section class="page-head">
      <p class="label">{CAT_NAMES[cat]}</p>
      <h1>{title}</h1>
      <span class="bar" aria-hidden="true"></span>
      <p class="intro">{intro}</p>
    </section>
    <section class="section" aria-label="Projects">
      {grid(projects)}
    </section>
    {extra}
  </div>
"""
    return body


def instructional_design():
    extra = f"""
    <section class="section" aria-labelledby="tools-title">
      <div class="panel"><p class="label">Toolkit</p><h3 id="tools-title">Tools I design with</h3><p>{TOOLS}</p></div>
    </section>"""
    body = category_page("courses", "Instructional Design &amp; Curriculum",
                         "I design courses, assessments and materials, from scope and sequence to rubrics.", extra)
    return page("Instructional Design & Curriculum", body, "/instructional-design/", scene="blocks")


def studio():
    vids = "".join(video(k) for k in VIDEOS if video_exists(k))
    extra = f"""
    <section class="section" aria-labelledby="cg-title">
      <div class="section-head"><div><p class="label">Animation</p><h2 id="cg-title">Character Guide</h2></div>
      <p>Locked faces, outfits and turnarounds for the folktale series.</p></div>
      {gallery("cast")}
    </section>
    <section class="section" aria-labelledby="ad-title">
      <div class="section-head"><div><p class="label">Animation</p><h2 id="ad-title">Art direction and storyboards</h2></div></div>
      {gallery("art")}
      <div style="height:20px"></div>
      {gallery("storyboard")}
    </section>"""
    body = f"""
  <div class="container">
    <section class="page-head">
      <p class="label">Video &amp; animation</p>
      <h1>Studio</h1>
      <span class="bar" aria-hidden="true"></span>
      <p class="intro">I write, design and produce my own learning media: animated stories, launch videos and course websites.</p>
    </section>
    <section class="section" aria-label="Videos"><div class="videos">{vids}</div></section>
    {extra}
    <section class="section" aria-labelledby="sp-title">
      <div class="section-head"><div><p class="label">Case studies</p><h2 id="sp-title">Studio projects</h2></div></div>
      {grid([p for p in PROJECTS if "video" in p["cats"]])}
    </section>
  </div>
"""
    return page("Studio", body, "/studio/", scene="dunes")


def teaching():
    T = TEACHING
    areas = "".join(f'<div class="panel"><p class="label">Courses</p><h3>{a}</h3><p>{b}</p></div>' for a, b in T["areas"])
    miy = "".join(f'<div class="panel"><p class="label">Miyazaki</p><h3>{a}</h3><p>{b}</p></div>' for a, b in T["miyazaki"])
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    extra = f"""
    <section class="section" aria-labelledby="now-title">
      <div class="panel panel-photo"><p class="label">Current role</p><h3 id="now-title">Qatar University</h3><p>{T['current']}</p></div>
    </section>
    <section class="section" aria-labelledby="areas-title">
      <div class="section-head"><div><p class="label">Teaching</p><h2 id="areas-title">Courses by area</h2></div></div>
      <div class="two-col">{areas}{miy}</div>
    </section>
    <section class="section" aria-labelledby="rs-title">
      <div class="two-col">
        <div><p class="label">Research and service</p><h2 class="sub" id="rs-title">Research and service</h2><ul class="refs">{li(T['service'])}</ul></div>
        <div><p class="label">About</p><h2 class="sub">Education and languages</h2><ul class="refs">{li(T['education'])}</ul></div>
      </div>
    </section>
    <section class="section" aria-labelledby="pub-title">
      <div class="two-col">
        <div><p class="label">Writing</p><h2 class="sub" id="pub-title">Selected publications</h2><ul class="refs">{li(T['publications'])}</ul></div>
        <div><p class="label">Speaking</p><h2 class="sub">Selected presentations</h2><ul class="refs">{li(T['presentations'])}</ul></div>
      </div>
    </section>"""
    body = category_page("teaching", "Teaching &amp; Academic Work", T["intro"], extra)
    return page("Teaching & Academic Work", body, "/teaching/", scene="rings")


def simple_category(cat, path, title, intro):
    return page(strip(title), category_page(cat, title, intro), path, scene=SCENE_FOR_CAT[cat])


def contact():
    body = f"""
  <div class="container">
    <section class="page-head">
      <p class="label">Contact</p>
      <h1>Let’s work together.</h1>
      <span class="bar" aria-hidden="true"></span>
      <p class="intro">Open to instructional design, curriculum and university teaching roles.</p>
    </section>
    <section class="section">
      <div class="two-col">
        <div class="panel"><p class="label">Email</p><h3><a href="mailto:{EMAIL}">{EMAIL}</a></h3><p>The fastest way to reach me.</p></div>
        <div class="panel"><p class="label">LinkedIn</p><h3><a href="{LINKEDIN}" rel="noopener">jeff-maggard</a></h3><p>Career history and recommendations.</p></div>
      </div>
    </section>
  </div>
"""
    return page("Contact", body, "/contact/")


def not_found():
    body = """
  <div class="container">
    <section class="page-head">
      <p class="label">404</p>
      <h1>This page isn’t here.</h1>
      <span class="bar" aria-hidden="true"></span>
      <p class="intro">Try the home page, or browse the work.</p>
    </section>
    <p style="padding-bottom:96px"><a class="button button-primary" href="/">Go to home</a></p>
  </div>
"""
    return page("Page not found", body)


def write(path, html):
    out = SITE / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def main():
    write("index.html", home())
    write("404.html", not_found())
    for i, p in enumerate(PROJECTS):
        write(f"work/{p['slug']}/index.html", case_study(p, i))
    write("instructional-design/index.html", instructional_design())
    write("teaching/index.html", teaching())
    write("studio/index.html", studio())
    write("cultural-projects/index.html", simple_category("cultural", "/cultural-projects/", "Cultural Projects",
          "Folktales, museum work, storytelling programs and seminars that connect students to cultures and communities."))
    write("ai-projects/index.html", simple_category("ai", "/ai-projects/", "AI Projects",
          "AI tools and AI-aware courses I design and build with Claude and Claude Code."))
    write("contact/index.html", contact())
    print("built", len(PROJECTS), "case studies")


if __name__ == "__main__":
    main()
