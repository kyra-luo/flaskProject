let h1Texts = ["Profile", "Posts", "Forum"];
let logoColors = ["var(--Profile-logo)", "var(--Post-logo)", "var(--Forum-logo)"];
let keyframes = ["wave-Profile-effect", "wave-Post-effect", "wave-Forum-effect"];
let urls = ["user", "explore", "community"]; // Add your URLs here

gsap.from(".floating-image", { y: "-100vh", delay: 0.5 });
gsap.to(".floating-image img", {
    x: "random(-20, 20)",
    y: "random(-20, 20)",
    zIndex: 22,
    duration: 2,
    ease: "none",
    yoyo: true,
    repeat: -1
});

const waveEffect = document.querySelector(".wave");
const sections = document.querySelectorAll(".section");
const prevButton = document.getElementById("prevButton");
const nextButton = document.getElementById("nextButton");
const navigateButton = document.getElementById("navigateButton");
const sectionContainer = document.querySelector(".section-container");

let index = 0;
let currentIndex = 0;
let currentPosition = 0;

nextButton.addEventListener("click", () => {
    if (currentPosition > -200) {
        currentPosition -= 100;
        sectionContainer.style.left = `${currentPosition}%`;
    }
    currentIndex++;
    if (currentIndex < h1Texts.length) {
        document.querySelector(".h1").innerHTML = h1Texts[currentIndex];
    }
    gsap.to(".logo", {
        opacity: 1,
        duration: 1,
        color: logoColors[currentIndex]
    });
    gsap.from(".h1", { y: "20%", opacity: 0, duration: 0.5 });
    gsap.from(".floating-image", { y: "-100vh", delay: 0.4, duration: 0.4 });

    if (currentIndex === h1Texts.length - 1) {
        nextButton.style.display = "none";
    }
    if (currentIndex > 0) {
        prevButton.style.display = "block";
    }
    nextButton.style.color = logoColors[currentIndex + 1];
    prevButton.style.color = logoColors[currentIndex - 1];
    nextButton.style.animationName = keyframes[currentIndex + 1];
    prevButton.style.animationName = keyframes[currentIndex - 1];
});

prevButton.addEventListener("click", () => {
    if (currentPosition < 0) {
        currentPosition += 100;
        sectionContainer.style.left = `${currentPosition}%`;
        sectionContainer.style.transition = `all 0.5s ease-in-out`;
    }
    currentIndex--;
    if (currentIndex >= 0) {
        document.querySelector(".h1").innerHTML = h1Texts[currentIndex];
    }
    gsap.to(".logo", { color: logoColors[currentIndex], duration: 1 });
    gsap.from(".h1", { y: "20%", opacity: 0, duration: 0.5 });
    gsap.from(".fruit-image", { y: "100vh", delay: 0.5 });

    nextButton.style.display = "block";
    if (currentIndex === 0) {
        prevButton.style.display = "none";
    }
    nextButton.style.color = logoColors[currentIndex + 1];
    prevButton.style.color = logoColors[currentIndex - 1];
    nextButton.style.animationName = keyframes[currentIndex + 1];
    prevButton.style.animationName = keyframes[currentIndex - 1];
});

navigateButton.addEventListener("click", () => {
    if (currentIndex < urls.length) {
        window.location.href = urls[currentIndex];
    }
});
