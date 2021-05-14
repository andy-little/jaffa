

window.onload = () => {
    const red = document.querySelector('#red');
    const imgHeight = red.offsetHeight;

    window.addEventListener('scroll', () => {
        red.style.height = `${imgHeight - window.pageYOffset}px`;
        
    });
};