// script for checkboxes
const is_popular = document.getElementById('is_popular_id'),
    is_best_seller = document.getElementById('is_best_seller_id');


is_popular.addEventListener('click', () => {
    if(is_popular.checked){
        is_popular.setAttribute('checked', false)
    }
    else{
        is_popular.setAttribute('checked', true)
    }
    
})

is_best_seller.addEventListener('click', () => {
    if(is_best_seller.checked){
        is_best_seller.setAttribute('checked', false)
    }
    else{
        is_best_seller.setAttribute('checked', true)
    }
    
})
