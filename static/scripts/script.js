
const card1 = document.querySelector('#card1 img');
const card2 = document.querySelector('#card2 img');
const card3 = document.querySelector('#card3 img');
const card4 = document.querySelector('#card4 img');

const cards = [card1, card2, card3, card4]
cards.forEach(card => {
    card.addEventListener('mouseover',() => {
        card.src = `static/images/card${cards.indexOf(card)+1}2.jpg`
    })
    card.addEventListener('mouseout', () => {
        card.src = `static/images/card${cards.indexOf(card)+1}1.jpg`
    })
});

const showcaseBanner = document.querySelectorAll('.showcase-banner')[0]
// const collectionPromo = document.querySelectorAll('.collection-promo')[0]


const promo1 = document.querySelectorAll('.promo-1')[0]
const promo2 = document.querySelectorAll('.promo-2')[0]
const promo3 = document.querySelectorAll('.promo-3')[0]
const promo4 = document.querySelectorAll('.promo-4')[0]


const collectionPromo1 = document.querySelectorAll('.collection-promo')[1]
const collectionShowcase = document.querySelectorAll('.collection-showcase')[0]
const collectionCarousel = document.querySelectorAll('.collection-carousel-main')[0]


let lastKnownScrollPosition = 0;
let ticking = false;

function fadeAnimate(scrollPos, el) {
    let pos = el.offsetTop
    if (scrollPos > pos - window.innerHeight){
        el.classList.add('fade-in')        
    }
}

document.addEventListener('scroll', function(e) {
    lastKnownScrollPosition = window.scrollY;

    if (!ticking) {
        window.requestAnimationFrame(function() {
            fadeAnimate(lastKnownScrollPosition, showcaseBanner);
            fadeAnimate(lastKnownScrollPosition, promo1);
            fadeAnimate(lastKnownScrollPosition, promo2);
            fadeAnimate(lastKnownScrollPosition, promo3);
            fadeAnimate(lastKnownScrollPosition, promo4);
            fadeAnimate(lastKnownScrollPosition, card1);
            fadeAnimate(lastKnownScrollPosition, card2);
            fadeAnimate(lastKnownScrollPosition, card3);
            fadeAnimate(lastKnownScrollPosition, card4);
            
            fadeAnimate(lastKnownScrollPosition, collectionShowcase);
            fadeAnimate(lastKnownScrollPosition, collectionPromo1);
            fadeAnimate(lastKnownScrollPosition, collectionCarousel);
            ticking = false;
        });

        ticking = true;
    }
}); 

const mw900 = window.matchMedia("(max-width: 900px)")
const mw720 = window.matchMedia("(max-width: 720px)")
const rightButton = document.getElementsByClassName('right-button')[0]
const leftButton = document.getElementsByClassName('left-button')[0]
const carouselCards = document.getElementsByClassName('bag')[0]
var perCarousel;
var length;
var totalState;
function calcPerCarousel(){
    if (mw720.matches){
        console.log("ONE")
        perCarousel = 1
        length = carouselCards.children.length
        totalState = Math.floor(length/perCarousel) - 1
    } else if (mw900.matches){
        console.log("two")

        perCarousel = 2
        length = carouselCards.children.length
        totalState = Math.floor(length/perCarousel) - 1 
    } else{
        console.log("four")

        perCarousel = 4
        length = carouselCards.children.length
        totalState = Math.floor(length/perCarousel)
    }
}
window.onload = calcPerCarousel()

console.log(perCarousel)


let carouselState = 0;



rightButton.addEventListener('click', ()=> {  
    console.log(totalState)
    console.log(carouselState)
    if (carouselState < totalState){
        console.log(`translate(-${(carouselState+1)*100}%)`)

        carouselCards.style.transform = `translate(-${(carouselState+1)*100}%)`
        carouselState += 1

    }
})

leftButton.addEventListener('click', ()=> {  
    console.log(totalState)
    console.log(carouselState)
    if (carouselState > 0){
        console.log(`translate(-${(carouselState)*100}%)`)

        carouselCards.style.transform = `translate(-${(carouselState-1)*100}%)`
        carouselState -= 1

    }
})



