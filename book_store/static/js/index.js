"use client";

let toggle = document.getElementById('toggle-register');
let body = document.querySelector('body');

toggle.addEventListener('click', function () {
    body.classList.toggle('open');
})




const carousel = document.getElementById("carousel-p");
const content = document.getElementById("content-p");

const carouselBestSeller = document.getElementById("carousel-bs");
const contentBestSeller = document.getElementById("content-bs");

const nextPopular = document.getElementById("right-p");
const prevPopular = document.getElementById("left-p");

const nextBestSeller = document.getElementById("right-bs");
const prevBestSller = document.getElementById("left-bs");


const carouselFunction = (carouselId, contentId, next, prev) => {
    const gap = 15;

    next.addEventListener("click", e => {
        carouselId.scrollBy(width + gap, 0);
        if (carouselId.scrollWidth !== 0) {
            prev.style.display = "flex";
        }
        if (contentId.scrollWidth - width - gap <= carouselId.scrollLeft + width) {
            next.style.display = "none";
        }
    });

    prev.addEventListener("click", e => {
        
        carouselId.scrollBy(-(width + gap), 0);
        if (carouselId.scrollLeft - width - gap <= 0) {
            prev.style.display = "none";
        }
        if (!contentId.scrollWidth - width - gap <= carouselId.scrollLeft + width) {
            next.style.display = "flex";
        }
    });
    
    let width = carouselId.offsetWidth;
    window.addEventListener("resize", e => (width = carouselId.offsetWidth));
}

carouselFunction(carousel, content, nextPopular, prevPopular);
carouselFunction(carouselBestSeller, contentBestSeller, nextBestSeller, prevBestSller);

