const addressForm = document.getElementsByClassName('address-form')[0];
const addressBtn = document.querySelector('.add-ress button');
const closeBtn = document.getElementById('form-btn');
const overlay = document.getElementById('mobile-overlay');
const classEdit = document.getElementsByClassName('')

addressBtn.addEventListener('click', ()=> {
    overlay.style.display = 'block';
    addressForm.style.display = 'flex';
    body.classList.add('noscroll');

    
})
closeBtn.addEventListener('click', ()=> {
    overlay.style.display = 'none';

    addressForm.style.display = 'none';
    body.classList.remove('noscroll');


})


// if (confirm('Are you sure you want to save this thing into the database?')) {
//     // Save it!
//     console.log('Thing was saved to the database.');
//   } else {
//     // Do nothing!
//     console.log('Thing was not saved to the database.');
//   }