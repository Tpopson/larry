let body = document.querySelector('body');
let toggle = document.querySelector('.toggle');
let moon = document.querySelector('.fa-moon');

toggle.addEventListener('click', ()=>{
    body.classList.toggle('dark')
    if(body.classList.contains('dark')){
        moon.classList.replace('fa-moon', 'fa-sun')
    }else{
        moon.classList.replace('fa-sun', 'fa-moon')
    }
})