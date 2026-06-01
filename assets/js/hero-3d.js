/**
 * SKY UNITED Hero 3D Shield Animation
 * Three.js powered premium 3D scene
 */

const HeroScene = (() => {
  let scene, camera, renderer;
  let outerShield, middleShield, innerShield;
  let glowRing;
  let mouseX = 0, mouseY = 0;
  let targetRotationX = 0, targetRotationY = 0;
  let particles = [];

  const config = {
    colors: {
      silver: 0xC0C0C0,
      blue: 0x4875A0,
      gold: 0xD4AF37,
      white: 0xFFFFFF
    },
    rotation: {
      outerSpeed: 0.0015,
      middleSpeed: -0.001,
      innerSpeed: 0.0008
    }
  };

  function init() {
    const canvas = document.getElementById('hero-3d-canvas');
    if (!canvas) return false;

    // Scene setup
    scene = new THREE.Scene();
    scene.background = null;

    // Camera
    const width = canvas.parentElement.clientWidth;
    const height = canvas.parentElement.clientHeight;
    camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
    camera.position.z = 5;

    // Renderer
    renderer = new THREE.WebGLRenderer({
      canvas,
      alpha: true,
      antialias: true,
      precision: 'highp',
      preserveDrawingBuffer: true
    });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.2;

    // Lighting
    setupLights();

    // Shields
    createShields();

    // Glow ring
    createGlowRing();

    // Particles
    createParticles();

    // Events
    window.addEventListener('resize', onWindowResize);
    document.addEventListener('mousemove', onMouseMove);
    window.addEventListener('scroll', onScroll);

    // Initial animation
    animateIn();

    // Start animation loop
    animate();

    return true;
  }

  function setupLights() {
    // Ambient light
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);

    // Directional light (gold warmth)
    const dirLight = new THREE.DirectionalLight(0xD4AF37, 0.8);
    dirLight.position.set(5, 3, 5);
    scene.add(dirLight);

    // Point light (blue accent)
    const pointLight = new THREE.PointLight(0x4875A0, 0.6);
    pointLight.position.set(-4, 2, 4);
    scene.add(pointLight);

    // Back light (rim)
    const rimLight = new THREE.DirectionalLight(0xffffff, 0.3);
    rimLight.position.set(-5, 0, -5);
    scene.add(rimLight);
  }

  function createShields() {
    // Outer Shield (Silver)
    const outerGeometry = new THREE.IcosahedronGeometry(3, 5);
    const outerMaterial = new THREE.MeshStandardMaterial({
      color: config.colors.silver,
      metalness: 0.85,
      roughness: 0.15,
      envMapIntensity: 1
    });
    outerShield = new THREE.Mesh(outerGeometry, outerMaterial);
    outerShield.rotation.z = Math.PI / 8;
    outerShield.castShadow = true;
    scene.add(outerShield);

    // Middle Shield (Blue)
    const middleGeometry = new THREE.IcosahedronGeometry(2.3, 5);
    const middleMaterial = new THREE.MeshStandardMaterial({
      color: config.colors.blue,
      metalness: 0.7,
      roughness: 0.25,
      envMapIntensity: 0.8
    });
    middleShield = new THREE.Mesh(middleGeometry, middleMaterial);
    middleShield.position.z = 0.2;
    middleShield.castShadow = true;
    scene.add(middleShield);

    // Inner Shield (Gold) - with emission
    const innerGeometry = new THREE.IcosahedronGeometry(1.6, 5);
    const innerMaterial = new THREE.MeshStandardMaterial({
      color: config.colors.gold,
      emissive: config.colors.gold,
      emissiveIntensity: 0.25,
      metalness: 0.95,
      roughness: 0.05,
      envMapIntensity: 1.2
    });
    innerShield = new THREE.Mesh(innerGeometry, innerMaterial);
    innerShield.position.z = 0.4;
    innerShield.castShadow = true;
    scene.add(innerShield);
  }

  function createGlowRing() {
    const ringGeometry = new THREE.TorusGeometry(3.5, 0.1, 16, 100);
    const ringMaterial = new THREE.MeshBasicMaterial({
      color: config.colors.gold,
      transparent: true,
      opacity: 0.4
    });
    glowRing = new THREE.Mesh(ringGeometry, ringMaterial);
    glowRing.rotation.x = Math.PI / 6;
    glowRing.position.z = -0.5;
    scene.add(glowRing);
  }

  function createParticles() {
    const particleCount = 12;
    const geometry = new THREE.BufferGeometry();
    const positions = [];

    for (let i = 0; i < particleCount; i++) {
      const angle = (i / particleCount) * Math.PI * 2;
      const radius = 6;
      positions.push(
        Math.cos(angle) * radius,
        Math.sin(angle) * radius,
        (Math.random() - 0.5) * 4
      );

      particles.push({
        startX: Math.cos(angle) * radius,
        startY: Math.sin(angle) * radius,
        startZ: (Math.random() - 0.5) * 4,
        progress: 0
      });
    }

    geometry.setAttribute('position', new THREE.BufferAttribute(new Float32Array(positions), 3));

    const material = new THREE.PointsMaterial({
      color: config.colors.gold,
      size: 0.15,
      transparent: true,
      opacity: 0.6,
      sizeAttenuation: true
    });

    const points = new THREE.Points(geometry, material);
    points.userData.geometry = geometry;
    points.userData.material = material;
    scene.add(points);
  }

  function animateIn() {
    // Fade in shields
    gsap.fromTo(outerShield.scale,
      { x: 0, y: 0, z: 0 },
      { x: 1, y: 1, z: 1, duration: 1, ease: 'back.out' }
    );
    gsap.fromTo(middleShield.scale,
      { x: 0, y: 0, z: 0 },
      { x: 1, y: 1, z: 1, duration: 1, ease: 'back.out', delay: 0.15 }
    );
    gsap.fromTo(innerShield.scale,
      { x: 0, y: 0, z: 0 },
      { x: 1, y: 1, z: 1, duration: 1, ease: 'back.out', delay: 0.3 }
    );

    // Particle animation
    gsap.to(particles, {
      progress: 1,
      duration: 2,
      ease: 'power2.inOut',
      onUpdate: updateParticlePositions
    });
  }

  function updateParticlePositions() {
    if (!scene.children.find(c => c.geometry && c.geometry.attributes.position)) return;

    const pointsObject = scene.children.find(c => c.isPoints);
    if (!pointsObject) return;

    const positions = pointsObject.geometry.attributes.position.array;

    particles.forEach((p, i) => {
      const progress = p.progress;
      const easeProgress = 1 - Math.pow(1 - progress, 3); // ease-out cubic

      positions[i * 3] = gsap.utils.interpolate(p.startX, 0, easeProgress);
      positions[i * 3 + 1] = gsap.utils.interpolate(p.startY, 0, easeProgress);
      positions[i * 3 + 2] = gsap.utils.interpolate(p.startZ, 0, easeProgress);
    });

    pointsObject.geometry.attributes.position.needsUpdate = true;
  }

  function animate() {
    requestAnimationFrame(animate);

    // Continuous rotation
    outerShield.rotation.y += config.rotation.outerSpeed;
    outerShield.rotation.x += config.rotation.outerSpeed * 0.5;

    middleShield.rotation.y += config.rotation.middleSpeed;
    middleShield.rotation.x += config.rotation.middleSpeed * 0.5;

    innerShield.rotation.y += config.rotation.innerSpeed;
    innerShield.rotation.x += config.rotation.innerSpeed * 0.5;

    // Glow ring rotation
    glowRing.rotation.z += 0.001;

    // Pulsing glow intensity
    const pulse = Math.sin(Date.now() * 0.0025) * 0.15 + 0.25;
    innerShield.material.emissiveIntensity = pulse;
    glowRing.material.opacity = pulse * 0.4;

    // Mouse tilt smoothing
    outerShield.rotation.x += (targetRotationX - outerShield.rotation.x) * 0.05;
    outerShield.rotation.y += (targetRotationY - outerShield.rotation.y) * 0.05;

    middleShield.rotation.x += (targetRotationX * 0.7 - middleShield.rotation.x) * 0.05;
    middleShield.rotation.y += (targetRotationY * 0.7 - middleShield.rotation.y) * 0.05;

    renderer.render(scene, camera);
  }

  function onMouseMove(e) {
    mouseX = (e.clientX / window.innerWidth) * 2 - 1;
    mouseY = -(e.clientY / window.innerHeight) * 2 + 1;

    targetRotationY = mouseX * 0.5;
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
        gsap.to(scene.position, {
          z: progress * 3,
          duration: 0.1
        });
        gsap.to([outerShield.scale, middleShield.scale, innerShield.scale], {
          x: 1 - progress * 0.4,
          y: 1 - progress * 0.4,
          z: 1 - progress * 0.4,
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

// Initialize when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => HeroScene.init());
} else {
  HeroScene.init();
}
