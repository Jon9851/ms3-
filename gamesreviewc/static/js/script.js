 document.addEventListener("DOMContentLoaded", function() {
 // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

// Drop Down initialization

    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
    
    collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);
    
 //delete modal initialization
    let modal = document.querySelectorAll('.modal');
    M.Modal.init(modal);
});

//  image Slider
var slides = document.querySelectorAll('.slide');
var buttons = document.querySelectorAll('.btn');
let currentSlide = 1;

//Autoplay Image Slider 
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
