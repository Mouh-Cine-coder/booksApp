const deleteModal = document.getElementById("delete-modal"),
    deleteBtn = document.getElementById("btn-delete"),
    closeModal = document.getElementById("btn-close"),
    cancelBtn = document.getElementById("btn-cancel"),
    addBtn = document.getElementById("btn-add"),
    addModal = document.getElementById("add-modal");

    

        
deleteBtn.onclick = function () {
    deleteModal.style.display = "block";
}

window.onclick = function(event) {
    if (event.target == deleteModal) {
        deleteModal.style.display = "none";
    }       
}

closeModal.onclick = function () {
    deleteModal.style.display = "none";
}

cancelBtn.onclick = function () {
    deleteModal.style.display = "none";
}

addBtn.onclick = function () {
    addModal.style.display = "block";
}

addBtn.onclick = function () {
    addModal.style.display = "block";
}

// script for add a book
