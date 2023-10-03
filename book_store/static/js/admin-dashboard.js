const deleteModal = document.getElementById("delete-modal"),
    deleteBtns = document.getElementsByClassName("btn__delete"),
    closeModal = document.getElementById("btn-close"),
    cancelBtn = document.getElementById("btn-cancel"),
    addBtn = document.getElementById("btn-add"),
    closeAddModal = document.getElementById("add-modal-close-btn"),
    addModal = document.getElementById("add-modal");

    



        

[...deleteBtns].forEach(deleteBtn => {
    deleteBtn.onclick = function () {
        deleteModal.style.display = "block";
    }
});

window.onclick = function(event) {
    if (event.target == deleteModal || event.target == addModal ) {
        deleteModal.style.display = "none";
        addModal.style.display = "none";
    }       
}

closeModal.onclick = function () {
    deleteModal.style.display = "none";
}

closeAddModal.onclick = function () {
    addModal.style.display = "none";
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

// script delete book 
const deleteIds = document.getElementsByClassName("btn__delete");
const confirmationDelete = document.getElementById("confirmation-delete");

[...deleteIds].forEach(element => {
    element.addEventListener('click', () => {
        confirmationDelete.value = element.value;
    })
})

