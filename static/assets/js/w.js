
const emailSuccessOutput = document.getElementById('emailSuccessOutput');
const emailFeedbackArea = document.getElementById('email-invalid-feedback')
const emailField = document.getElementById('yourEmail');
    emailField.addEventListener('keyup', function (e) {


    const emailVal = e.target.value

    emailSuccessOutput.style.display = 'block'
    emailSuccessOutput.textContent = `Checking ${emailVal}`
    emailField.classList.remove('is-invalid')

    if (emailVal.length > 0 ){

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
            //emailSuccessOutput.style.display = 'none'
            //console.log({'data':data,emailVal})
            console.log({'data':data})
            if (data.email_error) {
                emailField.classList.add('is-invalid')
                emailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`
            }
                     
        })        
    }
})