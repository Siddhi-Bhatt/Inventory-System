function openChatbot() {
  window.location.href = "your-chatbot-url.html"; // Replace with your chatbot link
}

// Canvas Background Animation
const canvas = document.getElementById("backgroundCanvas");
const ctx = canvas.getContext("2d");

let particles = [];
const particleCount = 100;
const speed = 2;

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

class Particle {
  constructor() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.z = Math.random() * canvas.width;
    this.radius = Math.random() * 2 + 1;
  }

  move() {
    this.z -= speed;
    if (this.z <= 0) {
      this.z = canvas.width;
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
    }
  }

  draw() {
    const x = (this.x - canvas.width / 2) * (canvas.width / this.z) + canvas.width / 2;
    const y = (this.y - canvas.height / 2) * (canvas.width / this.z) + canvas.height / 2;
    const radius = this.radius * (canvas.width / this.z);

    ctx.beginPath();
    ctx.arc(x, y, radius, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
    ctx.fill();
    ctx.closePath();
  }
}

function initParticles() {
  particles = [];
  for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
  }
}

function animate() {
  // Clear the canvas and fill with black
  ctx.fillStyle = "black";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  particles.forEach((particle) => {
    particle.move();
    particle.draw();
  });

  requestAnimationFrame(animate);
}

function addParticle(x, y) {
  for (let i = 0; i < 5; i++) {
    particles.push(new Particle(x, y, canvas.width));
  }
}

// Add Event Listener for Mouse Move
canvas.addEventListener("mousemove", (event) => {
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;
  addParticle(x, y);
});

window.addEventListener("resize", () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  initParticles();
});

initParticles();
animate();
