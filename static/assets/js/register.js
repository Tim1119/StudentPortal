function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Button for the User it disables for bad or invalid input
const submitButton = document.getElementById('submitbtn')



const usernameSuccessOutput = document.getElementById('usernameSuccessOutput')
const usernameFeedBackArea = document.getElementById('username-invalid-feedback')
const usernameField = document.getElementById('yourUsername');
    usernameField.addEventListener('keyup', function (e) {
    const usernameVal = e.target.value;
    usernameSuccessOutput.style.display = 'block'
    usernameSuccessOutput.textContent = `Checking ${usernameVal}`

    usernameField.classList.remove('is-invalid')

    if (usernameVal.length > 0 ){

        fetch('/accounts/validate-username/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                username: usernameVal,
            })
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            usernameSuccessOutput.style.display = 'none'
            submitButton.disabled = true
            console.log({'data':data})
            if (data.username_error) {
                usernameField.classList.add('is-invalid')
                usernameFeedBackArea.innerHTML = `<p>${data.username_error}</p>`
            }else{
                submitButton.removeAttribute('disabled')
            }
                     
        })        
    }
    if(usernameVal.length <= 0 ){
        usernameSuccessOutput.style.display = 'none'
    }
})


const emailSuccessOutput = document.getElementById('emailSuccessOutput');
const emailFeedbackArea = document.getElementById('email-invalid-feedback')
const emailField = document.getElementById('yourEmail');
    emailField.addEventListener('keyup', function (e) {


    const emailVal = e.target.value

    emailSuccessOutput.style.display = 'block'
    emailSuccessOutput.textContent = `Checking ${emailVal}`
    emailField.classList.remove('is-invalid')
   
    
    
    if (emailVal.length > 0){
        fetch('/accounts/validate-email/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                email:emailVal,
            })
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            emailSuccessOutput.style.display = 'none'
            console.log({'data':data})
            if (data.email_error) {
                // diable buton if emailis invalid
                submitButton.disabled = true
                emailField.classList.add('is-invalid')
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`
            }else{
                submitButton.removeAttribute('disabled')
            }
                     
        })        
    }
    if (emailVal.length <= 0){
        emailSuccessOutput.style.display = 'none',
        emailField.classList.remove('is-invalid')
    }
})

// Implementing toggle password field
const showPasswordToggle = document.getElementById('showpasswordtoggle');
const passwordField2 = document.getElementById("yourPassword2");
const passwordField = document.getElementById('yourPassword');

showPasswordToggle.addEventListener('click',function(e){
    if (showPasswordToggle.textContent === 'show password'){
        showPasswordToggle.textContent = 'hide password' 

        passwordField.setAttribute("type","text")
        passwordField2.setAttribute("type","text")
    }
    else{
        showPasswordToggle.textContent = 'show password';
        passwordField.setAttribute("type","password")
        passwordField2.setAttribute("type","password")
    }
})

