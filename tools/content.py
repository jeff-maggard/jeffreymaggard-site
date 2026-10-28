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
        caption="Title, story crawl and sunrise. 2D animation with a Pixar-inspired look. 68 seconds.",
    ),
    "pure-intellect-tutor": dict(
        src="/media/pure-intellect-tutor.mp4", poster="/media/pure-intellect-tutor.jpg", ratio="4 / 5",
        title="Pure Intellect Tutor · launch video",
        caption="A 60-second launch video for my AI tutor, built from real screens of the course website. Captioned to work with no sound.",
    ),
    "gofluent-promo": dict(
        src="/media/gofluent-promo.mp4", poster="/media/gofluent-promo.jpg", ratio="16 / 9",
        title="Instructional designer introduction · goFLUENT application video",
        caption="A 90-second introduction I scripted for an instructional design role. Motion graphics coded in React with Remotion, with an AI voice and an original piano score.",
    ),
}

PROJECTS = [
# ---------------------------------------------------------------- 1
dict(
  slug="two-country-course", art="exchange", cats=["courses", "teaching"],
  tag="Interdisciplinary · Virtual exchange",
  title="A shared first-year course across two countries",
  summary="Political science students in Japan and sociology students in Maine shared one website, one textbook and joint projects.",
  hook="Two institutions, two disciplines and one shared course website, years before “virtual exchange” had a name.",
  facts=dict(
    context="First-year students in two countries studied the same public issues from two disciplines.",
    audience="Political science students at Miyazaki International College (now Miyazaki International University). Sociology students at York County Technical College (now York County Community College) in Maine.",
    role="Designed the exchange. Wrote the website code and taught students to code. Co-taught with Dr. Kiyohiko Toyama and Dr. Cindy Lahar.",
    tools=["HTML/CSS", "Course website", "Shared textbook", "Video"],
  ),
  sections=[
    ("The challenge", [
      "<p>Political science students at Miyazaki International College (now Miyazaki International University) and sociology students at York County Technical College (now York County Community College) in Maine needed a reason to work together across an ocean.</p>",
    ]),
    ("The approach", [
      "<p>Both classes shared one website and one textbook. Students researched public issues together. They presented their findings in writing, speech and video.</p>",
      "<p>I wrote the website code. I also taught students to code, so they could publish their own work.</p>",
      '<div class="callout"><b>Why it matters today</b>This approach is now called virtual exchange, or COIL (Collaborative Online International Learning).</div>',
    ]),
    ("The team", [
      "<p>I co-taught with Dr. Kiyohiko Toyama (political science) and Dr. Cindy Lahar (sociology, Maine).</p>",
    ]),
    ("The outcome", [
      "<p>The course led to a peer-reviewed paper:</p>",
      '<p class="note">Maggard, J. (2002). Computer-mediated communication and political science: A collaborative learning approach. <cite>Comparative Culture</cite>, 8, 119–129.</p>',
    ]),
  ],
),
# ---------------------------------------------------------------- 2
dict(
  slug="english-21st-century", art="book", cats=["courses"],
  tag="Garnet Press · CEFR B1+",
  title="English for the 21st Century",
  summary="A CEFR B1+ course book, co-created with a team at Garnet Press.",
  hook="A published course book, built and refined over three editions.",
  facts=dict(
    context="Learners at CEFR B1+ needed a course book matched to their level.",
    audience="Adult English learners at CEFR B1+.",
    role="Co-creator. Editor of the 1st, 2nd and 3rd editions. Designated curriculum editor of the 3rd edition.",
    tools=["CEFR", "Scope and sequence", "Editing", "Publishing"],
  ),
  sections=[
    ("The project", [
      "<p><cite>English for the 21st Century</cite> is a CEFR B1+ course book. I co-created it with a team at Garnet Press.</p>",
    ]),
    ("My role", [
      '<ol class="steps"><li>Co-creator of the course book.</li><li>Editor of the 1st, 2nd and 3rd editions.</li><li>Designated curriculum editor of the 3rd edition (Aug. 2026).</li></ol>',
    ]),
    ("Process", [
      '<div class="media-slot">[Book cover and sample spreads: to be supplied]</div>',
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
  facts=dict(
    context="A Qatari folktale about compassion and forgiveness, ready for a new audience.",
    audience="Museum visitors, families and young viewers on YouTube.",
    role="Collector and editor of the story. Writer and producer of the animated film. Chair of the Cultural Awareness Team.",
    tools=["Story adaptation", "Storyboards", "Character Guide", "AI image and video", "Lip sync", "ffmpeg", "Sound design"],
  ),
  sections=[
    ("The story", [
      "<p>“He Who Doesn’t Know the Falcon Roasts It” is a Qatari folktale I collected and edited.</p>",
      "<p>It concludes Lila Abu-Lughod’s opening chapter in <cite>On the Move: Reframing Nomadic Pastoralism</cite> (Doha: Qatar Museums; [Milan]: Skira, 2022). The book thanks me and my Qatar University faculty editors. The National Museum of Qatar featured the story in its On the Move exhibition (Fall 2022 – Winter 2023).</p>",
    ]),
    ("From story to screen", [
      "<p>I am writing and producing an animated series of the story. Episode 1 is in production.</p>",
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
  slug="kamishibai", art="kamishibai", cats=["cultural"],
  tag="UNESCO-funded",
  title="UNESCO Mongolia Kamishibai Program",
  summary="Japanese paper-theater storytelling for university and K-12 students in Mongolia and Japan. A $30,000 grant.",
  hook="A two-year UNESCO project that brought Japanese paper theater to students in Mongolia and Japan.",
  facts=dict(
    context="A two-year, $30,000 UNESCO/Japan Funds-in-Trust grant at Akita International University (2005–2006).",
    audience="University students and faculty, plus K-12 students in Mongolia and Japan.",
    role="Principal Investigator and Steering Committee Chair. Director of the documentary team.",
    tools=["Kamishibai", "Grant writing", "Documentary", "Program leadership"],
  ),
  sections=[
    ("The program", [
      "<p>Kamishibai is Japanese paper-theater storytelling. This program used it to connect students in Mongolia and Japan.</p>",
      "<p>More than 40 faculty and students took part at Akita International University and the University of the Humanities (Ulaanbaatar). K-12 students in Mongolia and Japan joined too.</p>",
    ]),
    ("My role", [
      '<ul class="points"><li>Principal Investigator and Steering Committee Chair.</li><li>Directed the documentary team.</li></ul>',
    ]),
    ("Next", [
      '<div class="media-slot">[Improved artwork and a new story are coming. Japanese stories will be added.]</div>',
    ]),
  ],
),
# ---------------------------------------------------------------- 5
dict(
  slug="pure-intellect", art="tutor", cats=["ai"],
  tag="AI apps · Claude Code",
  title="Pure Intellect Tutor, Analyzer &amp; AI Ranking App",
  summary="AI education tools I design and build: a tutor that asks questions instead of giving answers, and a grading assistant for professors.",
  hook="AI that coaches students to think, and helps professors grade fairly.",
  video="pure-intellect-tutor",
  facts=dict(
    context="Students can ask AI to do the work for them. I wanted AI that makes them think harder instead.",
    audience="First-year university students and their professors.",
    role="Designer and developer.",
    tools=["Claude", "Claude Code", "React", "TypeScript", "Vite", "Three.js", "Vitest", "Playwright"],
  ),
  sections=[
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
      "<p>48 automated tests, plus a scripted click-through on desktop and phone.</p>",
      '<div class="media-slot">[App screenshots: to be added]</div>',
    ]),
  ],
),
# ---------------------------------------------------------------- 6
dict(
  slug="engl-203", art="timeline", cats=["courses", "ai"],
  tag="Course design · AI",
  title="ENGL 203: AI-Enhanced Academic Research and Writing",
  summary="A 15-week course. Students log every AI step and defend their choices orally.",
  hook="A writing course where AI use is visible, logged and defended.",
  facts=dict(
    context="Students now research and write with AI. The course makes that use transparent.",
    audience="University students, with differentiation for B1 and C1 learners.",
    role="Course designer (proposal under review at Qatar University).",
    tools=["Syllabus", "Scope and sequence", "Rubrics", "AI use policy"],
  ),
  sections=[
    ("Structure", [
      "<p>A 15-week syllabus with scope and sequence in three phases:</p>",
      '<ol class="steps"><li>AI literacy and research.</li><li>Writing as process.</li><li>Presentation and reflection.</li></ol>',
    ]),
    ("Assessment", [
      "<p>Students keep an AI Research Log. They defend their choices in an oral defense.</p>",
      "<p>The course includes rubrics, an AI use policy and differentiation for B1 and C1 learners.</p>",
      '<div class="media-slot">[Syllabus preview: to be supplied]</div>',
    ]),
  ],
  status="Proposal under review.",
),
# ---------------------------------------------------------------- 7
dict(
  slug="ai-humanities-course", art="course-map", cats=["courses", "ai"],
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
    ("Measuring success", [
      "<p>The course has not been taught yet. In a live course, success would show in the thinking logs, the rubric scores on each signature activity and the quality of the final decision briefs.</p>",
    ]),
  ],
  status="Sample course concept. Not affiliated with or endorsed by any university.",
),
# ---------------------------------------------------------------- 8
dict(
  slug="rhetoric-composition", art="lessons", cats=["courses", "video"],
  tag="Course design · AP-aligned",
  title="College-Level Rhetoric and Composition",
  summary="A full grade 11 course map: nine units, 108 lessons and a sample lesson package with video scripts.",
  hook="108 lessons, each built from the same reliable pattern: watch, practice, check.",
  facts=dict(
    context="An AP-aligned rhetoric and composition course for grade 11.",
    audience="Grade 11 students.",
    role="Course designer, scriptwriter and assessment writer.",
    tools=["Course map", "Video scripts", "Guided notes", "Quizzes", "Rubrics"],
  ),
  sections=[
    ("Course map", [
      "<p>Nine units and 108 lessons, built on public-domain nonfiction by Lincoln, Douglass, Wollstonecraft, Wells, Du Bois and others.</p>",
      "<p>Each lesson pairs a short video, a guided activity and a three-question quiz.</p>",
    ]),
    ("Sample lesson package", [
      "<p><b>“Reading the Rhetorical Situation”</b> (Unit 1, Lesson 1):</p>",
      '<ul class="points"><li>A video script with visual cues.</li><li>Printable guided notes using Elizabeth I’s Tilbury speech.</li><li>A five-question quiz with feedback on every answer.</li><li>An original four-level rubric.</li></ul>',
    ]),
    ("Video scripts", [
      "<p>Three teleprompter scripts: “What Counts as Evidence?”, “A Thesis That Needs Defending” and “Linking Evidence to Your Claim.”</p>",
      "<p>Each has timecodes, on-screen cues, a 20-second practice pause and a scaffolded quiz (identify, apply, analyze).</p>",
    ]),
  ],
),
# ---------------------------------------------------------------- 9
dict(
  slug="engl250-assessments", art="assessment", cats=["courses", "teaching"],
  tag="Assessment design · Qatar University",
  title="ENGL250 assessments",
  summary="Selected for the task force that created ENGL250. Co-created all of its assessments and edits its exams.",
  hook="Fair, consistent assessment across every section of a course.",
  facts=dict(
    context="A new course, ENGL250, needed assessments that work the same way in every section.",
    audience="Qatar University students and the faculty who teach ENGL250.",
    role="Task force member. Co-creator of all assessments. Midterm and final exam editor. Grading-norming facilitator.",
    tools=["Exams", "Rubrics", "Grading norming", "Piloting"],
  ),
  sections=[
    ("Timeline", [
      '<ol class="steps"><li>Selected for the task force that created ENGL250 (2018).</li><li>Piloted the course (2019).</li><li>Co-created all of its assessments.</li><li>Midterm and final exam editor.</li></ol>',
    ]),
    ("Consistency", [
      "<p>I facilitate grading norming across sections, so every student is scored against the same standard.</p>",
    ]),
  ],
),
# ---------------------------------------------------------------- 10
dict(
  slug="story-mile", art="story-mile", cats=["cultural"],
  tag="Zayed University · Public exhibition",
  title="The Story Mile",
  summary="300 student authors. A public exhibition on the Abu Dhabi Corniche, a permanent installation and a book.",
  hook="Student stories, written for the public and installed along the Abu Dhabi Corniche.",
  facts=dict(
    context="A storytelling project at Zayed University, made with major cultural partners.",
    audience="Zayed University students and the public in Abu Dhabi.",
    role="Co-founder of the Al Kharareef storytelling club. Co-creator of the Story Mile Project. Editor of the book.",
    tools=["Storytelling", "Partnerships", "Exhibition", "Editing"],
  ),
  sections=[
    ("The project", [
      "<p>I co-founded the Al Kharareef storytelling club. I co-created the Story Mile Project with Mubadala, the Sharjah Institute for Heritage and the Abu Dhabi Music &amp; Arts Festival.</p>",
    ]),
    ("The outcome", [
      '<ul class="points"><li>300 student authors took part.</li><li>A public exhibition on the Abu Dhabi Corniche.</li><li>A permanent installation at Khalifa Park.</li><li>The book <cite>The Story Mile</cite> (ISBN 978-9948-20-117-5), which I edited.</li></ul>',
      '<div class="media-slot">[Story Mile photos: to be supplied]</div>',
    ]),
  ],
),
# ---------------------------------------------------------------- 11
dict(
  slug="tales-of-forgiveness", art="tales", cats=["cultural"],
  tag="Bilingual book · Qatar University",
  title="Tales of Forgiveness",
  summary="A bilingual (Arabic/English) book of Qatari folktales collected by Qatar University students.",
  hook="Qatari folktales of compassion and forgiveness, collected by students.",
  facts=dict(
    context="Qatari folktales that show compassion and forgiveness.",
    audience="Readers of Arabic and English.",
    role="Lead editor, working with six co-editors. Chair of the Cultural Awareness Team (2016–2023).",
    tools=["Editing", "Translation", "Team leadership"],
  ),
  sections=[
    ("The book", [
      "<p><cite>Tales of Forgiveness</cite> is an unpublished bilingual (Arabic/English) book of Qatari folktales collected by Qatar University students. The stories show compassion and forgiveness.</p>",
    ]),
    ("My role", [
      "<p>I am lead editor, working with six co-editors. As Chair of the Cultural Awareness Team (2016–2023), I led more than 150 students, faculty and staff on the project.</p>",
    ]),
  ],
),
# ---------------------------------------------------------------- 12
dict(
  slug="peace-studies-seminar", art="seminar", cats=["cultural", "teaching"],
  tag="Miyazaki · Fall 2003",
  title="Peace Studies Seminar on Cambodia",
  summary="A 15-week, certificate-bearing seminar for 200+ students and community members, with a study trip to Cambodia.",
  hook="A seminar that brought faculty, embassies and NGOs into one classroom.",
  facts=dict(
    context="A 15-week, certificate-bearing seminar at Miyazaki (Fall 2003).",
    audience="More than 200 students and community members.",
    role="Co-creator. Leader of the student trip to Phnom Penh and Siem Reap.",
    tools=["Seminar design", "Partnerships", "Study abroad"],
  ),
  sections=[
    ("The seminar", [
      "<p>I co-created the seminar with 11 faculty, embassy staff from Cambodia and Japan, plus NGO staff.</p>",
      "<p>It served more than 200 students and community members.</p>",
    ]),
    ("The trip", [
      "<p>I led a student trip to Phnom Penh and Siem Reap.</p>",
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
  facts=dict(
    context="A blended sociology course at Miyazaki.",
    audience="University sociology students.",
    role="Writer, director and producer of the video series. Builder of the course website.",
    tools=["Scriptwriting", "Video production", "Course website"],
  ),
  sections=[
    ("The course", [
      "<p>I wrote, directed and produced the video series for a blended course taught with sociologist Dr. Hiroyuki Toyota.</p>",
      "<p>Students used the videos in class and online, alongside live lectures and a textbook. I built the course website.</p>",
    ]),
  ],
),
# ---------------------------------------------------------------- 14
dict(
  slug="motion-videos", art="motion", cats=["video", "ai"],
  tag="Motion graphics · Launch videos",
  title="Launch and promo videos",
  summary="Product launch videos, course walkthroughs and introductions, built as code with Remotion and AI voice.",
  hook="Launch videos built entirely in code: scripted, timed and captioned.",
  video="pure-intellect-tutor",
  facts=dict(
    context="Products and courses need short videos that explain them fast.",
    audience="Faculty, hiring teams and LinkedIn viewers.",
    role="Scriptwriter, designer and producer.",
    tools=["Remotion", "React", "AI voice", "Original music direction", "Captions", "ffmpeg"],
  ),
  sections=[
    ("What I make", [
      '<ul class="points"><li>Product launch videos, such as the Pure Intellect Tutor video.</li><li>Course website walkthroughs, captioned to work with no sound.</li><li>Introduction videos for job applications.</li><li>Formats for every channel: 16:9, 9:16, 1:1 and 4:5 for LinkedIn.</li></ul>',
    ]),
    ("How I build them", [
      "<p>Every frame is coded in React with Remotion. Captions and graphics are timed to the measured voice track. The music bed is an original piano score. I write every script.</p>",
      "@video:gofluent-promo",
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
    "Common values? English ability, ethnic attitudes, study motivation and intercultural contact (with H. Toyota). 37th World Congress, International Institute of Sociology, Stockholm, 2005.",
    "Scaffolding independence: CBE experiments in autonomous interlanguage development (with N. Naganuma and others). EuroCALL 2005, Kraków.",
    "Creating iMovie documentaries instead of term papers (with E. Lokon). TESOL 2004, Long Beach.",
    "Reorganizing knowledge structures to build fluency and reduce plagiarism. Thailand TESOL, 2004; Royal University of Phnom Penh, 2004.",
    "Using mobile learning tools for formative assessment in task-based classrooms. Qatar University, 2017.",
  ],
  education=[
    "M.A., Applied Linguistics: TESOL, Portland State University. Thesis: “Academic ESL: Semantic Mapping and Lexical Acquisition.”",
    "B.A., English Literature, and Certificate in Black Studies, Portland State University.",
    "Languages: English (native); Spanish (CEFR B1+); Japanese (CEFR A2).",
  ],
)

TOOLS = "Blackboard Ultra, Canvas, Moodle, Google Classroom · PowerPoint, Google Workspace, Adobe Creative Cloud, iMovie, Final Cut Pro, HTML/CSS · Mentimeter, Kahoot!, Padlet, Quizlet, Socrative, Nearpod, Quizizz · Claude, Claude Code, ChatGPT"

GALLERIES = {
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
    ("/media/falcon/storyboard-draft.webp", "Opening scene draft."),
    ("/media/falcon/storyboard-proof.webp", "Opening scene final proof."),
  ],
  "promo": [
    ("/media/falcon/thumbnail.webp", "Episode 1 thumbnail."),
    ("/media/falcon/title-art.webp", "LinkedIn carousel: title card."),
    ("/media/falcon/promo-tent.webp", "LinkedIn carousel: the camp."),
    ("/media/falcon/promo-release.webp", "LinkedIn carousel: the release."),
  ],
}
