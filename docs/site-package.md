# jeffreymaggard.com — Build Package for Claude Code

Paste Section 1 into a new Claude Code session. Keep this whole file in the project folder so Claude Code can refer to every section. The approved home page design is in `home-design-reference.dc.html`. It is a design-tool file: use it as a visual and layout reference, then rebuild it as clean HTML/CSS.

---

## 1. Prompt for Claude Code

> Build a brand-new portfolio website for me, Jeffrey Maggard, at jeffreymaggard.com. Use this package file as the single source of truth for design, copy and facts. Do not copy or reuse my old Netlify site, and do not change or delete it.
>
> **Goal:** Show hiring managers in instructional design, curriculum development, EdTech and university teaching (humanities, social science, writing) that I design learning at a professional level. Projects are the star.
>
> **Build:** A static site in plain HTML/CSS/JS, or Astro if it helps with shared layouts. No paid services. No server code unless I approve it. Mobile-first, fast and accessible.
>
> **Hosting (already set up; follow exactly):**
> - Domain jeffreymaggard.com is registered at Namecheap. Its nameservers point to Cloudflare (ingrid.ns.cloudflare.com, jaime.ns.cloudflare.com).
> - My Cloudflare account uses Google sign-in. The zone is active on the Free plan.
> - Email Routing is live: jeff@jeffreymaggard.com forwards to my Gmail. **Never touch the MX, SPF (TXT) or DKIM records, or the Email Routing settings.**
> - Log in: `npx wrangler login` (I approve in the browser).
> - Create the project: `npx wrangler pages project create jeffreymaggard --production-branch main`
> - Deploy: `npx wrangler pages deploy <output-folder> --project-name jeffreymaggard`
> - After every deploy, give me the preview link (https://jeffreymaggard.pages.dev).
> - Custom domain: when I approve the site, I will attach jeffreymaggard.com and www.jeffreymaggard.com in the Cloudflare dashboard (Workers & Pages > jeffreymaggard > Custom domains). Two old Namecheap parking records must be replaced at that step: A record @ 162.255.119.62, and CNAME www > parkingpage.namecheap.com. **Tell me before anything touches DNS.**
>
> **Working style:** Follow the content rules in Section 3 strictly. Never invent facts, numbers or titles; mark anything uncertain [CHECK]. Ask me for missing facts or files instead of guessing. Use clearly labeled placeholders for images I haven't supplied yet. After each major step, explain in plain language what you did and what you need from me.
>
> **Order of work:** (1) Set up the project and design tokens. (2) Build the Home page to match the reference design. (3) Deploy a preview. (4) Build the inner pages. (5) Add my assets as I send them.

---

## 2. Design system ("Night Studio", with Plus Jakarta Sans)

**Look:** dark navy, bold type and a mint accent. A tech-forward bento grid of project cards. Modern and focused, but warm and human, not corporate.

### Colors
| Token | Hex | Use |
|---|---|---|
| `--bg` | #0F1724 | Page background (night navy) |
| `--card` | #172235 | Card background |
| `--card-media` | #22324A | Image placeholder blocks |
| `--border` | #263449 | Card borders, dividers |
| `--border-strong` | #3A4A5E | Secondary button outline |
| `--text` | #EEF2F6 | Headlines, primary text |
| `--text-body` | #B7C2CF | Body text, nav links |
| `--text-muted` | #8FA0B3 | Role lines, labels, footer |
| `--accent` | #6EE7C8 | Mint: labels, primary button, logo dot |
| `--on-accent` | #0F1724 | Text on mint buttons |

Check contrast: body text must meet 4.5:1 on `--bg` and `--card`.

### Typography
- **One typeface everywhere: Plus Jakarta Sans** (Google Fonts, weights 400, 500, 600, 700, 800). It was chosen because it is the easiest to read.
- Hero headline: 800 weight, `clamp(42px, 6.4vw, 88px)`, line-height 1.0, letter-spacing -0.035em.
- Section headline: 800, `clamp(34px, 4.6vw, 60px)`, letter-spacing -0.03em.
- Card title: 800, 24px (28px on wide feature cards), line-height 1.2.
- Body: 400, 17px, line-height 1.6. Lead paragraph: 19px.
- Labels (card tags, eyebrows): 700, 13–15px, uppercase, letter-spacing 0.06em, mint.

### Layout and components
- Content max-width 1200px; 24px side padding; no horizontal scrolling on phones.
- **Header:** wordmark `jeffrey.maggard` (the dot in mint) on the left. Nav on the right: Instructional Design · Teaching · Cultural Projects · AI Projects · Contact. It wraps on small screens.
- **Hero:** mint eyebrow `// INSTRUCTIONAL DESIGN · TEACHING · AI`, a big headline, and a black-and-white portrait on the right (4:5 crop, 16px radius). Below: a lead paragraph plus two buttons (mint "Contact me"; outlined "Projects ↓").
- **Project cards (bento):** flex-wrap row, 20px gap. Wide cards `flex: 2 1 560px`; standard cards `flex: 1 1 320px`. Card: `--card` background, 1px `--border`, 16px radius, 28px padding. Inside: an image block (10px radius), a mint tag, a title, a purpose line, then a muted "Role · …" line.
- **Closing CTA:** top border, big headline "Have a learning project? *Let's talk.*" (the second sentence in mint). Email and LinkedIn links on the right.
- **Footer:** "© Jeffrey Maggard", muted.
- Buttons and links: minimum 44px touch targets, visible focus styles, real `<a>`/`<button>` elements.
- Images: real alt text on every image.

---

## 3. Content rules (strict)

1. No age, total years of experience, "decades" or similar. Dates on individual jobs are fine.
2. Short, clear sentences. Every phrase must be clear on first read. No repeated information.
3. Never put three or more "and"s in one sentence. Use a comma list with one "and" before the last item.
4. First mention: "Miyazaki International College (now Miyazaki International University)". After that: "Miyazaki" or "MIC".
5. First mention: "York County Technical College (now York County Community College)". It was renamed in July 2003.
6. Never hyphenate "community college".
7. Publisher is **Garnet Education** (Jeffrey's decision, 28 Oct 2026). Wording (updated 29 Oct 2026): "co-created a B1+ English course"; role list: co-creator of the syllabus and assessments (2019), piloted the course (2019), faculty reviewer of the 1st and 2nd editions, "Designated faculty editor for the 3rd edition (2026)."
8. Never write "Blackboard Learn" or "Blackboard administrator". "Blackboard Ultra" is fine. Chairing the WebCT/Blackboard Committee at UNT is fine.
9. The Qatari folktale book is titled **Tales of Qatari Heritage** (Jeffrey's decision, 28 Oct 2026; replaces "Tales of Forgiveness").
10. The falcon story title is **"He Who Doesn't Know the Falcon Roasts It."**
11. Peer-reviewed articles: say **"nearly 20"**.
12. Never use the word "Bible" in any title. Say "Character Guide" or "Style Guide".
13. No phone numbers. No street addresses. No mention of the PCC foreclosure story.
14. Only use facts from this file or files I give you. Mark uncertain items [CHECK].

---

## 4. Site map

| Page | Purpose |
|---|---|
| Home | Who I am, featured projects, contact |
| Instructional Design & Curriculum | Course design, textbook, assessments, AI course, sample lesson package |
| Teaching & Academic Work | University courses by area, publications, presentations |
| Cultural Projects | Folktales, museum work, kamishibai, animation, Peace Studies Seminar |
| AI Projects | Claude Code builds (add as finished) |
| Contact / CV | Email, LinkedIn, CV download |

---

## 5. Home page copy (approved)

**Eyebrow:** // INSTRUCTIONAL DESIGN · TEACHING · AI
**Headline:** Curriculum designer. Program builder. Teacher.
**Lead:** I design courses, materials and programs that help students learn by doing real work. I use AI to speed up design, while students keep their own voice.
**Buttons:** Contact me (mailto:jeff@jeffreymaggard.com) · Projects ↓

**Featured projects heading:** FEATURED PROJECTS

Cards in this order (1 and 6 are wide):

1. **INTERDISCIPLINARY · VIRTUAL EXCHANGE**
   **A shared first-year course across two countries**
   Political science students at Miyazaki International College (now Miyazaki International University) and sociology students at York County Technical College (now York County Community College) in Maine shared one website and textbook. They researched public issues and presented in writing, speech and video. The course led to a peer-reviewed paper in *Comparative Culture* (2002).
   Role · Designed the exchange; wrote the website code and taught students to code. Co-taught with Dr. Kiyohiko Toyama (political science) and Dr. Cindy Lahar (sociology, Maine).
   Image: [Course website or student work]

2. **GARNET PRESS · CEFR B1+**
   **English for the 21st Century**
   A CEFR B1+ course book, co-created with a team at Garnet Press.
   Role · Co-creator; editor of all three editions; curriculum editor of the 3rd edition.
   Image: [Book cover]

3. **MUSEUM PARTNERSHIP**
   **On the Move · National Museum of Qatar**
   "He Who Doesn't Know the Falcon Roasts It," a Qatari folktale I collected and edited, concludes Lila Abu-Lughod's opening chapter of the exhibition book. The museum featured it in the On the Move exhibition (Fall 2022 – Winter 2023).
   Role · Collector and editor; Chair of the Cultural Awareness Team; writer and producer of my own animated film of the story.
   Image: [Animated film still]

4. **UNESCO-FUNDED**
   **UNESCO Mongolia Kamishibai Program**
   Japanese paper-theater storytelling for university and K-12 students in Mongolia and Japan. A $30,000 grant.
   Role · Principal Investigator and Steering Committee Chair.
   Image: [Kamishibai image — Jeffrey is improving the art]

5. **AI APPS · CLAUDE CODE**
   **Pure Intellect Tutor, Analyzer & AI Ranking App**
   AI-powered education tools I design and build.
   Role · Designer and developer.
   Image: [App screens]

6. **COURSE DESIGN · AI**
   **ENGL 203: AI-Enhanced Academic Research and Writing**
   A 15-week course. Students log every AI step and defend their choices orally.
   Role · Course designer (proposal under review).
   Image: [Syllabus preview]

**Closing CTA:** Have a learning project? Let's talk.
**Links:** jeff@jeffreymaggard.com · LinkedIn (https://www.linkedin.com/in/jeff-maggard-a01181b3)

---

## 6. Inner page content

### 6.1 Instructional Design & Curriculum

**Intro:** I design courses, assessments and materials, from scope and sequence to rubrics.

Portfolio pieces:
1. **ENGL 203: AI-Enhanced Academic Research and Writing.** A 15-week syllabus with scope and sequence in three phases: AI literacy and research; writing as process; presentation and reflection. Students keep an AI Research Log and defend their choices in an oral defense. Includes rubrics, an AI use policy and differentiation for B1 and C1 learners. Status: proposal under review at Qatar University.
2. **College-Level Rhetoric and Composition (AP-aligned, grade 11).** A full course map: nine units, 108 lessons and public-domain nonfiction texts (Lincoln, Douglass, Wollstonecraft, Wells, Du Bois and others). Each lesson pairs a short video, a guided activity and a three-question quiz.
3. **Sample lesson package: "Reading the Rhetorical Situation" (Unit 1, Lesson 1).** A video script with visual cues, printable guided notes using Elizabeth I's Tilbury speech, a five-question quiz with feedback on every answer and an original four-level rubric.
4. **Three teleprompter video scripts:** "What Counts as Evidence?", "A Thesis That Needs Defending" and "Linking Evidence to Your Claim." Each has timecodes, on-screen cues, a 20-second practice pause and a scaffolded quiz (identify, apply, analyze).
5. **English for the 21st Century (CEFR B1+), Garnet Press.** Co-creator; editor of the 1st, 2nd and 3rd editions; designated curriculum editor for the 3rd edition (Aug. 2026).
6. **ENGL250 assessments, Qatar University.** Selected for the task force that created ENGL250 (2018); piloted it in 2019. Midterm and final exam editor. Co-created all of its assessments. Facilitates grading norming across sections.
7. **A shared first-year course across two countries** (see Home card 1). Add a longer case study: two institutions, one website, joint student projects in writing, speech and video. Today this approach is called virtual exchange or COIL (Collaborative Online International Learning).

Tools: Blackboard Ultra, Canvas, Moodle, Google Classroom · PowerPoint, Google Workspace, Adobe Creative Cloud, iMovie, Final Cut Pro, HTML/CSS · Mentimeter, Kahoot!, Padlet, Quizlet, Socrative, Nearpod, Quizizz · Claude, Claude Code, ChatGPT.

### 6.2 Teaching & Academic Work

**Intro:** I have taught university writing, humanities and social science courses in Japan, the USA, the UAE and Qatar.

Courses by area:
- **Academic English:** research writing, reading, grammar, communication, presentation and pronunciation. IELTS, TOEFL and TOEIC preparation.
- **Content-based courses:** political science, sociology, teacher education, business, law, linguistics, TESOL Methods and political economy.
- **Humanities and social science:** world history, ancient civilization, Intro to Sociology, International Sociological Perspectives, Intro to Political Science, Conflict Resolution, Sociology and Environmental Issues, Political Science and Environmental Issues.
- **Technology:** Applied Information Science (ICT).

Miyazaki highlights (inner page only, not Home):
- **Video lecture course in sociology.** I wrote, directed and produced the video series for a blended course taught with sociologist Dr. Hiroyuki Toyota. Students used the videos in class and online, alongside live lectures and a textbook. I built the course website. (The site no longer exists; no image needed. Text only.)
- **Faculty Technology Coordinator (1999–2001).** Supported faculty with teaching technology. Managed two Macintosh computer labs and their student staff.
- **Peace Studies Seminar on Cambodia (Fall 2003).** See Cultural Projects.

Current role: Lecturer, Foundation Program, Department of English, Qatar University (Feb. 2014 – present). Content-based courses in business, law and EFL for humanities, STEM, international affairs and mass communication students. About eight years of online and hybrid teaching.

Research and service:
- Nearly 20 peer-reviewed articles (selected list below).
- Peer reviewer, ELTWO Editorial Board, National University of Singapore (2009–2016).
- Quality Assurance Committee at Qatar University; contributed to the CEA self-study that renewed accreditation (Aug. 2026).

Selected publications:
- Maggard, J. (2002). Computer-mediated communication and political science: A collaborative learning approach. *Comparative Culture*, 8, 119–129.
- Maggard, J., Toyota, H., Lahar, C., Ly, M., & Landes, D. (2004). English proficiency and intercultural contact among Cambodian university students. *Comparative Culture*, 10, 115–134.
- Toyota, H., & Maggard, J. (2003). Implications of globalization on Japanese university students. *Comparative Culture*, 9, 149–169.
- Lokon, E., & Maggard, J. (2003). Young Japanese people's views on civic (dis)engagement. *Comparative Culture*, 9, 78–86.
- Maggard, J., & Lokon, E. (2004). Student produced iMovies: Motivation through linguistic and artistic expression. *TESOL Video News*, 15(3).
- Maggard, J. (2002). VTrain 3.0: Virtual flashcards for language learners. *CALL-EJ Online*, 4(1).
- Maggard, J. (2000). Semantic mapping and lexical acquisition: Are CAI methods effective? *Comparative Culture*, 6, 80–93.

Selected presentations:
- Colloquium on mobile language learning (invited; with G. Stockwell, M. Kapur and R. Chandran). CELT Symposium, National University of Singapore, 2013.
- Common values? English ability, ethnic attitudes, study motivation and intercultural contact (with H. Toyota). 37th World Congress, International Institute of Sociology, Stockholm, 2005.
- Scaffolding independence: CBE experiments in autonomous interlanguage development (with N. Naganuma and others). EuroCALL 2005, Kraków.
- Creating iMovie documentaries instead of term papers (with E. Lokon). TESOL 2004, Long Beach.
- Reorganizing knowledge structures to build fluency and reduce plagiarism. Thailand TESOL, 2004; Royal University of Phnom Penh, 2004.
- Using mobile learning tools for formative assessment in task-based classrooms. Qatar University, 2017.

### 6.3 Cultural Projects

- **On the Move · National Museum of Qatar.** "He Who Doesn't Know the Falcon Roasts It" concludes Lila Abu-Lughod's opening chapter in *On the Move: Reframing Nomadic Pastoralism* (Doha: Qatar Museums; [Milan]: Skira, 2022). The book thanks Jeffrey Darin Maggard and his Qatar University faculty editors. The story was featured in the exhibition (Fall 2022 – Winter 2023).
- **My animated folktale film.** I wrote and produced an animated film of the falcon story. Embed the film here. A "Character Guide" page or image can show the design process: style guide, characters, props and settings. (Never call it a "Bible".)
- **Tales of Forgiveness.** An unpublished bilingual (Arabic/English) book of Qatari folktales collected by Qatar University students. The stories show compassion and forgiveness. I am lead editor, working with six co-editors. As Chair of the Cultural Awareness Team (2016–2023), I led 150+ students, faculty and staff on the project.
- **The Story Mile, Zayed University.** I co-founded the Al Kharareef storytelling club at Zayed University in 2010 and was a faculty supervisor. In 2013, I invited the master storyteller Abdul Aziz Al Musallam, head of the Sharjah Institute for Heritage, to Zayed University to help faculty and students craft their stories. I co-created the Story Mile Project with Mubadala, the Sharjah Institute for Heritage and the Abu Dhabi Music & Arts Festival. Forty stories were exhibited at the 2013 festival, then became a permanent exhibition at Khalifa Park; *The Story Mile* book (ISBN 978-9948-20-117-5), which I edited, was published in 2014. 300 student authors took part. (The National, 13 Mar 2013, wrongly says Al Musallam led the club.)
- **UNESCO Mongolia Kamishibai Program (Akita International University, 2005–2006).** Principal Investigator and Steering Committee Chair of a two-year, $30,000 UNESCO/Japan Funds-in-Trust grant. 40+ faculty and students took part at AIU and the University of the Humanities (Ulaanbaatar). K-12 students in Mongolia and Japan joined too. I directed the documentary team. [Improved artwork and a new story coming; Japanese stories to be added.]
- **Peace Studies Seminar on Cambodia (Miyazaki, Fall 2003).** A 15-week, certificate-bearing seminar I co-created with 11 faculty, embassy staff from Cambodia and Japan, plus NGO staff. It served 200+ students and community members. I led a student trip to Phnom Penh and Siem Reap.

### 6.4 AI Projects

Cards for Pure Intellect Tutor, Pure Intellect Analyzer and AI Ranking App. Each card: title, one-line purpose, my role, tools, screenshot and link. **Ask me for the purpose, screenshots and links for each.** Add other Claude Code projects only when I name them.

### 6.5 Contact / CV

- Email: jeff@jeffreymaggard.com
- LinkedIn: https://www.linkedin.com/in/jeff-maggard-a01181b3
- No CV on the site, ever (Jeffrey's decision, to protect his identity).
- Line: Open to instructional design, curriculum and university teaching roles.

### 6.6 Education and languages (About section on Teaching or Contact page)

- M.A., Applied Linguistics: TESOL, Portland State University. Thesis: "Academic ESL: Semantic Mapping and Lexical Acquisition."
- B.A., English Literature, and Certificate in Black Studies, Portland State University.
- Languages: English (native); Spanish (CEFR B1+); Japanese (CEFR A2).

(Omit graduation years.)

---

## 7. Asset checklist

| Asset | Status | Where it goes |
|---|---|---|
| Portrait photo (Jeff_Maggard_Portrait) | Have it; Jeffrey will add it to the project | Home hero (grayscale) |
| Animated falcon film | In Jeffrey's Claude Code video project | Home card 3, Cultural Projects |
| Character Guide images | On Jeffrey's design canvas | Cultural Projects |
| Textbook cover | Needed | Home card 2, ID page |
| Shared-course website or student work | None survive; use a designed graphic | Home card 1 |
| Kamishibai art | Jeffrey is improving it | Home card 4, Cultural Projects |
| App screenshots and links | Needed | Home card 5, AI Projects |
| ENGL 203 syllabus preview | Needed | Home card 6, ID page |
| Story Mile photos | Needed | Cultural Projects |
| CV PDF | Needed | Contact |

---

## 8. Open items [CHECK]

- Purposes, links and screenshots for each AI app.
- Which Claude Code projects to add to AI Projects.
- A graphic for the shared first-year course (none of the original materials survive).
