/* document.addEventListener('DOMContentLoaded', () => {
    
    const cards = document.querySelectorAll('.card');

    cards.forEach((card) => {
        card.onclick = () => {
            if(card.classList.contains('open')){
                card.classList.remove('open');
            } else {
                cards.forEach((cCard) => {
                    cCard.classList.remove('open');
                })
                card.classList.add('open');
            }
        }
    })
});
 */