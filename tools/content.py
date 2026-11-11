"""All site content. Facts come only from docs/site-package.md and Jeffrey's own project records.
Each project becomes a card on Home and a case-study page at /work/<slug>/."""

CATEGORIES = [
    ("courses", "Courses & curriculum"),
    ("video", "Video & animation"),
    ("ai", "AI & apps"),
    ("cultural", "Cultural projects"),
    ("teaching", "Teaching & research"),
]

# Video files live in site/media/. A video only appears if its file exists.
VIDEOS = {
    "falcon-opening": dict(
        src="/media/falcon-opening.mp4", poster="/media/falcon/poster.jpg", ratio="16 / 9",
        title="He Who Doesn’t Know the Falcon Roasts It · Episode 1 opening",
        caption="I wrote and produced this 68-second opening for Episode 1 of my animated folktale series: title, story crawl and sunrise, in 2D animation with a Pixar-inspired look.",
    ),
    "pure-intellect-tutor": dict(
        src="/media/pure-intellect-tutor.mp4", poster="/media/pure-intellect-tutor.jpg", ratio="4 / 5",
        title="Pure Intellect Tutor · launch video",
        caption="I made this 60-second launch video for my AI tutor, built from real screens of the course website.",
    ),
    "portfolio-video": dict(
        src="/media/portfolio-video.mp4", poster="/media/portfolio-video.jpg", ratio="16 / 9",
        title="Designing learning that works · portfolio video",
        caption="A 96-second introduction to my work. Scripted by me, with motion graphics coded in React with Remotion, an AI voice and an original piano score.",
    ),
    "community-esl": dict(
        youtube="BVk-sMserNs", poster="/media/community-esl.jpg", ratio="16 / 9",
        title="Jimmy and Rosalynn Carter Foundation Award (Finalist)",
        caption="I made every part of this video for The Community ESL Project (Portland State University, 2009). I met the students in the project, wrote the scripts and interviewed people, then directed, filmed, recorded the sound, edited and rendered it.",
    ),
}

PROJECTS = [
# ---------------------------------------------------------------- 1
dict(
  slug="two-country-course", art="exchange-flags", cats=["courses", "teaching"], logos=[("/media/two-country/miyazaki.webp", "Miyazaki International University logo"), ("/media/two-country/york-county.webp", "York County Community College seal")],
  tag="Interdisciplinary · Virtual exchange",
  title="A shared first-year course across two countries",
  summary="I developed a COIL course that linked political science students in Japan with sociology students in Maine, and I wrote its website.",
  hook="I developed a COIL course that linked political science students in Japan with sociology students in Maine, and I wrote its website.",
  skills={"core": ["Curriculum development and delivery", "Intercultural course design across two countries", "Active and applied learning", "Co-teaching across two institutions"]},
  facts=dict(
    context="First-year students in two countries studied the same public issues from two disciplines.",
    audience="Political science students at Miyazaki International College (Japan). Sociology students at York County Technical College (USA).",
    role="I co-designed the COIL (collaborative online international learning) course. I wrote the course website and taught students to code. I team-taught with Dr. Kiyohiko Toyama (political science) and Dr. Cindy Lahar (sociology).",
    tools=["HTML and CSS: a hand-coded shared course website"],
  ),
  sections=[
    ("The purpose", [
      "<p>The political science students at Miyazaki International College (now Miyazaki International University) were not familiar with American culture of the Northeast, while the sociology students at York County Technical College (now York County Community College) were largely unfamiliar with Japanese culture at large. These differences created a natural foundation for cross-cultural exchange and gave students from both disciplines a meaningful reason to collaborate, learn from one another, and explore social and political issues from different cultural perspectives.</p>",
    ]),
    ("The approach", [
      "<p>Both classes shared one website. Students researched political and social issues together. They chatted weekly (socially), discussed course content in writing, and presented their findings in written, spoken and video formats.</p>",
      '<div class="callout"><b>Why it matters today</b>This approach is now called virtual exchange, or COIL (Collaborative Online International Learning).</div>',
    ]),
    ("The team", [
      "<p>I co-taught with Dr. Kiyohiko Toyama (political science) and Dr. Cindy Lahar (sociology, Maine).</p>",
    ]),
    ("The outcome", [
      "<p>The course led to a peer-reviewed paper and two conference papers:</p>",
      '<p class="note">Maggard, J. (2002). Computer-mediated communication and political science: A collaborative learning approach. <cite>Comparative Culture</cite>, 8, 119–129.</p>',
      '<p class="note">Interlanguage development through collaborative learning with CMC. Paper presented at the Integrating Content and Language: Meeting the Challenge of a Multilingual Higher Education Conference, Universiteit Maastricht, Netherlands, October 2003.</p>',
      '<p class="note">Creating iMovie documentaries instead of term papers. Paper presented (with Elizabeth Lokon) at the TESOL International Convention, Long Beach, USA, April 2004.</p>',
    ]),
  ],
),
# ---------------------------------------------------------------- 1b
dict(
  slug="moderation-hub", art="moderation", cats=["courses"], shots=[("/media/moderation/control-room.webp", "A simplified view of the Control Room: the course lead fills in the course, exam, samples and opening and closing dates. Everything else runs automatically.", "The Control Room: where the course lead sets up each session"), ("/media/moderation/scoring-form.webp", "A simplified view of the scoring form: lecturers read the prompt and rubric, open each sample and choose a mark for each criterion.", "The scoring form lecturers fill in"), ("/media/moderation/feedback-email.webp", "A simplified feedback email: the lecturer's marks sit directly above the key marks, and a mark more than 0.5 apart is highlighted in yellow.", "The feedback email each lecturer receives")],
  tag="Instructional design · Microsoft 365 and Rise 360",
  title="Embedded Calibrated Grading and Automated Writing Moderation System",
  summary="I built a Microsoft 365 system that automates writing moderation (grading calibration) for exams, with a Rise 360 orientation for lecturers.",
  hook="I built a Microsoft 365 system that automates writing moderation (grading calibration) for exams, with a Rise 360 orientation for lecturers.",
  skills={"core": ["Grading, norming and exam development", "Assessment design and learning outcomes", "Formative assessment and feedback", "Accreditation and program improvement", "Faculty mentoring and stakeholder engagement"], "ai": ["Quality assurance and workflow design", "AI-assisted design and build with Claude, with documented human review"]},
  facts=dict(
    context="Writing moderation (grading calibration) for four English foundation courses at a university foundation program.",
    audience="Lecturers and course leads in a university foundation program.",
    role="Instructional designer and developer: needs analysis, design, build, testing and documentation.",
    tools=["Microsoft Forms", "Excel", "Power Automate", "SharePoint", "Office Scripts", "Articulate Rise 360", "SCORM 2004", "Blackboard Ultra"],
  ),
  sections=[
    ("The purpose", [
      "<p>At every midterm and final exam, lecturers mark writing samples in a moderation session, so that grading is consistent and fair. Each course used to have a co-course lead who ran these sessions. When that role was removed, the work fell on the course leads, or on a faculty member they assigned.</p>",
      "<p>Done by hand, it takes about 20 hours per course lead each semester: sending emails, collecting scores, analyzing them, sending feedback to every lecturer and keeping records. I built this system to do all of that automatically.</p>",
      "<p>Every session is archived, so the department builds a record of marking accuracy over time. That evidence supports data-driven review: we can see where calibration drifts, target training where it is needed, and reflect on and improve our assessment practice.</p>",
    ]),
    ("What the course lead does", [
      '<ol class="steps"><li>Open the Control Room (an Excel workbook on SharePoint) and choose the midterm or final exam.</li><li>Upload three anonymized samples of student writing to SharePoint.</li><li>Set the opening and closing dates in the Control Room.</li></ol>',
      "<p>That is the whole setup. Everything else runs on its own.</p>",
    ]),
    ("What happens automatically", [
      '<ol class="steps"><li>Power Automate emails every lecturer when the session opens.</li><li>Lecturers score the samples in one Microsoft Form, and Power Automate saves each score to the Excel workbook.</li><li>When the session closes, Excel with Office Scripts compares each score with the key mark. The course lead chooses the key mark: their own scores, or the median of the lecturers who marked the sample.</li><li>Power Automate sends each lecturer one email showing their mark for each rubric criterion directly above the key mark.</li><li>A lecturer more than 0.5 from the key mark marks another sample and gets instant feedback. For example, if the median is 3 and a lecturer gives a 4 or a 2, they mark another sample. They get up to two extra samples.</li><li>If they are still out of range, Power Automate emails the course lead, so they can meet and help.</li><li>SharePoint archives all the data, and the course leads receive a report. A name-free summary can go to the department for CEA accreditation.</li></ol>',
    ]),
    ("Why it matters", [
      '<ul class="points"><li>Saves each course lead about 20 hours a semester.</li><li>Frees the faculty member who was assigned to run moderation for other work that builds the program.</li><li>Shows course leads which lecturers need support, so they can help them early.</li><li>Provides documented evidence of assessment quality for CEA accreditation.</li></ul>',
    ]),
    ("Orientation", [
      "<p>I made a 5-minute Rise 360 orientation for lecturers, published as SCORM 2004 in Blackboard Ultra.</p>",
    ]),
    ("Next steps", [
      "<p>Built and tested with invented data in November 2026. With permission from the department, I will pilot it in Spring 2027 with the Embedded Foundation courses. If it works well, it can expand to the Foundation Program and Post-Foundation courses, so all three divisions of the department can use it.</p>",
    ]),
  ],
),
# ---------------------------------------------------------------- 2
dict(
  slug="english-21st-century", art="book", cats=["courses"], hero_block='<div class="cover-pair"><figure class="cover"><img src="/media/c21-cover-doha.webp" alt="Cover of English for the 21st Century, Course Book, B1+ Intermediate, Special Edition, with the Doha skyline, published by Garnet Education" loading="lazy" width="453" height="593"></figure><figure class="cover"><img src="/media/c21-cover.webp" alt="Cover of English for the 21st Century, Course Book, B1+ Intermediate, Special Edition, with trees and a garden, published by Garnet Education" loading="lazy" width="682" height="886"></figure><p class="cover-cap"><cite>English for the 21st Century</cite> (C21), Course Book, B1+ Intermediate, Special Edition. Garnet Education.</p></div>',
  tag="Garnet Education · CEFR B1+",
  title="English for the 21st Century",
  summary="I co-created a B1+ English course. I am the designated faculty textbook editor for the 3rd edition (2026) of its Garnet Education textbook.",
  hook="A B1+ English course I co-created, and its Garnet Education textbook. Designated faculty textbook editor for the 3rd edition (2026).",
  skills={"core": ["Curriculum development and delivery", "Assessment design and learning outcomes", "TESOL instruction at CEFR B1+", "Piloting a new course", "Textbook review and editing with a publisher"]},
  facts=dict(
    context="Learners at CEFR B1+ needed a course and a textbook matched to their level.",
    audience="English learners at CEFR B1+.",
    role="Co-creator of the B1+ English course. Designated faculty textbook editor for the 3rd edition (2026) of its Garnet Education textbook.",
    tools=[],
  ),
  sections=[
    ("The purpose", [
      "<p>Qatar University's Foundation Program needed an English course and a textbook matched to its students' CEFR B1+ level.</p>",
    ]),
    ("My role", [
      '<ul class="points"><li>Co-creator of the B1+ English course syllabus and assessments (2019).</li><li>Piloted the course (2019).</li><li>Faculty reviewer of the Garnet Education textbook, <cite>English for the 21st Century B1+</cite> (1st and 2nd editions).</li><li>Designated faculty textbook editor for the 3rd edition (2026).</li></ul>',
      '<figure class="photo wide-photo"><img src="/media/doha-skyline.webp" alt="The Doha skyline at night, reflected in the water" loading="lazy"><figcaption>Doha, Qatar, where the course was created.</figcaption></figure>',
    ]),
  ],
),
# ---------------------------------------------------------------- 3
dict(
  slug="falcon-folktale", art="animation", cats=["video", "cultural"], hero="/media/falcon/mohammed-hurr.webp",
  tag="Animation · Museum partnership",
  title="He Who Doesn’t Know the Falcon Roasts It",
  summary="A Qatari folktale I collected and edited. It appears in a National Museum of Qatar exhibition book. Now I am animating it.",
  hook="From a folktale told in Qatar, to a museum exhibition, to my own animated series.",
  video="falcon-opening",
  skills={"core": ["Collecting oral folktales with students", "Bilingual editing", "Partnership with the National Museum of Qatar", "Faculty mentoring and stakeholder engagement"], "ai": ["AI-assisted video and animation production", "Story adaptation and scriptwriting", "Prompt engineering and scene direction", "Character design and visual consistency", "AI voice casting and direction", "Art direction and visual style guides", "Cultural authenticity in AI-generated media", "AI production planning and budgeting", "Quality assurance and workflow design", "AI agent direction and orchestration"]},
  facts=dict(
    context="A Qatari folktale about compassion and forgiveness, ready for a new audience.",
    audience="Museum visitors, families and young viewers on YouTube.",
    role="Managing Editor of Tales of Qatari Heritage, the book this story comes from. As Chair of the Cultural Awareness Team, I led the students and faculty who collected it and built the partnership with the National Museum of Qatar. Writer, art director and producer of the animated series.",
    tools=["Claude", "Claude Code", "Higgsfield", "AI voice", "Lip sync", "ffmpeg", "Excel", "Google Drive", "GitHub"],
  ),
  sections=[
    ("The purpose", [
      "<p>To keep a Qatari folktale alive and share its lesson with new audiences: first in a book, then in a museum exhibition, and now as an animated film.</p>",
    ]),
    ("The story", [
      "<p>“He Who Doesn’t Know the Falcon Roasts It” is one of the 19 stories in <cite>Tales of Qatari Heritage</cite>, the bilingual book I lead as Managing Editor. Qatar University students on my Cultural Awareness Team collected it from their elders, and I edited it.</p>",
      "<p>It concludes Lila Abu-Lughod’s opening chapter in <cite>On the Move: Reframing Nomadic Pastoralism</cite> (Doha: Qatar Museums; [Milan]: Skira, 2022). The National Museum of Qatar featured the story in its On the Move exhibition (Fall 2022 – Winter 2023). The book acknowledges me and my Qatar University faculty editorial team.</p>",
      '<figure class="cover"><img src="/media/on-the-move-cover.webp" alt="Cover of On the Move: Reframing Nomadic Pastoralism, published by Qatar Museums and Skira" loading="lazy"><figcaption><cite>On the Move: Reframing Nomadic Pastoralism</cite> (Qatar Museums and Skira, 2022). My story concludes the opening chapter.</figcaption></figure>',
    ]),
    ("From story to screen", [
      '<div class="reel-3d hero3d-band story-reel" data-scene="animation">@@CANVAS@@<span class="reel-3d-label"><span class="label">Animation</span><b>From story to screen</b><span>Storyboards, a locked Character Guide and AI animation for my folktale series.</span></span></div>',
      "<p>I am writing and producing an animated series of folktales from Qatar, UAE, Mongolia, and Japan. Below you can see how I approach the design elements and characters.</p>",
      '<ul class="points"><li><b>Look:</b> 2D animation, Pixar-inspired. Clean shapes, expressive faces and cinematic light.</li><li><b>Setting:</b> an authentic Qatari desert and culture.</li><li><b>Rules:</b> a written style guide, cast guide, cultural-accuracy rules and a QA checklist for every scene.</li><li><b>Sound:</b> story subtitles, voice and lip sync, and an original music theme.</li></ul>',
    ]),
    ("Character Guide", [
      "<p>Each character has a locked face, outfit and turnaround, so every scene stays consistent.</p>",
      "@gallery:cast",
    ]),
    ("Art direction and asset library", [
      "<p>A locked art-direction board sets the look, palette, locations and props for the whole series.</p>",
      "@gallery:art",
    ]),
    ("Storyboards and layout", [
      "<p>Each scene starts as a layout plan and a rough draft before it is animated.</p>",
      "@gallery:storyboard",
    ]),
    ("Promotion", [
      "<p>I also design the launch materials: a 4K thumbnail and a LinkedIn carousel.</p>",
      "@gallery:promo",
    ]),
  ],
  status="Episode 1 in production.",
),
# ---------------------------------------------------------------- 4
dict(
  slug="kamishibai", art="kamishibai", cats=["cultural"], hero="/media/kamishibai/snow-run.webp",
  tag="UNESCO-funded",
  title="UNESCO Mongolia Kamishibai Program",
  summary="As Principal Investigator, I wrote the UNESCO grant, built the team, led students to Mongolia to train university students and faculty in kamishibai, and co-produced the program DVD.",
  hook="As Principal Investigator, I wrote the UNESCO grant, built the team, led students to Mongolia to train university students and faculty in kamishibai, and co-produced the program DVD.",
  skills={"core": ["Grant writing and serving as Principal Investigator", "Building and leading an international team", "Budget and program management", "Research design and data collection", "Faculty mentoring and teacher training"]},
  facts=dict(
    context="A two-year, $30,000 UNESCO/Japan Funds-in-Trust grant at Akita International University (2005–2006).",
    audience="University students and faculty, plus K-12 students in Mongolia and Japan.",
    role="Principal Investigator and Steering Committee Chair. Director of the documentary team.",
    tools=["iMovie", "PowerPoint", "iDVD", "Multi-disc DVD burner"],
  ),
  sections=[
    ("The purpose", [
      "<p>To preserve folktales from Mongolia and Japan and share them across both countries, by training university students to collect the stories and perform them as kamishibai for K-12 students.</p>",
    ]),
    ("How it started", [
      "<p>I wrote the grant and served as Principal Investigator. I built a team around the project. One team member, a former Vice President of the Asian Development Bank, helped the proposal win funding from UNESCO through the Asia/Pacific Cultural Centre for UNESCO (ACCU).</p>",
    ]),
    ("The program", [
      "<p>More than 40 faculty and students took part at Akita International University and the University of the Humanities (Ulaanbaatar) to teach folklore and kamishibai theatre traditions to hundreds of K-12 students in Mongolia and Japan.</p>",
      "<p>Kamishibai is a Japanese storytelling tradition in which a performer presents a sequence of illustrated paper panels on a small stage, sliding each scene across the frame in rhythm with the narration. The storyteller uses expressive vocal techniques, gestures, timing, and character voices reminiscent of traditional Japanese theatrical performance. In many ways, manga can be seen as its modern analogue: both rely on sequential images, visual pacing, and the interaction between images and narrative to tell a story.</p>",
    ]),
    ("My role", [
      '<ul class="points"><li>Wrote the UNESCO grant and served as Principal Investigator and Steering Committee Chair.</li><li>Planned the pre-departure and in-country program and managed the budget.</li><li>Led the student team to Mongolia and trained University of the Humanities students and faculty in kamishibai methods.</li><li>Designed the research program and its data collection tools.</li><li>Directed the documentary team.</li><li>Co-produced and self-published the <em>UNESCO Mongolia Kamishibai Program</em> DVD with Chris Hoskins. It was distributed widely to schools in Japan and Mongolia, and to universities.</li></ul>',
      "<p>The DVD holds the Japanese and Mongolian kamishibai stories as PowerPoint slideshows. It has videos on collecting the folktales from oral tellers. It also has a PPT with instructions on how to create kamishibai illustrations, and how to use traditional voice-acting methods.</p>",
      '<figure class="photo photo-half"><img src="/media/kamishibai/dvd-landing.webp" alt="DVD landing screen: Akita International University UNESCO/ACCU Kamishibai Project with Mongolia University of Humanities, with a strip of project photos and menu items for Slideshows, Movies, Presentations, Team Members, Japanese Kamishibai and Mongolian Kamishibai. Children&rsquo;s faces are blurred." loading="lazy" width="760" height="583"><figcaption>DVD landing screen</figcaption></figure>',
    ]),
    ("New artwork", [
      "<p>This is new artwork for the program’s Japanese stories. I am currently reproducing the stories as cartoon shorts. The new version will also become graded readers with a reading/writing curriculum.</p>",
      "@gallery:kamishibai",
    ]),
    ("The history of kamishibai", [
      "<p class=\"era-intro\">Kamishibai, or paper theater, has very old roots in the Heian period.</p>",
      '<div class="eras">',
      '<article class="era"><div class="era-body"><h3>Heian-era picture scrolls (794–1185)</h3><p>In Heian-era Kyoto, artists painted <i>emakimono</i>: illustrated handscrolls that joined text with pictures in sequence. The <cite>Tale of Genji</cite> scrolls are the best-known example. By the late Heian and Kamakura periods, Buddhist monks used picture scrolls to tell stories and moral lessons to people who could not read, pointing to each scene as they spoke.</p></div><figure class="era-media"><img src="/media/kamishibai/roots-emaki.webp" alt="Illustration of a Heian-era picture scroll: a palace scene with a court lady and a courtier beside columns of brush calligraphy" loading="lazy" width="1024" height="688"><figcaption>A Heian-style picture scroll. Original illustration.</figcaption></figure></article>',
      '<article class="era"><div class="era-body"><h3>Street kamishibai</h3><p>Storytellers rode bicycles from street to street (1930s–1950s) with a small wooden stage, the <i>butai</i>. They clapped wooden <i>hyoshigi</i> sticks to call children, then slid one picture card after another through the frame as they told the story.</p></div><figure class="era-media"><img src="/media/kamishibai/roots-stage.webp" alt="Illustration of a wooden kamishibai stage with open doors on a bicycle, with wooden hyoshigi clappers tied with a red and white cord" loading="lazy" width="1024" height="688"><figcaption>A wooden <i>butai</i> stage and <i>hyoshigi</i> clappers. Original illustration.</figcaption></figure></article>',
      '<article class="era"><div class="era-body"><h3>Kamishibai today</h3><p>Teachers and librarians still use kamishibai. The pairing of pictures and voice holds an audience and helps young learners follow a story in sequence. Our program brought this tradition to students in Mongolia and Japan.</p></div><figure class="era-media"><img src="/media/kamishibai/roots-performance.webp" alt="Illustration of a storyteller sliding a picture card through a wooden kamishibai stage while children raise their hands" loading="lazy" width="1024" height="688"><figcaption>A kamishibai performance in a classroom. Original illustration.</figcaption></figure></article>',
      '</div>',
    ]),
  ],
),
# ---------------------------------------------------------------- 5
dict(
  slug="pure-intellect", art="tutor", cats=["ai"],
  tag="AI apps · Claude Code",
  title="Pure Intellect Tutor, Analyzer &amp; AI Ranking App",
  summary="I create AI education tools: a tutor that asks students questions instead of giving answers, and a grading assistant for professors.",
  hook="I create AI education tools: a tutor that asks students questions instead of giving answers, and a grading assistant for professors.",
  video="pure-intellect-tutor",
  skills={"core": ["Curriculum development and delivery", "Formative assessment and feedback", "Assessment design and rubrics", "Accessibility: WCAG 2.2 AA, for Deaf and hard-of-hearing students"], "ai": ["AI literacy and critical thinking in education", "AI-assisted web development with Claude Code", "Ethical AI policy, with no AI detection", "Quality assurance and workflow design"]},
  facts=dict(
    context="Students can ask AI to do the work for them. I wanted AI that makes them think harder instead.",
    audience="First-year university students and their professors.",
    role="Designer and developer.",
    tools=["Claude", "Claude Code", "React", "TypeScript", "Vite", "Three.js", "Vitest", "Playwright"],
  ),
  sections=[
    ("The purpose", [
      "<p>Students can ask AI to do their work for them. I wanted AI that makes them think harder instead.</p>",
    ]),
    ("Pure Intellect Tutor", [
      "<p>The tutor is a Socratic coach. It asks one question at a time and never writes the answer.</p>",
      '<ul class="points"><li>Replies stay under 60 words.</li><li>Students get at most three hints per step.</li><li>A code-level guard turns any finished-work reply into a question.</li></ul>',
    ]),
    ("Pure Intellect Analyzer", [
      "<p>The Analyzer is for professors only. It suggests a rubric level for each criterion and quotes the student’s own words as evidence. The professor accepts or changes every level.</p>",
      '<ul class="points"><li>Feedback the professor chooses: a strength, a “try this” and one question back.</li><li>An AI-use check against the course policy. It never guesses whether text was written by AI.</li><li>One optional revision, where the higher score counts.</li><li>A gradebook with Excel and CSV export.</li></ul>',
    ]),
    ("AI Ranking App", [
      "<p>The project began as the AI Use Rating App: a voluntary “show your work” portal that coaches how people think while they use AI. It uses no AI detection and no keystroke tracking.</p>",
    ]),
    ("Design principles", [
      '<ul class="points"><li>Accessibility first: WCAG 2.2 AA, designed for Deaf and hard-of-hearing students.</li><li>No timers and no leaderboards.</li><li>Student data stays on the student’s device.</li></ul>',
    ]),
    ("Quality", [
      "<p>48 automated tests, plus a scripted click-through on desktop and phone. Screens below use invented sample students.</p>",
      '@gallery:pi-app',
    ]),
  ],
),
# ---------------------------------------------------------------- 14
dict(
  slug="motion-videos", art="motion", cats=["video", "ai"],
  tag="Motion graphics · Launch videos",
  title="Launch and promo videos",
  summary="I script and build launch and promo videos in code with React and Remotion, with an AI voice and original music.",
  hook="I script and build launch and promo videos in code with React and Remotion, with an AI voice and original music.",
  video="pure-intellect-tutor",
  skills={"core": ["Scriptwriting", "Visual storytelling", "Captions for every video"], "ai": ["AI voice casting and direction", "AI-assisted video production", "AI-assisted coding with Claude Code"]},
  facts=dict(
    context="Products and courses need short videos that explain them fast.",
    audience="Faculty, hiring teams and LinkedIn viewers.",
    role="Scriptwriter, designer and producer.",
    tools=["React", "Remotion", "AI voice", "ffmpeg", "Claude Code"],
  ),
  sections=[
    ("The purpose", [
      "<p>Products and courses need short videos that explain them fast.</p>",
    ]),
    ("What I make", [
      '<ul class="points"><li>Product launch videos, such as the Pure Intellect Tutor video.</li><li>Course website walkthroughs, captioned to work with no sound.</li><li>Portfolio and introduction videos.</li><li>Formats for every channel: 16:9, 9:16, 1:1 and 4:5 for LinkedIn.</li></ul>',
    ]),
    ("How I build them", [
      "<p>Every frame is coded in React with Remotion. Captions and graphics are timed to the measured voice track. The music bed is an original piano score. I write every script.</p>",
      "@video:portfolio-video",
    ]),
  ],
),
# ---------------------------------------------------------------- 7
dict(
  slug="ai-humanities-course", art="course-map", cats=["courses", "ai"], hidden=True,  # hidden 8 Nov 2026 at Jeffrey's request; delete hidden=True to restore
  tag="Course concept · AI literacy",
  title="Technology and Society: AI and the Humanities",
  summary="A complete 15-week first-year course concept: 45 sessions, Bloom’s-sequenced activities and an AI tutor.",
  hook="A full first-year course where students use AI to think harder, not less.",
  facts=dict(
    context="A sample course concept I designed for a first-year technology and society program.",
    audience="First-year university students across majors, including Deaf and hard-of-hearing students.",
    role="Course designer and developer of the course website and tutor.",
    tools=["Backward design", "Bloom’s taxonomy", "UDL", "Rubrics", "Brightspace cartridge", "Claude Code"],
  ),
  sections=[
    ("Scope", [
      '<ul class="points"><li>15 weeks in 5 three-week units.</li><li>45 sessions of 50 minutes, each planned to the minute.</li><li>26 readings and 15 weekly thinking logs.</li><li>6 signature activities, 9 studio activities and a final decision brief.</li></ul>',
    ]),
    ("Units", [
      '<ol class="steps"><li>New technology, old fears.</li><li>What AI is and how to check it.</li><li>Who benefits, pays and decides.</li><li>Whose world AI builds.</li><li>How we should decide.</li></ol>',
    ]),
    ("Activity design", [
      "<p>Every activity has five steps, sequenced with Bloom’s taxonomy. Students can respond in writing, ASL or a sketch. Each activity offers lenses for eight majors.</p>",
      "<p>Each activity sets one of four AI modes: Plan only, Co-draft, Directed or Open. Every graded piece carries an AI record. There are no AI detectors.</p>",
    ]),
    ("Grading", [
      '<ul class="points"><li>Signature activities: 60%.</li><li>Final decision brief: 25%.</li><li>Weekly thinking logs: 15%, graded for completion, never for grammar or length.</li></ul>',
    ]),
    ("Deliverables", [
      '<ul class="points"><li>A 31-page course packet and 32 pages of lesson plans.</li><li>A syllabus, scope and sequence, rubrics, reading list and instructor guide.</li><li>A course website with the Pure Intellect Tutor.</li><li>A course cartridge for Brightspace with 16 modules and 81 pages.</li></ul>',
    ]),
    ("The course website", [
      "<p>Students reach every week, activity and the tutor from one course website. Sample students and work are invented.</p>",
      "@gallery:course-site",
    ]),
    ("Measuring success", [
      "<p>The course has not been taught yet. In a live course, success would show in the thinking logs, the rubric scores on each signature activity and the quality of the final decision briefs.</p>",
    ]),
  ],
  status="Sample course concept. Not affiliated with or endorsed by any university.",
),
# ---------------------------------------------------------------- 10
dict(
  slug="story-mile", art="story-mile", cats=["cultural"], hero="/media/story-mile/artwork.webp",
  tag="Zayed University · Public exhibition",
  title="The Story Mile",
  summary="I co-founded a student storytelling club and led its stories to a public exhibition on the Abu Dhabi Corniche, a permanent installation and a book I edited.",
  hook="I co-founded a student storytelling club and led its stories to a public exhibition on the Abu Dhabi Corniche, a permanent installation and a book I edited.",
  skills={"core": ["Founding and supervising a student club", "Partnerships with cultural and corporate sponsors", "Exhibition planning on a public site", "Editing a book of 40 student stories", "Active and applied learning"]},
  facts=dict(
    context="A storytelling project at Zayed University, made with major cultural partners.",
    audience="Zayed University students and the public in Abu Dhabi.",
    role="Co-founder and a faculty supervisor of the Al Kharareef storytelling club. Co-creator of the Story Mile Project. Editor of the book.",
    tools=[],
  ),
  sections=[
    ("The purpose", [
      "<p>To preserve Emirati oral traditions and give students a public audience for their writing.</p>",
    ]),
    ("The project", [
      "<p>I co-founded the Al Kharareef storytelling club at Zayed University in 2011 and was a faculty supervisor.</p><p>In 2013, I invited the world-famous master storyteller Abdul Aziz Al Musallam, head of the Sharjah Institute for Heritage, to Zayed University. He helped participating faculty &amp; students craft their stories the way they were meant to be told.</p><p>I co-created the Story Mile Project with Mubadala, the Sharjah Institute for Heritage and the Abu Dhabi Music &amp; Arts Festival. Forty stories were initially exhibited as part of the festival in 2013. Then they became a permanent exhibition at Khalifa Park and <cite>The Story Mile</cite> book was published in 2014.</p>",
      '<figure class="photo banner"><img src="/media/story-mile/al-kharareef.webp" alt="Al Kharareef Storytelling Club banner: a storyteller with a falcon and children around a campfire" loading="lazy" width="1000" height="250"><figcaption>The banner from the Al Kharareef Storytelling Club website.</figcaption></figure>',
      '<figure class="cover"><img src="/media/story-mile/story-illustration.webp" alt="Story illustration: a girl in a yellow dress with red dots beside an old stone archway" loading="lazy" width="441" height="414"><figcaption>A story illustration from the project.</figcaption></figure>',
    ]),
    ("On the Corniche", [
      "<p><cite>The Story Mile: A Journey Through Emirati Oral Traditions</cite> opened on the Abu Dhabi Corniche as part of the 10th Abu Dhabi Festival, 10–29 March 2013. Admission was free.</p>",
      "<p>Lightboxes along the seafront path showed the stories by Zayed University students and the Al Kharareef Club. Some were passed down through generations. Others were new stories that students adapted or combined.</p>",
      '<figure class="photo photo-half"><img src="/media/story-mile/lightbox-half.webp" alt="A Story Mile lightbox on the Abu Dhabi Corniche showing the story Killing Men Softly, with people walking along the seafront path" loading="lazy" width="760" height="507"><figcaption>The Story Mile exhibition on the Abu Dhabi Corniche, March 2013. These stories later became the book <cite>The Story Mile</cite>. Photo: <cite>The National</cite>.</figcaption></figure>',
      '<figure class="cover flyer"><img src="/media/story-mile/e-flyer.webp" alt="Abu Dhabi Festival e-flyer for The Story Mile on Abu Dhabi Corniche, 10 to 29 March 2013, showing characters from Emirati folktales on the Corniche" loading="lazy" width="1000" height="1419"><figcaption>The Abu Dhabi Festival e-flyer for The Story Mile, 2013.</figcaption></figure>',
      '<h3 class="subhead">World Storytelling Day</h3>',
      "<p>The Al Kharareef Club also took part in a number of events, including the World Storytelling Day event in Abu Dhabi on 20 March 2013. Club members told stories to visiting schoolchildren at Abu Dhabi Heritage Village. Children&rsquo;s faces are blurred for their privacy.</p>",
      "@gallery:storytelling-day",
      '<h3 class="subhead">School visits</h3>',
      "<p>The Kharareef Club also did a number of school visits to hold storytelling events. One was at Mushrif School on 12 March 2013.</p>",
    ]),
    ("The outcome", [
      '<ul class="points"><li>300 student authors took part.</li><li>A public exhibition on the Abu Dhabi Corniche.</li><li>A permanent installation at Khalifa Park.</li><li>The book <cite>The Story Mile</cite> (ISBN 978-9948-20-117-5), which I edited.</li></ul>',
    ]),
  ],
),
# ---------------------------------------------------------------- 11
dict(
  slug="tales-of-qatari-heritage", art="tales", cats=["cultural"], showcase_feature="tales-feature", no_toc=True, banner="/media/tales/falcon-strip.webp", banner_alt="Student artwork in five panels: a falconer among tents and camels, a man cradling a bird, a man shading his eyes in the desert, a man running toward a fallen falcon, and a falconer with his falcon.", banner_caption="He Who Doesn’t Know the Falcon Roasts It",
  tag="Bilingual book · Qatar University",
  title="Tales of Qatari Heritage",
  summary="I am lead editor of a bilingual book of Qatari folktales, leading six co-editors and more than 150 students, faculty and staff.",
  hook="I am lead editor of a bilingual book of Qatari folktales, leading six co-editors and more than 150 students, faculty and staff.",
  skills={"core": ["Leading more than 150 students, faculty and staff", "Training students to collect stories from elders", "Bilingual editing with six co-editors", "Faculty mentoring and stakeholder engagement", "Active and applied learning"]},
  facts=dict(
    context="Qatari folktales that show compassion and forgiveness.",
    audience="Readers of Arabic and English.",
    role="Lead editor, working with six co-editors. Chair of the Cultural Awareness Team (2016–2023).",
    tools=[],
  ),
  sections=[
    ("The purpose", [
      "<p>To preserve and share Qatar’s folktales, fables and legends, and to give students a way to serve their community.</p>",
    ]),
    ("The book", [
      "<p><cite>Tales of Qatari Heritage</cite> is an unpublished bilingual (Arabic/English) book of Qatari folktales collected by Qatar University students. Most stories show compassion and forgiveness.</p>",
    ]),
    ("My role", [
      "<p>I am lead editor, working with six co-editors. As Chair of the Cultural Awareness Team (2016–2023), I led more than 150 students, faculty and staff on the project.</p>",
    ]),
    ("The stories", [
      '<div class="toc-wrap"><table class="toc-table"><thead><tr><th scope="col">English</th><th scope="col" lang="ar" dir="rtl">العربية</th></tr></thead><tbody><tr><td>Muneera: The Sheikh’s Daughter</td><td lang="ar" dir="rtl">منيرة بنت الشيخ</td></tr><tr><td>The Song of the Warrior</td><td lang="ar" dir="rtl">عزوة الفارس</td></tr><tr><td>He Who Doesn’t Know the Falcon Roasts It</td><td lang="ar" dir="rtl">اللي ما يعرف الصقر يشويه</td></tr><tr><td>Entertaining the Guest</td><td lang="ar" dir="rtl">إكرام الضيف</td></tr><tr><td>Gheelan: The Kind Sailor</td><td lang="ar" dir="rtl">البحار الطيب غيلان</td></tr><tr><td>The Gracious Forgiveness</td><td lang="ar" dir="rtl">الصفح الجميل</td></tr><tr><td>You Reap What You Sow</td><td lang="ar" dir="rtl">جنت على نفسها براقش</td></tr><tr><td>The Solemn Promise</td><td lang="ar" dir="rtl">حكاية عهد</td></tr><tr><td>A Tale of Generosity</td><td lang="ar" dir="rtl">قصة الكرم</td></tr><tr><td>The Noble Knight</td><td lang="ar" dir="rtl">الفارس النبيل</td></tr><tr><td>Allawi and Hmaarat Al Qayla</td><td lang="ar" dir="rtl">علاوي وحمارة القايلة</td></tr><tr><td>Afra and the Wolf</td><td lang="ar" dir="rtl">عفرة والذئب</td></tr><tr><td>The Broken Promise</td><td lang="ar" dir="rtl">النكث بالعهد</td></tr><tr><td>Um Elheilan</td><td lang="ar" dir="rtl">أم الهيلان</td></tr><tr><td>Nteef Nteefan: A Morsel or Two</td><td lang="ar" dir="rtl">نتيف نتيفان</td></tr><tr><td>Can’t Catch a Break</td><td lang="ar" dir="rtl">المتعوس متعوس</td></tr><tr><td>Strength in Forgiveness</td><td lang="ar" dir="rtl">العفو عند المقدرة</td></tr><tr><td>The Donkey’s Tail</td><td lang="ar" dir="rtl">ذيل الحمار</td></tr><tr><td>The Price of Greed</td><td lang="ar" dir="rtl">ثمن الطمع</td></tr></tbody></table></div>',
    ]),
  ],
),
# ---------------------------------------------------------------- 12
dict(
  slug="peace-studies-seminar", art="seminar", cats=["cultural", "teaching"], hero="/media/peace/bayon.webp", hero_class="hero-short", hero_alt="A giant carved stone face at Bayon temple, Angkor.",
  tag="Miyazaki · Fall 2003",
  title="Peace Studies Seminar on Cambodia",
  summary="I co-created a 15-week seminar on Cambodia for more than 200 students and community members, and led a student study trip to Phnom Penh and Siem Reap.",
  hook="I founded the Peace Studies Club, led its campaign for an anti-trafficking NGO in Cambodia, co-created a seminar on Cambodia, and took the students to meet the NGO and the people they supported.",
  skills={"core": ["Organizing a seminar end to end: embassies, NGOs, 11 faculty and visiting speakers", "Partnering with an anti-trafficking NGO in Cambodia", "Leading a student study trip abroad", "Fundraising with four student clubs", "Service learning and community engagement"]},
  facts=dict(
    context="A 15-week, certificate-bearing seminar at Miyazaki (Fall 2003).",
    audience="More than 200 students and community members.",
    role="Founded the Peace Studies Club and served as its faculty advisor. Co-created the seminar. Led the student trip to Phnom Penh and Siem Reap. Helped raise more than $3,000 for an NGO.",
    tools=[],
  ),
  sections=[
    ("The purpose of the seminar", [
      '<p>To teach peace studies and conflict resolution to Miyazaki International University students and members of the local Miyazaki community.</p>',
    ]),
    ("Lead-up to the seminar", [
      '<p>In January 2003, I visited Siem Reap and met a man who worked with the Vulnerable Children’s Assistance Organization (VCAO), a UNHCR program that stops children from being sold into slavery and prostitution. This is what VCAO does:</p>',
      '<div class="story-cards"><article><p class="label">The problem VCAO fights</p><h3>A $100 promise</h3><p>Traffickers offer poor families about $100 and a factory job for a child, then sell the child. The parents are tricked; they don’t realize what is happening.</p></article><article><p class="label">VCAO prevention</p><h3>Village workshops</h3><p>In two-day conflict resolution workshops, children and adults learn to identify their problems and plan solutions. Most problems trace back to poverty. The solution: move children at risk to a safe house, out of the traffickers’ reach.</p></article><article><p class="label">VCAO protection</p><h3>A guarded safe house</h3><p>Eleven girls lived in his family home under armed guard, safe from traffickers.</p></article></div>',
      "<p><b>Life at the safe house in Siem Reap.</b> Krama are long silk scarves; VCAO sells them to fund its work.</p>",
      '<figure class="safe-house"><a href="/media/peace/safe-house.webp" target="_blank" rel="noopener"><img src="/media/peace/safe-house.webp" alt="Collage of eleven panels from the VCAO safe house: an armed guard in front of a wooden house on stilts; girls weaving at wooden looms; two finished silk krama scarves; a girl tending vegetables; a girl feeding a pig beside chickens; girls reading at a table; three girls wearing checked krama. All faces are blurred." loading="lazy" width="1536" height="1024"></a><figcaption><b>Top row:</b> the guard and the house on stilts, girls weaving at the looms, and finished silk krama. <b>Bottom row:</b> more weaving, growing vegetables, raising pigs and chickens, a reading lesson, and girls wearing their krama. Illustration; faces blurred for privacy.</figcaption></figure>',
    ]),
    ("The role of the Peace Studies Club", [
      "<p>In March 2003, in Miyazaki, I founded the Peace Studies Club with a student who hoped to become an NGO worker. My colleague Dr. Kiyohiko Toyama encouraged me to start it before he left for Tokyo, newly elected to the House of Councillors, the upper house of Japan’s parliament.</p>",
      "<p>From the start of the school year, the club ran a campaign for VCAO, and the Drama, Music and Dance Clubs joined it. All the money raised went to VCAO:</p>",
      '<ol class="journey"><li><h3>Saturday markets</h3><p>I bought krama for $10 each, and the club sold them for $20 (¥2,000). Each sale doubled the money, which bought more krama. This went on for three years.</p></li><li><h3>A concert</h3><p>An evening concert in a concert hall, with ticket sales.</p></li><li><h3>A comedy show and play</h3><p>An evening show at the university, where we collected donations.</p></li><li><h3>Donation boxes</h3><p>Boxes in convenience and grocery stores across town.</p></li></ol>',
    ]),
    ("The seminar", [
      '<figure class="seminar-shot"><img src="/media/peace/seminar.webp" alt="Illustration of a lecture hall full of students, with a presenter beside a slide reading Peace Studies Seminar: Cambodia’s Path Forward, Miyazaki International College, 2003." loading="lazy" width="900" height="504"><figcaption>Illustration of the seminar.</figcaption></figure>',
      "<p>By June 2003, the campaign had built strong interest across Miyazaki. To build on it, I co-created the Peace Studies Seminar on Cambodia with Dr. Elizabeth Lokon. It ran for 15 weeks in the fall semester of 2003.</p>",
      "<p>Mr. Ok Veth, the Cambodian Ambassador’s Counsellor, opened the seminar. Sessions by 11 MIU faculty and guest speakers covered Cambodian history and the Khmer Rouge, Buddhism, anthropology and the economy. An NGO spoke on landmine removal, and staff from Japan’s embassy in Phnom Penh presented their Official Development Assistance (ODA) work.</p>",
      "<p>More than 200 students and community members from Miyazaki attended. Everyone who attended 12 or more sessions received a certificate.</p>",
      "<p>Dr. Toyama spoke at the closing session and thanked the students and the community for their work.</p>",
    ]),
    ("The Peace Studies Club trip", [
      "<p>In February 2004, I led the students to Cambodia. At VCAO headquarters in Phnom Penh, the Peace Studies Club gave VCAO more than $3,000, everything it had raised. The staff showed us their projects. In Siem Reap, the students met the girls they had been supporting, and we bought more krama to sell at home.</p>",
      '<div class="trip-essay"><div class="te te-meeting"><span class="te-chip">VCAO community workshop</span><img src="/media/peace/meeting.webp" alt="A community meeting in Cambodia under an open-sided metal roof, with rows of people on plastic chairs facing a table at the front." loading="lazy" width="951" height="804"></div><div class="te te-vcao"><img src="/media/peace/vcao-logo.webp" alt="Logo of the Vulnerable Children Assistance Organization: a family under an umbrella." loading="lazy" width="448" height="448"></div><div class="te te-street"><img src="/media/peace/street.webp" alt="A busy street in Cambodia with motorbikes and a schoolgirl crossing. Her face is blurred for privacy." loading="lazy" width="1208" height="906"><span class="te-chip">Cambodia</span></div><div class="te te-men"><img src="/media/peace/two-men.webp" alt="Two men standing on a sidewalk in Cambodia, one leaning on a crutch." loading="lazy" width="906" height="1208"></div><div class="te te-park"><img src="/media/peace/park.webp" alt="A sculpture of a pistol on a plinth in a Cambodian park, with a man in a bucket hat in the foreground." loading="lazy" width="1208" height="906"></div><div class="te te-logo"><img src="/media/peace/oda-logo.webp" alt="The Japan Official Development Assistance emblem on an aid vehicle." loading="lazy" width="598" height="646"></div><p class="te-note">Photos from the student trip. Children’s faces are blurred for privacy.</p></div>',
    ]),
    ("The impact", [
      '<ul class="points"><li>The girls stayed in the safe house and built their weaving skills. Once skilled, they took their looms home and kept weaving to support their families. The safe house still runs today.</li><li>More than 20 years later, the university still teaches peace and conflict studies: a 15-week course led by a political science professor.</li><li>Dr. Jeong-Pyo Hong’s seminar lecture, “Sino-Cambodian Relations: from the Chinese Perspective,” is listed among his publications in a 2004 Korea Institute for International Economic Policy report.</li></ul>',
      '<h3 class="sub-h">Student outcomes</h3>',
      '<ul class="points"><li>The student who co-founded the club became an NGO worker. She has worked in Cambodia, Thailand, Bangladesh, India and Laos.</li><li>In 2003, I trained club members to do research and co-wrote a paper with them, “Young Japanese people’s views on civic (dis)engagement.” I led them to Tokyo, where we presented it together at the 2nd Peace as a Global Language Conference. On the same trip, the students met Dr. Toyama at the National Diet Building. He was a sitting member of the upper house at the time. He praised their work and encouraged them to keep going.</li><li>In 2004, I led the students to Kyoto, where we presented our co-written research, “Developing social responsibility and IC skills,” at the 3rd Peace as a Global Language Conference.</li></ul>',
    ]),
  ],
),
# ---------------------------------------------------------------- 13
dict(
  slug="sociology-video-course", art="video-course", cats=["video", "teaching"],
  tag="Video lecture course · Miyazaki",
  title="Video lecture course in sociology",
  summary="I wrote, directed and produced a video lecture series for a blended sociology course, and built its website.",
  hook="A blended course built on a video series I wrote, directed and produced.",
  skills={"core": ["Blended course design", "Scriptwriting and directing", "Co-teaching with a sociologist", "Curriculum development and delivery"]},
  facts=dict(
    context="A blended sociology course at Miyazaki.",
    audience="University sociology students.",
    role="Writer, director and producer of the video series. Builder of the course website.",
    tools=["Tape video cameras, later digital cameras", "iMovie"],
  ),
  sections=[
    ("The purpose", [
      "<p>To teach sociology in English through a blended course, with video lectures students could watch in class and online.</p>",
    ]),
    ("The course", [
      "<p>I wrote, directed and produced the video series for a blended course taught with sociologist Dr. Hiroyuki Toyota.</p>",
      "<p>Students used the videos in class and online, alongside live lectures and a textbook. I built the course website.</p>",
    ]),
    ("The outcome", [
      "<p>The course led to a conference workshop:</p>",
      '<p class="note">Content-based sociology courses and CMC. Workshop (with Hiroyuki Toyota) at Thailand TESOL: Culture, Content and Competency, Bangkok, Thailand, January 2003.</p>',
    ]),
  ],
),
]

TEACHING = dict(
  intro="I have taught university writing, humanities and social science courses in Japan, the USA, the UAE and Qatar.",
  current="Lecturer, Foundation Program, Department of English, Qatar University (Feb. 2014 – present). Content-based courses in business, law and EFL for humanities, STEM, international affairs and mass communication students. About eight years of online and hybrid teaching.",
  areas=[
    ("Academic English", "Research writing, reading, grammar, communication, presentation and pronunciation. IELTS, TOEFL and TOEIC preparation."),
    ("Content-based courses", "Political science, sociology, teacher education, business, law, linguistics, TESOL Methods and political economy."),
    ("Humanities and social science", "World history, ancient civilization, Intro to Sociology, International Sociological Perspectives, Intro to Political Science, Conflict Resolution, Sociology and Environmental Issues, Political Science and Environmental Issues."),
    ("Technology", "Applied Information Science (ICT)."),
  ],
  miyazaki=[
    ("Faculty Technology Coordinator (1999–2001)", "Supported faculty with teaching technology. Managed two Macintosh computer labs and their student staff."),
  ],
  service=[
    "Nearly 20 peer-reviewed articles.",
    "Peer reviewer, ELTWO Editorial Board, National University of Singapore (2009–2016).",
    "Quality Assurance Committee at Qatar University. Contributed to the CEA self-study that renewed accreditation (Aug. 2026).",
  ],
  publications=[
    "Maggard, J. (2002). Computer-mediated communication and political science: A collaborative learning approach. <cite>Comparative Culture</cite>, 8, 119–129.",
    "Maggard, J., Toyota, H., Lahar, C., Ly, M., &amp; Landes, D. (2004). English proficiency and intercultural contact among Cambodian university students. <cite>Comparative Culture</cite>, 10, 115–134.",
    "Toyota, H., &amp; Maggard, J. (2003). Implications of globalization on Japanese university students. <cite>Comparative Culture</cite>, 9, 149–169.",
    "Lokon, E., &amp; Maggard, J. (2003). Young Japanese people’s views on civic (dis)engagement. <cite>Comparative Culture</cite>, 9, 78–86.",
    "Maggard, J., &amp; Lokon, E. (2004). Student produced iMovies: Motivation through linguistic and artistic expression. <cite>TESOL Video News</cite>, 15(3).",
    "Maggard, J. (2002). VTrain 3.0: Virtual flashcards for language learners. <cite>CALL-EJ Online</cite>, 4(1).",
    "Maggard, J. (2000). Semantic mapping and lexical acquisition: Are CAI methods effective? <cite>Comparative Culture</cite>, 6, 80–93.",
  ],
  presentations=[
    "Colloquium on mobile language learning (invited; with G. Stockwell, M. Kapur and R. Chandran). CELT Symposium, National University of Singapore, 2013.",
    "Common values? English ability, ethnic attitudes, study motivation and intercultural contact (with H. Toyota). 37th World Conference of the International Institute of Sociology, Stockholm, Sweden, July 2005.",
    "Scaffolding independence: CBE experiments in autonomous interlanguage development (with N. Naganuma and others). EuroCALL 2005, Kraków.",
    "Creating iMovie documentaries instead of term papers (with E. Lokon). TESOL 2004, Long Beach.",
    "Reorganizing knowledge structures to build fluency and reduce plagiarism. Thailand TESOL, 2004; Royal University of Phnom Penh, 2004.",
    "Interlanguage development through collaborative learning with CMC. Integrating Content and Language: Meeting the Challenge of a Multilingual Higher Education Conference, Universiteit Maastricht, Netherlands, October 2003.",
    "Using visual models to develop recognition of rhetorical patterns of text. Integrating Content and Language: Meeting the Challenge of a Multilingual Higher Education Conference, Universiteit Maastricht, Netherlands, October 2003.",
    "Using mobile learning tools for formative assessment in task-based classrooms. Qatar University, 2017.",
  ],
  education=[
    "M.A., Applied Linguistics: TESOL, Portland State University. Thesis: “Academic ESL: Semantic Mapping and Lexical Acquisition.”",
    "B.A., English Literature, and Certificate in Black Studies, Portland State University.",
    "Languages: English (native); Spanish (CEFR B1+); Japanese (CEFR A2).",
  ],
)

TOOLS = "Blackboard Ultra, Canvas, Moodle, Google Classroom · PowerPoint, Google Workspace, Adobe Creative Cloud, iMovie, Final Cut Pro, HTML/CSS · Mentimeter, Kahoot!, Padlet, Quizlet, Socrative, Nearpod, Quizizz · Microsoft Forms, Power Automate, SharePoint, Articulate Rise 360, SCORM · Claude Max (Claude and Claude Code), ChatGPT"

GALLERIES = {
  "kamishibai": [
    ("/media/kamishibai/closeup.webp", "A masked figure in a straw cloak, in the falling snow.", "From “The 999 Steps”"),
    ("/media/kamishibai/village.webp", "Two masked figures arrive at a snowy village.", ""),
  ],
  "tales-feature": [
    ("/media/tales/camel.webp", "Student artwork: a rider on a camel silhouetted against an orange desert sky.", "Strength in Forgiveness"),
    ("/media/tales/fish-pattern.webp", "Student artwork: a patterned black-and-white fish swimming among seaweed and bubbles.", "You Reap What You Sow"),
    ("/media/tales/broken-promise.webp", "Student artwork: a woman combs the long hair of a girl wearing a gold headpiece.", "The Broken Promise"),
  ],
  "storytelling-day": [
    ("/media/story-mile/wsd-tent.webp", "Club members telling stories to schoolchildren in a traditional tent."),
    ("/media/story-mile/wsd-majlis.webp", "Children gather in a majlis for food and stories."),
    ("/media/story-mile/wsd-arrival.webp", "School groups arrive at Abu Dhabi Heritage Village."),
    ("/media/story-mile/wsd-falcon.webp", "A falconry demonstration during the day."),
  ],
  "kharareef": [
    ("/media/story-mile/al-kharareef.webp", "The Al Kharareef Storytelling Club banner."),
    ("/media/story-mile/story-illustration.webp", "A story illustration from the project."),
  ],
  "pi-app": [
    ("/media/pi/tutor.webp", "Pure Intellect Tutor: it asks one question at a time and gives hints only when asked."),
    ("/media/pi/feedback.webp", "Student feedback: rubric levels and the professor’s chosen comments."),
    ("/media/pi/analyzer.webp", "Pure Intellect Analyzer: the professor’s queue of hand-ins to grade."),
    ("/media/pi/analyzer-item.webp", "Analyzer: suggested rubric levels, with the student’s own words as evidence."),
    ("/media/pi/gradebook.webp", "Gradebook with Excel and CSV export."),
  ],
  "course-site": [
    ("/media/pi/home.webp", "Course website home: an illustrated campus map for navigation."),
    ("/media/pi/weeks.webp", "Weeks 1–15, grouped by unit, each with its guiding question."),
    ("/media/pi/activity.webp", "An activity in five Bloom’s-sequenced steps, with its AI mode."),
    ("/media/pi/graded.webp", "Graded work: weights, due dates and what strong work does."),
  ],
  "cast": [
    ("/media/falcon/cast-mohammed.webp", "Character Guide: Mohammed, the hunter. Face, outfit and turnaround."),
    ("/media/falcon/cast-abdulla.webp", "Character Guide: Abdulla. Face, expressions and outfit."),
    ("/media/falcon/cast-elder.webp", "Character Guide: the Elder. Face expressions and outfit."),
    ("/media/falcon/cast-wife.webp", "Character Guide: the Wife, in niqab, shayla and abaya. Turnaround."),
    ("/media/falcon/cast-son.webp", "Character Guide: the Son. Full body, expressions and turnaround."),
  ],
  "art": [
    ("/media/falcon/art-direction.webp", "Locked art direction, style guide and asset library: locations, props and color palette."),
    ("/media/falcon/cast-board.webp", "Locked cast reference board."),
  ],
  "storyboard": [
    ("/media/falcon/storyboard-layout.webp", "Opening scene layout plan."),
    ("/media/falcon/storyboard-proof.webp", "Opening scene final proof."),
  ],
  "promo": [
    ("/media/falcon/thumbnail.webp", "Episode 1 thumbnail."),
    ("/media/falcon/title-art.webp", "LinkedIn carousel: title card."),
    ("/media/falcon/promo-tent.webp", "LinkedIn carousel: the camp."),
    ("/media/falcon/promo-release.webp", "LinkedIn carousel: the release."),
  ],
}
