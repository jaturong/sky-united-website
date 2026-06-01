/**
 * SKY UNITED Hero Molecular Orbital Animation
 * Three.js powered 3D molecule structure with orbiting cubes
 */

const MoleculeScene = (() => {
  let scene, camera, renderer;
  let nucleus, electrons = [];
  let orbitalPaths = [];
  let bondLines = [];
  let mouseX = 0, mouseY = 0;
  let targetRotationX = 0, targetRotationY = 0;
  let time = 0;

  const config = {
    colors: {
      silver: 0xC0C0C0,
      blue: 0x4875A0,
      gold: 0xD4AF37,
      white: 0xFFFFFF
    },
    electrons: [
      { radius: 3.5, speed: 0.004, axis: 'x', color: 0xC0C0C0 },    // Silver 1
      { radius: 4.2, speed: -0.003, axis: 'y', color: 0x4875A0 },   // Blue 1
      { radius: 3.8, speed: 0.0035, axis: 'z', color: 0xD4AF37 },   // Gold 1
      { radius: 4.8, speed: -0.0032, axis: 'x', color: 0x93AECC },  // Sky Blue
      { radius: 3.2, speed: 0.0038, axis: 'y', color: 0xC0C0C0 },   // Silver 2
      { radius: 4.5, speed: -0.0033, axis: 'z', color: 0x4875A0 },  // Blue 2
      { radius: 3.9, speed: 0.0036, axis: 'x', color: 0xD4AF37 },   // Gold 2
      { radius: 4.1, speed: -0.0031, axis: 'y', color: 0x93AECC }    // Sky Blue 2
    ]
  };

  function init() {
    const canvas = document.getElementById('hero-3d-canvas');
    if (!canvas) return false;

    scene = new THREE.Scene();
    scene.background = null;

    const width = canvas.parentElement.clientWidth;
    const height = canvas.parentElement.clientHeight;
    camera = new THREE.PerspectiveCamera(60, width / height, 0.1, 1000);
    camera.position.z = 14;

    renderer = new THREE.WebGLRenderer({
      canvas,
      alpha: true,
      antialias: true,
      precision: 'highp'
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.1;

    setupLights();
    createNucleus();
    createElectrons();
    createBonds();
    createOrbitalPaths();

    window.addEventListener('resize', onWindowResize);
    document.addEventListener('mousemove', onMouseMove);
    window.addEventListener('scroll', onScroll);

    animateIn();
    animate();

    return true;
  }

  function setupLights() {
    // Ambient (เข้มขึ้น)
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    scene.add(ambientLight);

    // Key light (gold)
    const keyLight = new THREE.DirectionalLight(0xD4AF37, 1.2);
    keyLight.position.set(6, 5, 6);
    scene.add(keyLight);

    // Fill light (blue)
    const fillLight = new THREE.DirectionalLight(0x4875A0, 0.8);
    fillLight.position.set(-5, 2, -5);
    scene.add(fillLight);

    // Rim light (sky blue)
    const rimLight = new THREE.DirectionalLight(0x93AECC, 0.6);
    rimLight.position.set(0, -6, 3);
    scene.add(rimLight);

    // Back light
    const backLight = new THREE.DirectionalLight(0xffffff, 0.4);
    backLight.position.set(0, 4, -8);
    scene.add(backLight);
  }

  function createNucleus() {
    const geometry = new THREE.IcosahedronGeometry(1.2, 5);
    const material = new THREE.MeshStandardMaterial({
      color: 0xFFFFFF,
      emissive: 0xFFFFFF,
      emissiveIntensity: 0.8,
      metalness: 0.9,
      roughness: 0.1
    });
    nucleus = new THREE.Mesh(geometry, material);
    nucleus.castShadow = true;
    scene.add(nucleus);
  }

  function createElectrons() {
    config.electrons.forEach((electronConfig, index) => {
      // Cube geometry (ใหญ่ขึ้น)
      const geometry = new THREE.BoxGeometry(0.85, 0.85, 0.85);
      const material = new THREE.MeshStandardMaterial({
        color: electronConfig.color,
        emissive: electronConfig.color,
        emissiveIntensity: 0.2,
        metalness: 0.8,
        roughness: 0.2
      });

      const electron = new THREE.Mesh(geometry, material);
      electron.castShadow = true;
      electron.userData = {
        radius: electronConfig.radius,
        speed: electronConfig.speed,
        axis: electronConfig.axis,
        angle: (index / 3) * Math.PI * 2,
        config: electronConfig
      };

      scene.add(electron);
      electrons.push(electron);
    });
  }

  function createOrbitalPaths() {
    // 3 orbital planes for 8 cubes
    const orbitConfig = [
      { axis: 'x', radius: 4, color: 0xC0C0C0, rotation: { x: 0, y: 0, z: 0 } },
      { axis: 'y', radius: 4.5, color: 0x4875A0, rotation: { x: Math.PI / 3, y: 0, z: 0 } },
      { axis: 'z', radius: 4.2, color: 0xD4AF37, rotation: { x: 0, y: 0, z: Math.PI / 4 } }
    ];

    orbitConfig.forEach((config) => {
      const curve = new THREE.EllipseCurve(
        0, 0,
        config.radius, config.radius,
        0, 2 * Math.PI,
        false,
        0
      );

      const points = curve.getPoints(256);
      const geometry = new THREE.BufferGeometry().setFromPoints(points);
      const material = new THREE.LineBasicMaterial({
        color: config.color,
        transparent: true,
        opacity: 0.12,
        linewidth: 1
      });

      const line = new THREE.Line(geometry, material);
      line.rotation.x = config.rotation.x;
      line.rotation.y = config.rotation.y;
      line.rotation.z = config.rotation.z;

      scene.add(line);
      orbitalPaths.push(line);
    });
  }

  function createBonds() {
    const material = new THREE.LineBasicMaterial({
      color: 0xD4AF37,
      transparent: true,
      opacity: 0.3,
      linewidth: 1
    });

    // Central nucleus to each electron
    electrons.forEach((electron) => {
      const geometry = new THREE.BufferGeometry();
      geometry.setAttribute('position', new THREE.BufferAttribute(
        new Float32Array([0, 0, 0, 0, 0, 0]), 3
      ));

      const line = new THREE.Line(geometry, material);
      scene.add(line);
      bondLines.push({ line, electron });
    });
  }

  function animateIn() {
    // Nucleus scale in
    gsap.fromTo(nucleus.scale,
      { x: 0, y: 0, z: 0 },
      { x: 1, y: 1, z: 1, duration: 1, ease: 'back.out' }
    );

    // Electrons scale in with stagger
    electrons.forEach((electron, index) => {
      gsap.fromTo(electron.scale,
        { x: 0, y: 0, z: 0 },
        {
          x: 1, y: 1, z: 1,
          duration: 0.8,
          ease: 'back.out',
          delay: 0.15 * (index + 1)
        }
      );
    });

    // Orbital paths fade in
    orbitalPaths.forEach((path, index) => {
      gsap.fromTo(path.material,
        { opacity: 0 },
        { opacity: 0.15, duration: 1, delay: 0.3 * (index + 1) }
      );
    });
  }

  function animate() {
    requestAnimationFrame(animate);
    time += 0.016; // ~60fps

    // Update electron positions
    electrons.forEach((electron) => {
      const data = electron.userData;
      data.angle += data.speed;

      // Position based on axis
      switch (data.axis) {
        case 'x':
          electron.position.y = Math.cos(data.angle) * data.radius;
          electron.position.z = Math.sin(data.angle) * data.radius;
          break;
        case 'y':
          electron.position.x = Math.cos(data.angle) * data.radius;
          electron.position.z = Math.sin(data.angle) * data.radius;
          break;
        case 'z':
          electron.position.x = Math.cos(data.angle) * data.radius;
          electron.position.y = Math.sin(data.angle) * data.radius;
          break;
      }

      // Rotate cube
      electron.rotation.x += 0.01;
      electron.rotation.y += 0.015;
      electron.rotation.z += 0.008;

      // Pulsing glow
      const pulse = Math.sin(time * 2) * 0.15 + 0.2;
      electron.material.emissiveIntensity = pulse;
    });

    // Nucleus pulsing
    const nucleusPulse = Math.sin(time * 1.5) * 0.3 + 0.8;
    nucleus.material.emissiveIntensity = nucleusPulse;

    // Update bond lines
    bondLines.forEach(({ line, electron }) => {
      const positions = line.geometry.attributes.position.array;
      positions[3] = electron.position.x;
      positions[4] = electron.position.y;
      positions[5] = electron.position.z;
      line.geometry.attributes.position.needsUpdate = true;

      // Opacity based on distance
      const distance = electron.position.length();
      line.material.opacity = Math.max(0.1, 0.4 - distance * 0.08);
    });

    // Rotate entire scene with mouse
    scene.rotation.x += (targetRotationX - scene.rotation.x) * 0.05;
    scene.rotation.y += (targetRotationY - scene.rotation.y) * 0.05;

    renderer.render(scene, camera);
  }

  function onMouseMove(e) {
    mouseX = (e.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(e.clientY / window.innerHeight) * 2 + 1;

    targetRotationY = mouseX * 0.4;
    targetRotationX = mouseY * 0.3;
  }

  function onScroll() {
    const scrollProgress = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight);
    const heroSection = document.querySelector('.hero-section');

    if (heroSection) {
      const rect = heroSection.getBoundingClientRect();
      const inView = rect.top < window.innerHeight && rect.bottom > 0;

      if (inView) {
        const progress = 1 - (rect.bottom / window.innerHeight);

        // Scale down
        gsap.to([nucleus.scale, electrons.map(e => e.scale)], {
          x: 1 - progress * 0.5,
          y: 1 - progress * 0.5,
          z: 1 - progress * 0.5,
          duration: 0.1,
          overwrite: 'auto'
        });

        // Orbit radius shrink
        electrons.forEach((electron) => {
          electron.userData.radius *= (1 - progress * 0.01);
        });

        // Fade out
        gsap.to([nucleus.material, ...electrons.map(e => e.material)], {
          opacity: 1 - progress * 0.5,
          duration: 0.1,
          overwrite: 'auto'
        });
      }
    }
  }

  function onWindowResize() {
    const canvas = document.getElementById('hero-3d-canvas');
    if (!canvas) return;

    const width = canvas.parentElement.clientWidth;
    const height = canvas.parentElement.clientHeight;

    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  }

  return {
    init
  };
})();

// Initialize
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => MoleculeScene.init());
} else {
  MoleculeScene.init();
}
