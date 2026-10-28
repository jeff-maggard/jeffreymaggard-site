/* 3D motion headers. One canvas per .hero3d-band; the scene comes from data-scene.
   Scenes: globe, blocks, rings, dunes, paper, network. Needs THREE (r128) loaded first. */
(function () {
  if (!window.THREE) return;
  var T = window.THREE;
  var BLUE = new T.Color('#29ABFF');
  var VIOLET = new T.Color('#9A76FF');
  var WHITE = new T.Color('#FFFFFF');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function randDir() {
    var u = Math.random() * 2 - 1, th = Math.random() * Math.PI * 2, r = Math.sqrt(1 - u * u);
    return new T.Vector3(r * Math.cos(th), u, r * Math.sin(th));
  }

  function mix(t) { return BLUE.clone().lerp(VIOLET, Math.min(1, Math.max(0, t))); }

  function pointsMaterial(size, opacity) {
    return new T.PointsMaterial({ size: size, vertexColors: true, transparent: true, opacity: opacity, depthWrite: false, sizeAttenuation: true });
  }

  function lineMat(color, opacity) {
    return new T.LineBasicMaterial({ color: color, transparent: true, opacity: opacity });
  }

  // ---------------------------------------------------------------- scenes
  var SCENES = {};

  // Globe of light with arcs between the places Jeffrey has taught and built programs.
  SCENES.globe = function (scene, camera) {
    camera.position.set(0, 0, 6.2);
    var g = new T.Group();
    g.position.x = 1.7;
    g.rotation.x = 0.35;
    scene.add(g);
    var R = 2;
    var n = 1600, pos = [], col = [];
    for (var i = 0; i < n; i++) {
      var y = 1 - (i / (n - 1)) * 2, r = Math.sqrt(1 - y * y), th = i * 2.399963;
      pos.push(Math.cos(th) * r * R, y * R, Math.sin(th) * r * R);
      var c = mix((y + 1) / 2); col.push(c.r, c.g, c.b);
    }
    var geo = new T.BufferGeometry();
    geo.setAttribute('position', new T.Float32BufferAttribute(pos, 3));
    geo.setAttribute('color', new T.Float32BufferAttribute(col, 3));
    g.add(new T.Points(geo, pointsMaterial(0.035, 0.85)));

    function ll(lat, lon, rad) {
      var phi = (90 - lat) * Math.PI / 180, the = (lon + 180) * Math.PI / 180;
      return new T.Vector3(-rad * Math.sin(phi) * Math.cos(the), rad * Math.cos(phi), rad * Math.sin(phi) * Math.sin(the));
    }
    var places = [[36.2, 138.3], [31.9, 131.4], [39.7, 140.1], [44.4, -69.0], [45.5, -122.7], [47.9, 106.9], [11.6, 104.9], [24.5, 54.4], [25.3, 51.5]];
    var marks = new T.Group(); g.add(marks);
    places.forEach(function (p) {
      var m = new T.Mesh(new T.SphereGeometry(0.045, 12, 12), new T.MeshBasicMaterial({ color: WHITE }));
      m.position.copy(ll(p[0], p[1], R * 1.01)); marks.add(m);
      var halo = new T.Mesh(new T.RingGeometry(0.07, 0.095, 24), new T.MeshBasicMaterial({ color: BLUE, transparent: true, opacity: 0.8, side: T.DoubleSide }));
      halo.position.copy(m.position); halo.lookAt(0, 0, 0); marks.add(halo);
    });
    var links = [[0, 3], [3, 4], [0, 5], [5, 6], [0, 8], [8, 7], [1, 3], [2, 5], [6, 8], [4, 0]];
    var arcs = links.map(function (l, k) {
      var a = ll(places[l[0]][0], places[l[0]][1], R), b = ll(places[l[1]][0], places[l[1]][1], R);
      var mid = a.clone().add(b).multiplyScalar(0.5); mid.setLength(R + 0.35 + a.distanceTo(b) * 0.35);
      var curve = new T.QuadraticBezierCurve3(a, mid, b);
      var pts = curve.getPoints(80);
      var ag = new T.BufferGeometry().setFromPoints(pts);
      var line = new T.Line(ag, lineMat(k % 2 ? VIOLET : BLUE, 0.9));
      g.add(line);
      return { line: line, offset: k * 0.37 };
    });
    var ring = new T.Mesh(new T.TorusGeometry(2.75, 0.012, 8, 160), new T.MeshBasicMaterial({ color: VIOLET, transparent: true, opacity: 0.55 }));
    ring.rotation.x = 1.25; g.add(ring);
    var ring2 = new T.Mesh(new T.TorusGeometry(3.1, 0.006, 8, 160), new T.MeshBasicMaterial({ color: BLUE, transparent: true, opacity: 0.35 }));
    ring2.rotation.x = 1.05; ring2.rotation.y = 0.4; g.add(ring2);
    return function (t) {
      g.rotation.y = t * 0.12;
      ring.rotation.z = t * 0.2;
      arcs.forEach(function (a) {
        var p = ((t * 0.35 + a.offset) % 1.6) / 1.2;
        a.line.geometry.setDrawRange(0, Math.floor(Math.min(1, p) * 81));
        a.line.material.opacity = p > 1 ? Math.max(0, 1 - (p - 1) * 2.5) : 0.9;
      });
    };
  };

  // A living course map: modules rising and falling in waves.
  SCENES.blocks = function (scene, camera) {
    camera.position.set(6, 6.5, 8); camera.lookAt(2.2, 0, 0);
    var g = new T.Group(); g.position.x = 2.4; scene.add(g);
    var cols = 12, rows = 8, cells = [];
    var box = new T.BoxGeometry(0.7, 1, 0.7); box.translate(0, 0.5, 0);
    var edges = new T.EdgesGeometry(box);
    for (var x = 0; x < cols; x++) for (var z = 0; z < rows; z++) {
      var c = mix(x / cols);
      var fill = new T.Mesh(box, new T.MeshBasicMaterial({ color: c, transparent: true, opacity: 0.12 }));
      var line = new T.LineSegments(edges, lineMat(c, 0.9));
      var cell = new T.Group(); cell.add(fill); cell.add(line);
      cell.position.set((x - cols / 2) * 0.9, 0, (z - rows / 2) * 0.9);
      g.add(cell); cells.push({ g: cell, x: x, z: z, fill: fill });
    }
    var path = [];
    for (var i = 0; i <= 60; i++) { var u = i / 60; path.push(new T.Vector3((u - 0.5) * cols * 0.9, 2.6 + Math.sin(u * 6) * 0.25, Math.sin(u * 9) * 2)); }
    g.add(new T.Line(new T.BufferGeometry().setFromPoints(path), lineMat(WHITE, 0.6)));
    return function (t) {
      cells.forEach(function (c) {
        var h = 0.25 + (Math.sin(c.x * 0.6 + t * 1.2) * 0.5 + 0.5) * (Math.cos(c.z * 0.7 + t * 0.8) * 0.5 + 0.5) * 1.9;
        c.g.scale.y = h;
        c.fill.material.opacity = 0.06 + h * 0.1;
      });
      g.rotation.y = Math.sin(t * 0.15) * 0.25;
    };
  };

  // Concentric orbiting rings with travelling knowledge points.
  SCENES.rings = function (scene, camera) {
    camera.position.set(0, 0, 7);
    var g = new T.Group(); g.position.x = 2; scene.add(g);
    var rings = [];
    for (var i = 0; i < 6; i++) {
      var r = 0.8 + i * 0.42;
      var m = new T.Mesh(new T.TorusGeometry(r, i === 2 ? 0.022 : 0.012, 10, 180), new T.MeshBasicMaterial({ color: i === 2 ? new T.Color('#BFE3FF') : mix(i / 5), transparent: true, opacity: i === 2 ? 0.9 : 0.7 }));
      m.rotation.x = 0.9 + i * 0.18; m.rotation.y = i * 0.35;
      var dot = new T.Mesh(new T.SphereGeometry(0.07, 14, 14), new T.MeshBasicMaterial({ color: i % 2 ? VIOLET : BLUE }));
      var holder = new T.Group(); holder.add(m); dot.position.x = r; holder.add(dot);
      holder.rotation.copy(m.rotation); m.rotation.set(0, 0, 0);
      g.add(holder); rings.push({ h: holder, speed: 0.15 + i * 0.05, dir: i % 2 ? -1 : 1 });
    }
    var core = new T.Mesh(new T.IcosahedronGeometry(0.42, 1), new T.MeshBasicMaterial({ color: BLUE, wireframe: true }));
    g.add(core);
    var dust = new T.BufferGeometry(), dp = [], dc = [];
    for (var k = 0; k < 500; k++) { var v = randDir().multiplyScalar(1.5 + Math.random() * 2.5); dp.push(v.x, v.y, v.z); var c = mix(Math.random()); dc.push(c.r, c.g, c.b); }
    dust.setAttribute('position', new T.Float32BufferAttribute(dp, 3)); dust.setAttribute('color', new T.Float32BufferAttribute(dc, 3));
    var dustPts = new T.Points(dust, pointsMaterial(0.03, 0.6)); g.add(dustPts);
    return function (t) {
      rings.forEach(function (r) { r.h.rotation.z = t * r.speed * r.dir; });
      core.rotation.y = t * 0.4; core.rotation.x = t * 0.2;
      dustPts.rotation.y = t * 0.03;
    };
  };

  // Desert dunes of light, a sun ring and a gliding falcon (from the folktale film).
  SCENES.dunes = function (scene, camera) {
    camera.position.set(0, 1.3, 6); camera.lookAt(0, 0.1, -2);
    var W = 160, D = 70, geo = new T.BufferGeometry(), pos = new Float32Array(W * D * 3), col = [];
    for (var x = 0; x < W; x++) for (var z = 0; z < D; z++) {
      var i = (x * D + z) * 3; pos[i] = (x / W - 0.5) * 18; pos[i + 2] = -z * 0.22 + 2;
      var c = mix(z / D); col.push(c.r, c.g, c.b);
    }
    geo.setAttribute('position', new T.BufferAttribute(pos, 3));
    geo.setAttribute('color', new T.Float32BufferAttribute(col, 3));
    scene.add(new T.Points(geo, pointsMaterial(0.055, 1)));
    var sun = new T.Mesh(new T.TorusGeometry(1.3, 0.05, 12, 160), new T.MeshBasicMaterial({ color: WHITE }));
    sun.position.set(3.6, 1.9, -9); scene.add(sun);
    var halo = new T.Mesh(new T.TorusGeometry(1.7, 0.012, 8, 160), new T.MeshBasicMaterial({ color: VIOLET, transparent: true, opacity: 0.6 }));
    halo.position.copy(sun.position); scene.add(halo);
    // falcon: two wing strokes and a body
    var bird = new T.Group();
    var wingGeo = new T.BufferGeometry().setFromPoints([new T.Vector3(0, 0, 0), new T.Vector3(-0.35, 0.1, 0), new T.Vector3(-0.75, 0.02, 0)]);
    var lw = new T.Line(wingGeo, lineMat(WHITE, 1)), rw = new T.Line(wingGeo, lineMat(WHITE, 1));
    rw.scale.x = -1; bird.add(lw); bird.add(rw);
    bird.add(new T.Line(new T.BufferGeometry().setFromPoints([new T.Vector3(0, 0.03, 0.15), new T.Vector3(0, 0, -0.35)]), lineMat(WHITE, 1)));
    bird.scale.setScalar(1.1); scene.add(bird);
    return function (t) {
      for (var x = 0; x < W; x++) for (var z = 0; z < D; z++) {
        var i = (x * D + z) * 3, px = pos[i], pz = pos[i + 2];
        pos[i + 1] = Math.sin(px * 0.45 + t * 0.5) * 0.45 + Math.sin(pz * 0.6 + px * 0.2 + t * 0.3) * 0.35 - 0.6;
      }
      geo.attributes.position.needsUpdate = true;
      halo.rotation.z = t * 0.2;
      var a = t * 0.25;
      bird.position.set(Math.cos(a) * 2.6 + 2, 1.5 + Math.sin(t * 0.8) * 0.2, Math.sin(a) * 1.2 - 1);
      bird.rotation.y = -a + Math.PI / 2;
      var flap = Math.sin(t * 5) * 0.35; lw.rotation.z = flap; rw.rotation.z = -flap;
    };
  };

  // Paper theater: story cards floating out of a kamishibai frame.
  SCENES.paper = function (scene, camera) {
    camera.position.set(0, 0.5, 7.5);
    var g = new T.Group(); g.position.x = 2.2; g.rotation.y = -0.45; scene.add(g);
    var frame = new T.LineSegments(new T.EdgesGeometry(new T.BoxGeometry(3.2, 2.3, 0.4)), lineMat(WHITE, 0.95));
    g.add(frame);
    var doorL = new T.LineSegments(new T.EdgesGeometry(new T.BoxGeometry(1.1, 2.3, 0.05)), lineMat(BLUE, 0.9));
    doorL.position.set(-2.15, 0, 0.35); doorL.rotation.y = 0.7; g.add(doorL);
    var doorR = doorL.clone(); doorR.material = lineMat(VIOLET, 0.9); doorR.position.x = 2.15; doorR.rotation.y = -0.7; g.add(doorR);
    var cards = [];
    for (var i = 0; i < 7; i++) {
      var c = mix(i / 6);
      var card = new T.Group();
      card.add(new T.Mesh(new T.PlaneGeometry(2.6, 1.8), new T.MeshBasicMaterial({ color: c, transparent: true, opacity: 0.14, side: T.DoubleSide })));
      card.add(new T.LineSegments(new T.EdgesGeometry(new T.PlaneGeometry(2.6, 1.8)), lineMat(c, 0.9)));
      g.add(card); cards.push(card);
    }
    return function (t) {
      cards.forEach(function (card, i) {
        var p = ((t * 0.12 + i / cards.length) % 1);
        card.position.set(-p * 4.5, Math.sin(p * Math.PI) * 1.4 + (p - 0.5) * 0.4, p * 3.2);
        card.rotation.set(Math.sin(p * 3) * 0.3, p * 1.4, p * 0.4);
        card.children[0].material.opacity = 0.18 * (1 - p);
        card.children[1].material.opacity = 0.95 * (1 - p * 0.9);
      });
      g.rotation.y = -0.45 + Math.sin(t * 0.2) * 0.12;
    };
  };

  // Neural network: nodes, links and travelling pulses.
  SCENES.network = function (scene, camera) {
    camera.position.set(0, 0, 8);
    var g = new T.Group(); g.position.x = 2.2; scene.add(g);
    var nodes = [], N = 90;
    for (var i = 0; i < N; i++) nodes.push(randDir().multiplyScalar(1 + Math.random() * 2.4));
    var np = [], nc = [];
    nodes.forEach(function (v, i) { np.push(v.x, v.y, v.z); var c = mix(i / N); nc.push(c.r, c.g, c.b); });
    var ng = new T.BufferGeometry(); ng.setAttribute('position', new T.Float32BufferAttribute(np, 3)); ng.setAttribute('color', new T.Float32BufferAttribute(nc, 3));
    g.add(new T.Points(ng, pointsMaterial(0.12, 1)));
    var lp = [], pairs = [];
    for (var a = 0; a < N; a++) for (var b = a + 1; b < N; b++) if (nodes[a].distanceTo(nodes[b]) < 1.15) { lp.push(nodes[a].x, nodes[a].y, nodes[a].z, nodes[b].x, nodes[b].y, nodes[b].z); pairs.push([a, b]); }
    var lg = new T.BufferGeometry(); lg.setAttribute('position', new T.Float32BufferAttribute(lp, 3));
    g.add(new T.LineSegments(lg, lineMat(BLUE, 0.28)));
    var pulses = [];
    for (var k = 0; k < 24; k++) {
      var m = new T.Mesh(new T.SphereGeometry(0.05, 10, 10), new T.MeshBasicMaterial({ color: k % 2 ? WHITE : VIOLET }));
      g.add(m); pulses.push({ m: m, pair: pairs[(k * 37) % pairs.length], off: k * 0.13 });
    }
    return function (t) {
      g.rotation.y = t * 0.1; g.rotation.x = Math.sin(t * 0.15) * 0.2;
      pulses.forEach(function (p, i) {
        var u = (t * 0.6 + p.off) % 1;
        if (u < 0.02) p.pair = pairs[(Math.floor(t * 10) * 13 + i * 31) % pairs.length];
        p.m.position.lerpVectors(nodes[p.pair[0]], nodes[p.pair[1]], u);
      });
    };
  };


  // Cartoon making: a film strip of frames sweeping past, an onion-skin falcon flapping, keyframes on a curve.
  SCENES.animation = function (scene, camera) {
    camera.position.set(0, 0.4, 8);
    var g = new T.Group(); g.position.x = 0.6; scene.add(g);
    var path = new T.CatmullRomCurve3([new T.Vector3(-7, -0.6, -3), new T.Vector3(-3.5, 0.3, 0), new T.Vector3(0, 0.6, 1.2), new T.Vector3(3.5, 0.3, 0), new T.Vector3(7, -0.6, -3)]);
    function wing(flap, color, opacity) {
      var b = new T.Group();
      var pts = [new T.Vector3(-0.9, 0.15 + flap, 0), new T.Vector3(-0.4, 0.12 + flap * 0.5, 0), new T.Vector3(0, 0, 0), new T.Vector3(0.4, 0.12 + flap * 0.5, 0), new T.Vector3(0.9, 0.15 + flap, 0)];
      b.add(new T.Line(new T.BufferGeometry().setFromPoints(new T.CatmullRomCurve3(pts).getPoints(30)), lineMat(color, opacity)));
      b.add(new T.Line(new T.BufferGeometry().setFromPoints([new T.Vector3(0, 0.02, 0), new T.Vector3(0, -0.35, 0)]), lineMat(color, opacity)));
      return b;
    }
    var frames = [], N = 16;
    for (var i = 0; i < N; i++) {
      var f = new T.Group(), c = mix(i / (N - 1));
      f.add(new T.LineSegments(new T.EdgesGeometry(new T.PlaneGeometry(1.3, 0.9)), lineMat(c, 0.95)));
      f.add(new T.Mesh(new T.PlaneGeometry(1.3, 0.9), new T.MeshBasicMaterial({ color: c, transparent: true, opacity: 0.08, side: T.DoubleSide })));
      for (var k = 0; k < 5; k++) for (var side = -1; side <= 1; side += 2) {
        var hole = new T.LineSegments(new T.EdgesGeometry(new T.PlaneGeometry(0.12, 0.08)), lineMat(WHITE, 0.55));
        hole.position.set(-0.52 + k * 0.26, side * 0.57, 0); f.add(hole);
      }
      var bird = wing(Math.sin(i * 0.8) * 0.35, WHITE, 0.95); bird.scale.setScalar(0.42); f.add(bird);
      g.add(f); frames.push(f);
    }
    // big onion-skin falcon above the strip
    var onion = new T.Group(); onion.position.set(1.6, 2.2, 0); g.add(onion);
    var ghosts = [];
    for (var j = 0; j < 6; j++) { var w = wing(0, j === 0 ? WHITE : (j % 2 ? BLUE : VIOLET), j === 0 ? 1 : 0.5 - j * 0.07); w.position.x = -j * 0.45; w.scale.setScalar(1.7); onion.add(w); ghosts.push(w); }
    // keyframe curve with diamond keys
    var kp = []; for (var q = 0; q <= 80; q++) { var u = q / 80; kp.push(new T.Vector3((u - 0.5) * 7, -2.3 + Math.sin(u * 7) * 0.25, 0.5)); }
    g.add(new T.Line(new T.BufferGeometry().setFromPoints(kp), lineMat(VIOLET, 0.8)));
    [0, 0.25, 0.5, 0.75, 1].forEach(function (u) {
      var d = new T.Mesh(new T.PlaneGeometry(0.14, 0.14), new T.MeshBasicMaterial({ color: WHITE, side: T.DoubleSide }));
      d.position.set((u - 0.5) * 7, -2.3 + Math.sin(u * 7) * 0.25, 0.5); d.rotation.z = Math.PI / 4; g.add(d);
    });
    return function (t) {
      frames.forEach(function (f, i) {
        var u = (i / N + t * 0.035) % 1;
        f.position.copy(path.getPointAt(u));
        var tan = path.getTangentAt(u);
        f.rotation.set(0, -tan.x * 0.25 + (u - 0.5) * -1.1, 0);
      });
      ghosts.forEach(function (w, j) {
        var flap = Math.sin(t * 4 - j * 0.6) * 0.4;
        w.children[0].geometry.dispose();
        var pts = [new T.Vector3(-0.9, 0.15 + flap, 0), new T.Vector3(-0.4, 0.12 + flap * 0.5, 0), new T.Vector3(0, 0, 0), new T.Vector3(0.4, 0.12 + flap * 0.5, 0), new T.Vector3(0.9, 0.15 + flap, 0)];
        w.children[0].geometry = new T.BufferGeometry().setFromPoints(new T.CatmullRomCurve3(pts).getPoints(30));
      });
      onion.position.y = 2.2 + Math.sin(t * 0.8) * 0.15;
    };
  };

  // ---------------------------------------------------------------- runner
  function start(band) {
    var name = band.getAttribute('data-scene');
    if (!SCENES[name]) return;
    var canvas = band.querySelector('canvas.hero3d');
    var renderer;
    try { renderer = new T.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true }); } catch (e) { return; }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    var scene = new T.Scene();
    scene.fog = new T.Fog(0x16181D, 9, 22);
    var camera = new T.PerspectiveCamera(45, 1, 0.1, 100);
    var update = SCENES[name](scene, camera);
    var baseX = camera.position.x, baseY = camera.position.y, mx = 0, my = 0;
    var target = camera.getWorldDirection(new T.Vector3()).add(camera.position);

    function resize() {
      var w = band.clientWidth, h = band.clientHeight;
      renderer.setSize(w, h, false);
      camera.aspect = w / h;
      // On narrow screens, center the scene behind the text
      scene.children.forEach(function (c) { if (c.isGroup && c.userData.baseX === undefined) c.userData.baseX = c.position.x; if (c.isGroup) c.position.x = w < 760 ? 0 : c.userData.baseX; });
      camera.updateProjectionMatrix();
    }
    resize();
    window.addEventListener('resize', resize);
    band.addEventListener('pointermove', function (e) {
      var r = band.getBoundingClientRect();
      mx = (e.clientX - r.left) / r.width - 0.5; my = (e.clientY - r.top) / r.height - 0.5;
    });

    var visible = true, t0 = performance.now();
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { visible = es[0].isIntersecting; }).observe(band);
    function frame(now) {
      var t = reduce ? 6 : (now - t0) / 1000;
      update(t);
      camera.position.x += (baseX + mx * 0.6 - camera.position.x) * 0.05;
      camera.position.y += (baseY - my * 0.4 - camera.position.y) * 0.05;
      camera.lookAt(target);
      renderer.render(scene, camera);
    }
    if (reduce) { frame(0); return; }
    (function loop(now) { if (visible && !document.hidden) frame(now); requestAnimationFrame(loop); })(t0);
    band.classList.add('is-3d');
  }

  document.querySelectorAll('.hero3d-band').forEach(start);
})();
