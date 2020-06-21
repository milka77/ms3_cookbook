function sendMail(contactForm) {
    emailjs.send("gmail", "rosie", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            contactForm.name.value = "";
            contactForm.email.value = "";
            contactForm.message.value = "";
            document.getElementById('email-message').innerHTML = "Your message was sent succesfully!";
            document.getElementById('email-message').classList.add('email-success');
        },
        function(error) {
            document.getElementById('email-message').innerHTML = "Oops Something went wrong!";
            document.getElementById('email-message').classList.add('email-failed');
        });
    return false;
    
}