const ableInputs = document.getElementById("able-inputs");

const username = document.getElementById('username_id'),
    email = document.getElementById('email_id'),
    firstName = document.getElementById('first_name_id'),
    lastName = document.getElementById('last_name_id'),
    submitEditProfile = document.getElementById('submit_profile_id'),
    userImage = document.getElementById('user_image_id');


inputs = [username, email, firstName, lastName];

ableInputs.addEventListener('click', () => {
    inputs.forEach((input) => {
        input.disabled = false;
    })
    ableInputs.style.display = 'none';
    submitEditProfile.style.display = 'block';
    userImage.style.display = 'flex';
})