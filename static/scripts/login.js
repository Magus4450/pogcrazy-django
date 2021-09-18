const login = document.getElementById('login')
const recover = document.getElementById('recover')
const backToLogin = document.querySelector('#recover .login-signup a')
const forgot = document.querySelector('#login .login-form #forgot span')

forgot.addEventListener('click', ()=> {

    login.classList.remove('form-out')
    recover.classList.remove('form-in')

    login.classList.add('form-out')
    setTimeout(()=>{
        login.style.display = 'none'
        recover.style.display = 'flex'
        recover.classList.add('form-in')
    }, 1000)

})
backToLogin.addEventListener('click', ()=> {

    login.classList.remove('form-out')
    recover.classList.remove('form-in')

    recover.classList.add('form-out')
    setTimeout(()=>{
        recover.style.display = 'none'
        login.style.display = 'flex'
        login.classList.add('form-in')
    }, 1000)

})

