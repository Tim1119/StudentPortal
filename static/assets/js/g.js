emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;
  
    emailField.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";
  
    if (emailVal.length > 0) {
      fetch("/authentication/validate-email", {
        body: JSON.stringify({ email: emailVal }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("data", data);
          if (data.email_error) {
            submitBtn.disabled = true;
            emailField.classList.add("is-invalid");
            emailFeedBackArea.style.display = "block";
            emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
          } else {
            submitBtn.removeAttribute("disabled");
          }
        });
    }
  });