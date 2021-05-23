document.addEventListener('DOMContentLoaded', () => {
    const mobHam = document.querySelector('.nav-hamburger');
    const nav = document.querySelector('nav');
    const overlay = document.querySelector('.overlay');
    mobHam.onclick = () => {
        nav.classList.toggle('open');
        overlay.classList.toggle('active');
        document.querySelector('body').classList.toggle('locked');
    } 
})