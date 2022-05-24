document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

// Drop Down initialization

    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
    
    let collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);

});
//  text slider
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides((slideIndex += n));
}

function currentSlide1(n) {
  showSlides((slideIndex = n));
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = slides.length;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}
window.onload = function () {
  setInterval(function () {
    plusSlides(1);
  }, 3000);
};

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


