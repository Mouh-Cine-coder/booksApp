// script for checkboxes
const is_staff = document.getElementById('is_staff'),
    is_superuser = document.getElementById('is_superuser');


    is_staff.addEventListener('click', () => {
    if(is_staff.checked){
        is_staff.setAttribute('checked', false)
    }
    else{
        is_staff.setAttribute('checked', true)
    }
    
})

is_superuser.addEventListener('click', () => {
    if(is_superuser.checked){
        is_superuser.setAttribute('checked', false)
    }
    else{
        is_superuser.setAttribute('checked', true)
    }
    
})


const ableInputs = document.getElementById("able-inputs");

const username = document.getElementById('username_id'),
    email = document.getElementById('email_id'),
    firstName = document.getElementById('first_name_id'),
    lastName = document.getElementById('last_name_id'),
    submitEditProfile = document.getElementById('submit_profile_id'),
    userImage = document.getElementById('user_image_id');


inputs = [username, email, firstName, lastName, is_staff, is_superuser];

ableInputs.addEventListener('click', () => {
    inputs.forEach((input) => {
        input.disabled = false;
    })
    ableInputs.style.display = 'none';
    submitEditProfile.style.display = 'block';
    userImage.style.display = 'flex';
})