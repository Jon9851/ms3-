document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);
});

//  image Slider
var slides = document.querySelectorAll('.slide');
var buttons = document.querySelectorAll('.btn');
let currentSlide = 1;

//Autoplay Image Slider with Navigation 
var repeat = function(activeClass){
    let active = document.getElementsByClassName('active');
    let i = 1;

    var repeater = () => {
        setTimeout(function(){
            [...active].forEach((activeSlide) => {
            activeSlide.classList.remove('active');
    });

    slides[i].classList.add('active');
    i++;

    if(slides.length == i){
        i = 0;
    }
    if(i >= slides.length){
        return;
    }
    repeater();
        }, 5000);
    }
    repeater();
}
repeat();
