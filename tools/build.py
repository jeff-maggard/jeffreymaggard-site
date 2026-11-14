"""Builds every page in site/ from tools/content.py.  Run:  python3 tools/build.py"""
import os
from pathlib import Path
import hashlib

from art import svg
from content import CATEGORIES, GALLERIES, PROJECTS, TEACHING, TOOLS, VIDEOS

# Projects marked hidden=True are left out of every page and listing.
PROJECTS = [p for p in PROJECTS if not p.get("hidden")]


def ver(rel):
    """Cache-busting stamp for a file under site/, so browsers fetch new CSS/JS after each change."""
    data = (Path(__file__).resolve().parent.parent / "site" / rel).read_bytes()
    return hashlib.md5(data).hexdigest()[:8]

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CAT_NAMES = dict(CATEGORIES)
BY_SLUG = {p["slug"]: p for p in PROJECTS}

NAV = [
    ("Instructional Design", "/instructional-design/"),
    ("Teaching", "/teaching/"),
    ("Studio", "/studio/"),
    ("Cultural Projects", "/cultural-projects/"),
    ("Home", "/"),
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&amp;family=Noto+Naskh+Arabic:wght@400;600&amp;display=swap">
<link rel="stylesheet" href="/css/tokens.css?v={ver("css/tokens.css")}">
<link rel="stylesheet" href="/css/site.css?v={ver("css/site.css")}">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="site-header-bar">
  <header class="site-header container">
    <span class="brand-logo" role="img" aria-label="Jeffrey Maggard">
      <svg class="logo-mark" viewBox="0 0 44 44" width="44" height="44" aria-hidden="true" focusable="false">
        <defs><linearGradient id="lg-jm" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0069D9"/><stop offset="1" stop-color="#6D4AEE"/></linearGradient></defs>
        <rect width="44" height="44" rx="11" fill="url(#lg-jm)"/>
        <path d="M14.5 13v13.2c0 3.1-1.9 4.8-4.6 4.8" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M19.5 31V13l6.2 10.2L31.9 13v18" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="36" cy="31" r="2" fill="#29ABFF"/>
      </svg>
      <span class="logo-text" aria-hidden="true"><span class="logo-first">Jeffrey</span> <span class="logo-last">Maggard</span></span>
    </span>
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
<script src="/js/hero3d.js?v={ver("js/hero3d.js")}" defer></script>
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
      <article class="card" data-cats="{cats}" data-slug="{p['slug']}">
        <div class="thumb">{thumb(p)}</div>
        <div class="card-body">
          <p class="label">{p['tag']}</p>
          <h3><a href="/work/{p['slug']}/">{p['title']}</a></h3>
          <p class="summary">{p['summary']}</p>
          <p class="more" aria-hidden="true">The purpose →</p>
        </div>
      </article>"""


def grid(projects):
    return '<div class="grid">' + "".join(card(p) for p in projects) + "\n    </div>"


def video_exists(key):
    if key in VIDEOS and VIDEOS[key].get("youtube"):
        return True
    return key in VIDEOS and (SITE / VIDEOS[key]["src"].lstrip("/")).exists()


def video(key, heading_level=None):
    if not video_exists(key):
        return ""
    v = VIDEOS[key]
    if v.get("youtube"):
        return f"""
      <figure class="video">
        <a class="yt-lite" style="aspect-ratio:{v['ratio']}" href="https://www.youtube.com/watch?v={v['youtube']}" target="_blank" rel="noopener" aria-label="Play video on YouTube (opens in a new tab): {v['title']}"><img src="{v['poster']}" alt="" loading="lazy"><span class="yt-play" aria-hidden="true"></span><span class="yt-note">Plays on YouTube</span></a>
        <figcaption><b>{v['title']}</b>{v['caption']}</figcaption>
      </figure>"""
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
        f'<a class="shot" href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{alt}" loading="lazy">'
        + (f'<span>{cap[0] if cap else alt}</span>' if (cap[0] if cap else alt) else '') + '</a>'
        for src, alt, *cap in GALLERIES[key]
    )
    return f'<div class="gallery">{items}</div>'


def feature_pair(key):
    """Two artworks side by side at the same height (each flexes by its width/height ratio)."""
    if not key:
        return ""
    from PIL import Image
    items = []
    for src, alt, cap in GALLERIES[key]:
        w, h = Image.open(SITE / src.lstrip("/")).size
        items.append(f'<a class="shot" style="flex:{w / h:.3f} 1 0" href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{alt}" loading="lazy" width="{w}" height="{h}"><span>{cap}</span></a>')
    return f'<div class="feature-pair">{"".join(items)}</div>'


def expand(block):
    block = block.replace("@@CANVAS@@", CANVAS)
    if block.startswith("@gallery:"):
        return gallery(block.split(":", 1)[1])
    if block.startswith("@video:"):
        return video(block.split(":", 1)[1])
    return block


# ---------------------------------------------------------------- pages

SKILLS = ["Course design", "Curriculum", "Assessment", "Textbooks", "Animation", "Launch videos", "AI tutors", "Claude Code", "Storytelling", "Virtual exchange", "Accessibility", "Teacher training"]


# Highlights strip under the Home hero (wording approved by Jeffrey, 14 Nov 2026).
PROOF = [
    "Taught first-year university courses in the USA, Japan, the UAE and Qatar",
    "Political science, sociology, IT and English composition courses",
    "Team-taught across disciplines",
    "UNESCO-funded project lead",
    "Published research on technology and learning",
    "AI-assisted animation, video and course design",
]


def home():
    skills = "".join(f"<span>{k}</span>" for k in SKILLS)
    proof = "".join(f"<li>{x}</li>" for x in PROOF)
    # Same order and names as the top menu.
    btn = lambda k, v: f'<li><button type="button" aria-pressed="false" data-filter="{k}">{v}</button></li>'
    filters = ('<li><button type="button" aria-pressed="true" data-filter="all">All</button></li>'
               + btn("courses", "Instructional Design") + btn("teaching", "Teaching") + btn("video", "Studio")
               + btn("cultural", "Cultural Projects"))
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

  <section class="proof-strip" aria-label="Highlights">
    <ul class="container proof-list">{proof}</ul>
  </section>

  <section class="section container" id="work" aria-labelledby="work-title">
    <div class="section-head">
      <div><p class="label">Featured projects</p><h2 id="work-title">Selected work</h2></div>
      <p>Open any of these projects to see what I did, how I did it, and why.</p>
    </div>
    <ul class="filters" aria-label="Filter projects">{filters}</ul>
    {grid(PROJECTS)}
  </section>
<script>
(function () {{
  // Custom card order for a filter, so a filtered view does not look like the full list.
  var ORDER = {{ teaching: ['peace-studies-seminar', 'sociology-video-course', 'two-country-course'], cultural: ['tales-of-qatari-heritage', 'kamishibai', 'story-mile', 'peace-studies-seminar', 'falcon-folktale'] }};
  var buttons = document.querySelectorAll('[data-filter]');
  var cards = document.querySelectorAll('.grid .card');
  buttons.forEach(function (b) {{
    b.addEventListener('click', function () {{
      var f = b.getAttribute('aria-pressed') === 'true' ? 'all' : b.getAttribute('data-filter');
      buttons.forEach(function (x) {{ x.setAttribute('aria-pressed', x.getAttribute('data-filter') === f ? 'true' : 'false'); }});
      cards.forEach(function (c) {{
        c.hidden = f !== 'all' && c.getAttribute('data-cats').split(' ').indexOf(f) < 0;
        var o = (ORDER[f] || []).indexOf(c.getAttribute('data-slug'));
        c.style.order = o < 0 ? '' : o;
        c.style.gridColumnEnd = (f === 'cultural' && c.getAttribute('data-slug') === 'falcon-folktale') ? '-1' : '';
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
    sk = p.get("skills", {})
    comp = "".join(
        f'<p class="comp-sub">{n}</p><ul class="comp-list">' + "".join(f"<li>{x}</li>" for x in sk[k]) + "</ul>"
        for n, k in (("Core", "core"), ("AI", "ai")) if sk.get(k))
    comp = f'<div><dt class="label">Competencies</dt><dd>{comp}</dd></div>' if comp else ""
    banner = (
        f'<div class="cs-section showcase-head"><h2>Student artwork</h2></div><a class="shot cs-banner" href="{p["banner"]}" target="_blank" rel="noopener"><div class="cs-banner-scroll"><img src="{p["banner"]}" alt="{p.get("banner_alt", "")}" width="3920" height="476"></div><span>{p.get("banner_caption", "")}</span></a>'
        if p.get("banner") else ""
    )
    hero = f'<div class="cs-book">{p["hero_block"]}</div>' if p.get("hero_block") else "" if p.get("banner") else (
        '<div class="cs-logos">' + "".join(f'<img src="{src}" alt="{alt}" loading="lazy">' for src, alt in p["logos"]) + '</div>'
        if p.get("logos") else
        '<div class="cs-shots">' + "".join(f'<a class="shot" href="{src}" target="_blank" rel="noopener"><img src="{src}" alt="{alt}"><span>{cap}</span></a>' for src, alt, cap in p["shots"]) + '</div>'
        if p.get("shots") else
        f'<div class="cs-hero {p.get("hero_class", "")}"><img src="{p.get("hero", p.get("image"))}" alt="{p.get("hero_alt", "")}" style="width:100%;height:100%;object-fit:cover"></div>'
        if p.get("hero") or p.get("image") else '<div class="cs-gap" aria-hidden="true"></div>' if p.get("no_hero") else f'<div class="cs-hero">{svg(p["art"], "Illustration for " + strip(p["title"]))}</div>'
    )
    sections = list(p["sections"])
    purpose_top = ""
    if sections and sections[0][0] == "The purpose" and p.get("showcase_feature"):
        # purpose sits above the student artwork block
        purpose_top = f'<section class="cs-section purpose-top"><h2>The purpose</h2>{"".join(expand(b) for b in sections[0][1])}</section>'
        sections = sections[1:]
    if p.get("video") and video_exists(p["video"]):
        at = 1 if sections and sections[0][0] == "The purpose" else 0
        sections.insert(at, ("Watch", [video(p["video"])]))
    toc = "".join(f'<li><a href="#s{n}">{t}</a></li>' for n, (t, _) in enumerate(sections, 1))
    secs = "".join(
        f'\n      <section class="cs-section" id="s{n}"><h2>{t}</h2>{"".join(expand(b) for b in blocks)}</section>'
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
    {'<div class="cs-gap" aria-hidden="true"></div>' if p.get('shots') or p.get('hero_block') else hero}
    <dl class="facts {'facts-3' if f["tools"] and comp else 'facts-2'}{' facts-top' if p.get('banner') else ''}">
      <div><dt class="label">My role</dt><dd>{f['role']}</dd></div>
      {comp}
      {f'<div><dt class="label">Tools</dt><dd><ul class="chips">{tools}</ul></dd></div>' if f["tools"] else ""}
    </dl>
    {hero if p.get('shots') or p.get('hero_block') else ''}
    {purpose_top}
    {banner}
    {f'<div class="showcase">{feature_pair(p.get("showcase_feature"))}{gallery(p["showcase"]) if p.get("showcase") else ""}<p class="showcase-note">Original artwork by Qatar University Foundation Program students.</p></div>' if p.get("showcase") or p.get("showcase_feature") else ""}
    <div class="cs-body{' cs-body-full' if p.get('no_toc') else ''}">
      {'' if p.get('no_toc') else f'<nav class="cs-toc" aria-label="On this page"><p class="label">On this page</p><ol>{toc}</ol></nav>'}
      <div>{secs}
        {status}
      </div>
    </div>
    <nav class="next-up" aria-label="More projects">
      <a class="button button-secondary" href="/work/{prev_p['slug']}/"><span aria-hidden="true">←</span> {strip(prev_p['title'])}</a>
      <a class="button button-secondary" href="/work/{next_p['slug']}/">{strip(next_p['title'])} <span aria-hidden="true">→</span></a>
    </nav>
  </div>
"""
    return page(strip(p["title"]), body, "", strip(p["summary"]), SCENE_FOR_CAT[p["cats"][0]])


# Hand-picked order for some category pages (slugs first, in this order; the rest follow).
CATEGORY_ORDER = {
    "cultural": ["tales-of-qatari-heritage", "kamishibai", "story-mile", "peace-studies-seminar", "falcon-folktale"],
}


def category_page(cat, title, intro, extra=""):
    projects = [p for p in PROJECTS if cat in p["cats"]]
    order = CATEGORY_ORDER.get(cat, [])
    projects.sort(key=lambda p: order.index(p["slug"]) if p["slug"] in order else len(order))
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
    </section>
    <section class="section" aria-labelledby="comp-title">
      <div class="section-head"><div><p class="label">What I bring</p><h2 id="comp-title">Competencies</h2></div></div>
      <div class="skills-grid comp-grid">
        <div class="skill-col"><p class="label">Teaching and curriculum</p><ul><li>TESOL instruction across proficiency levels</li><li>Curriculum development and delivery</li><li>Active and applied learning</li><li>Faculty mentoring and stakeholder engagement</li></ul></div>
        <div class="skill-col"><p class="label">Assessment and quality</p><ul><li>Assessment design and learning outcomes</li><li>Grading, norming and exam development</li><li>Formative assessment and feedback</li><li>Accreditation and program improvement</li></ul></div>
        <div class="skill-col"><p class="label">Learning technology</p><ul><li>Learning management systems: Blackboard Ultra and Canvas</li><li>SCORM 2004</li><li>Low-code automation: Power Automate and SharePoint</li><li>Motion graphics coded in React with Remotion</li></ul></div>
        <div class="skill-col"><p class="label">AI in education</p><ul><li>Claude (Claude Max): Claude and Claude Code for research, design, coding and production</li><li>AI literacy and critical thinking in education</li><li>AI-assisted web development with Claude Code</li><li>AI agent direction and orchestration</li><li>Quality assurance and workflow design</li></ul></div>
        <div class="skill-col"><p class="label">AI media production</p><ul><li>AI-assisted video and animation production</li><li>Story adaptation and scriptwriting</li><li>Prompt engineering and scene direction</li><li>Character design and visual consistency</li><li>AI voice casting and direction</li><li>Art direction and visual style guides</li><li>Cultural authenticity in AI-generated media</li><li>AI production planning and budgeting</li></ul></div>
    </section>"""
    body = category_page("courses", "Instructional Design &amp; Curriculum",
                         "I design courses, assessments and systems, from scope and sequence to rubrics, so students learn by doing real work.", extra)
    return page("Instructional Design & Curriculum", body, "/instructional-design/", scene="blocks")


def studio():
    side = "".join(video(k) for k in ("falcon-opening", "community-esl") if video_exists(k))
    body = f"""
  <div class="container">
    <section class="page-head">
      <p class="label">Video &amp; animation</p>
      <h1>Studio</h1>
      <span class="bar" aria-hidden="true"></span>
      <p class="intro">I write, design and produce my own learning media: animated stories, launch videos and course websites.</p>
    </section>
    <section class="section" aria-label="Videos">
      <div class="studio-feature">{video("portfolio-video")}</div>
      <div class="studio-row">{side}</div>
    </section>
    <section class="section" aria-labelledby="sp-title">
      <div class="section-head"><div><h2 id="sp-title">Studio projects</h2></div><p>Open any of these projects to see what I did, how I did it, and why.</p></div>
      {grid([p for p in PROJECTS if "video" in p["cats"]])}
    </section>
  </div>
"""
    return page("Studio", body, "/studio/", scene="dunes")


def teaching():
    T = TEACHING
    areas = "".join(
        f'<div class="panel"><p class="label">Courses</p><h3>{x[0]}</h3><p>{x[1]}</p>'
        + (f'<p class="label next-label">{x[2]}</p><p>{x[3]}</p>' if len(x) > 2 else "")
        + '</div>' for x in T["areas"])
    miy = "".join(f'<div class="panel"><p class="label">IT leadership</p><h3>{a}</h3><p>{b}</p></div>' for a, b in T["miyazaki"])
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    svc = "".join(f'<div class="panel"><p class="label">{lab}</p><h3>{h}</h3><ul class="svc-list">{li(items)}</ul></div>' for lab, h, items in T["service_panels"])
    extra = f"""
    <section class="section section-tight" aria-labelledby="now-title">
      <div class="panel"><p class="label">Current role</p><h3 id="now-title">Qatar University</h3><p>{T['current']}</p></div>
    </section>
    <section class="section section-tight" aria-labelledby="areas-title">
      <div class="section-head"><div><p class="label">Teaching</p><h2 id="areas-title">Courses by area</h2></div></div>
      <div class="two-col">{areas}{miy}</div>
    </section>
    <section class="section section-tight" aria-labelledby="rs-title">
      <div class="section-head"><div><p class="label">Research and service</p><h2 id="rs-title">Research and service</h2></div></div>
      <div class="two-col">{svc}</div>
    </section>
    <section class="section section-tight" aria-labelledby="edu-title">
      <div class="two-col">
        <div><p class="label">About</p><h2 class="sub" id="edu-title">Education and languages</h2><ul class="refs">{li(T['education'])}</ul></div>
      </div>
    </section>
    <section class="section section-tight" aria-labelledby="pub-title">
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
          "I lead projects that collect, publish and perform folktales, and I build seminars and exchanges that connect students with communities in Japan, Mongolia, Cambodia, the UAE and Qatar."))
    write("contact/index.html", contact())
    print("built", len(PROJECTS), "projects")


if __name__ == "__main__":
    main()
