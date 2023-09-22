"use client"
const categoryForm = document.getElementById("category__form");
const allCategories = document.getElementById("all-categories");

allCategories.addEventListener("click", () => {
    window.location.href = "http://localhost:8000/"
    
})


// function saveScrollPosition() {
//     localStorage.setItem('scrollPosition', window.scrollY);
// }

// function restoreScrollPosition() {
//     const scrollPosition = localStorage.getItem('scrollPosition');
//     if (scrollPosition !== null) {
//         window.scrollTo(0, parseInt(scrollPosition));
//         localStorage.removeItem('scrollPosition');
//     }
// }

// window.addEventListener('beforeunload', saveScrollPosition);

// window.addEventListener('load', restoreScrollPosition);

  
  