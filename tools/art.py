"""Line-art thumbnails: one SVG motif per project, vermilion and white on near-black."""
O = "url(#gb)"   # blue-to-violet gradient
W = "#FFFFFF"   # white
G = "rgba(255,255,255,0.07)"   # dot texture

def frame(inner, label):
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="{G}"/>' for x in range(40, 800, 40) for y in range(40, 500, 40))
    return (f'<svg viewBox="0 0 800 500" role="img" aria-label="{label}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">'
            f'<defs><linearGradient id="gb" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="800" y2="500"><stop offset="0" stop-color="#29ABFF"/><stop offset="1" stop-color="#9A76FF"/></linearGradient>'
            f'<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4DA3FF"/><stop offset="1" stop-color="#7C5CFC"/></linearGradient></defs>'
            f'<rect width="800" height="500" fill="#16181D"/>{dots}'
            f'<rect x="30" y="70" width="12" height="360" rx="6" fill="url(#bar)" opacity=".9"/>{inner}</svg>')

def s(color, w=6):
    return f'fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'

MOTIFS = {
"animation": lambda: (
    # storyboard panels with a falcon flapping across them (onion-skin), film-strip perforations, a keyframe curve
    "".join(f'<rect x="{110+i*205}" y="95" width="180" height="125" rx="10" {s(W if i!=1 else O,5)}/>' for i in range(3))
    + "".join(f'<path d="M{200+i*205-48} {160-a} Q{200+i*205-22} {150-a*1.6} {200+i*205} {165} Q{200+i*205+22} {150-a*1.6} {200+i*205+48} {160-a}" {s(O if i!=1 else W,5)}/>' for i,a in enumerate([18,-4,12]))
    + "".join(f'<rect x="{95+i*42}" y="{y}" width="22" height="14" rx="3" fill="{W}" opacity=".85"/>' for i in range(15) for y in (255, 300))
    + f'<rect x="85" y="245" width="640" height="78" rx="8" {s(W,3)}/>'
    + f'<path d="M110 420 C200 340 280 470 380 400 S560 340 690 410" {s(O,5)}/>'
    + "".join(f'<rect x="{x-9}" y="{y-9}" width="18" height="18" transform="rotate(45 {x} {y})" fill="{W}"/>' for x,y in [(110,420),(380,400),(690,410)])),
"exchange": lambda: (
    f'<circle cx="230" cy="270" r="110" {s(W)}/><ellipse cx="230" cy="270" rx="45" ry="110" {s(W,4)}/><path d="M120 270h220M135 215h190M135 325h190" {s(W,4)}/>'
    f'<circle cx="570" cy="270" r="110" {s(O)}/><ellipse cx="570" cy="270" rx="45" ry="110" {s(O,4)}/><path d="M460 270h220M475 215h190M475 325h190" {s(O,4)}/>'
    f'<path d="M260 150 Q400 20 540 150" {s(W,5)} stroke-dasharray="4 16"/><circle cx="540" cy="150" r="9" fill="{O}"/><circle cx="260" cy="150" r="9" fill="{W}"/>'),
"book": lambda: (
    f'<rect x="250" y="110" width="300" height="60" rx="8" {s(W)}/><rect x="230" y="180" width="340" height="60" rx="8" {s(O)}/><rect x="250" y="250" width="300" height="60" rx="8" {s(W)}/>'
    + "".join(f'<rect x="{180+i*76}" y="370" width="60" height="18" rx="9" fill="{O if i==3 else "none"}" stroke="{W if i!=3 else O}" stroke-width="4"/>' for i in range(6))
    + f'<text x="{180+3*76+30}" y="425" fill="{O}" font-family="sans-serif" font-weight="800" font-size="22" text-anchor="middle">B1+</text>'),
"falcon": lambda: (
    f'<circle cx="400" cy="250" r="170" {s(O)}/>'
    f'<path d="M230 250 Q320 170 390 230 Q410 180 470 175 Q450 200 455 215 Q520 190 590 205 Q520 235 470 245 Q455 300 400 330 Q410 290 390 265 Q320 300 230 250Z" {s(W,5)}/>'
    f'<circle cx="462" cy="196" r="5" fill="{O}"/>'),
"kamishibai": lambda: (
    f'<rect x="230" y="110" width="340" height="250" rx="10" {s(W)}/><path d="M230 110l-60 30v220l60 0M570 110l60 30v220l-60 0" {s(W,4)}/>'
    f'<rect x="265" y="145" width="270" height="180" rx="6" {s(O)}/><path d="M285 300 l70-80 50 50 40-40 70 70" {s(O,5)}/><circle cx="470" cy="190" r="20" {s(W,4)}/>'
    f'<path d="M300 400h200M340 430h120" {s(W,5)}/>'),
"tutor": lambda: (
    f'<path d="M190 130h300a30 30 0 0 1 30 30v110a30 30 0 0 1-30 30H300l-60 50v-50h-50a30 30 0 0 1-30-30V160a30 30 0 0 1 30-30z" {s(W)}/>'
    f'<text x="340" y="250" fill="{O}" font-family="sans-serif" font-weight="800" font-size="120" text-anchor="middle">?</text>'
    f'<path d="M420 280h190a30 30 0 0 1 30 30v70a30 30 0 0 1-30 30h-20v40l-50-40H420a30 30 0 0 1-30-30v-70a30 30 0 0 1 30-30z" {s(O)}/><path d="M440 330h150M440 365h100" {s(O,5)}/>'),
"course-map": lambda: (
    f'<path d="M120 380 C220 380 220 150 320 150 S420 350 520 350 S620 140 690 140" {s(W,5)} stroke-dasharray="2 14"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="34" fill="#16181D" stroke="{O if i in (0,4) else W}" stroke-width="6"/><text x="{x}" y="{y+9}" fill="{O if i in (0,4) else W}" font-family="sans-serif" font-weight="800" font-size="26" text-anchor="middle">{i+1}</text>'
              for i,(x,y) in enumerate([(120,380),(320,150),(440,285),(520,350),(690,140)]))),
"timeline": lambda: (
    "".join(f'<rect x="{110+i*40}" y="{380-(40+i*16)}" width="24" height="{40+i*16}" rx="6" fill="{O if i in (4,9,14) else "none"}" stroke="{O if i in (4,9,14) else W}" stroke-width="4"/>' for i in range(15))
    + f'<path d="M100 400h610" {s(W,4)}/>'),
"lessons": lambda: (
    "".join(f'<circle cx="{150+c*62}" cy="{100+r*27}" r="8" fill="{O if (c+r)%7==0 else "none"}" stroke="{O if (c+r)%7==0 else W}" stroke-width="3"/>' for c in range(9) for r in range(12))),
"assessment": lambda: (
    f'<rect x="200" y="90" width="400" height="320" rx="14" {s(W)}/>'
    + "".join(f'<rect x="240" y="{130+i*65}" width="36" height="36" rx="6" {s(O if i<3 else W,5)}/><path d="M{290} {148+i*65}h{250-i*30}" {s(W,5)}/>' for i in range(4))
    + "".join(f'<path d="M248 {147+i*65}l9 10 16-20" {s(O,5)}/>' for i in range(3))),
"story-mile": lambda: (
    f'<path d="M80 420 C200 420 180 300 300 300 S420 180 520 180 S640 80 720 80" {s(W,8)}/><path d="M80 420 C200 420 180 300 300 300 S420 180 520 180 S640 80 720 80" fill="none" stroke="#16181D" stroke-width="2" stroke-dasharray="14 14"/>'
    + "".join(f'<path d="M{x} {y}v-50l34 14-34 14" {s(O,5)}/>' for x,y in [(180,390),(330,295),(470,200),(640,110)])),
"tales": lambda: (
    f'<path d="M400 140 Q300 100 180 120v250q120-20 220 20 100-40 220-20V120q-120-20-220 20z" {s(W)}/><path d="M400 140v250" {s(W,4)}/>'
    + "".join(f'<path d="M210 {170+i*40}h150" {s(O,5)}/>' for i in range(5)) + "".join(f'<path d="M440 {170+i*40}h150" {s(W,5)}/>' for i in range(5))),
"seminar": lambda: (
    f'<circle cx="400" cy="300" r="60" {s(O)}/><circle cx="400" cy="300" r="120" {s(W,4)}/><circle cx="400" cy="300" r="180" {s(W,3)} stroke-dasharray="3 14"/>'
    + "".join(f'<circle cx="{400+120*__import__("math").cos(a)}" cy="{300+120*__import__("math").sin(a)}" r="10" fill="{O}"/>' for a in [i*0.5236 for i in range(12)])),
"video-course": lambda: (
    f'<rect x="170" y="110" width="460" height="270" rx="16" {s(W)}/><path d="M370 190v110l95-55z" fill="{O}" stroke="{O}" stroke-width="6" stroke-linejoin="round"/>'
    + "".join(f'<rect x="{190+i*60}" y="410" width="40" height="26" rx="4" {s(W,3)}/>' for i in range(8))),
"motion": lambda: (
    "".join(f'<rect x="{100+i*20}" y="{250-h}" width="10" height="{2*h}" rx="5" fill="{O if 12<=i<=19 else W}"/>' for i,h in enumerate([20,40,70,50,90,120,80,60,100,140,110,70,150,170,130,160,120,90,140,110,70,90,50,80,40,60,30,20,40,25,15]))),
"analyzer": lambda: (
    "".join(f'<rect x="{180+c*110}" y="{110+r*70}" width="90" height="50" rx="8" fill="{O if (r,c) in [(0,3),(1,2),(2,3),(3,1)] else "none"}" stroke="{O if (r,c) in [(0,3),(1,2),(2,3),(3,1)] else W}" stroke-width="4"/>' for r in range(4) for c in range(4))),
}

def svg(motif, label):
    return frame(MOTIFS[motif](), label)
