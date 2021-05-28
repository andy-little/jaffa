document.addEventListener('DOMContentLoaded', () => {
    const mobHam = document.querySelector('.nav-hamburger');
    const nav = document.querySelector('nav');
    const overlay = document.querySelector('.overlay');
    mobHam.onclick = () => {
        nav.classList.toggle('open');
        overlay.classList.toggle('active');
        document.querySelector('body').classList.toggle('locked');
    } 
    const mascot = document.querySelector('.nav-mascot');
    window.addEventListener('scroll', () => {

        if (window.innerWidth > 900) {
            mascot.style.width = `calc(171px - ${pageYOffset / 9}px)`;
        } else {
            mascot.style.width = `calc(20vw - ${pageYOffset / 9}px)`;
        }

        
    });
})

