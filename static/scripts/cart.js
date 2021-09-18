const cart = document.querySelectorAll('.cart')[0]
const cartButton = document.querySelector('#cart i')
const cartCrossButton = document.querySelectorAll('.cart-head-button')[0]

cartButton.addEventListener('click', ()=>{
    cart.style.right = "0";
})
cartCrossButton.addEventListener('click', ()=>{
    cart.style.right = "-150%";
})