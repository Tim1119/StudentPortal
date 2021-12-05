const showPasswordToggle = document.getElementById('showpasswordtoggle');
const passwordField2 = document.getElementById("id_password2");
const passwordField = document.getElementById('id_password1');

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

