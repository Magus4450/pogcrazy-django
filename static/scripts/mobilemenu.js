
const btn = document.querySelector("#hamburger-menu");
const mobileBtn = document.querySelector("#mobile-btn");
const mobileMenu = document.querySelector('#mobile-menu');
const mobileOverlay = document.querySelector('#mobile-overlay');
const body = document.querySelector('body');



btn.addEventListener('click', () => {

    mobileMenu.classList.remove('hidden');
    mobileOverlay.classList.remove('hidden');

    body.classList.add('noscroll');

    mobileOverlay.classList.add('mobileOverlayFadeIn');
    mobileOverlay.classList.remove('mobileOverlayFadeOut');

    mobileMenu.classList.add('mobileMenuSlideIn');
    mobileMenu.classList.remove('mobileMenuSlideOut');


})
mobileBtn.addEventListener('click', () => {

    body.classList.remove('noscroll');

    mobileOverlay.classList.remove('mobileOverlayFadeIn');
    mobileOverlay.classList.add('mobileOverlayFadeOut');
    
    mobileMenu.classList.remove('mobileMenuSlideIn');
    mobileMenu.classList.add('mobileMenuSlideOut');

    // Timeout to wait for animation to happen then hide the div
    setTimeout(()=>{
        mobileOverlay.classList.add('hidden');
        mobileMenu.classList.add('hidden');

    },500);




})