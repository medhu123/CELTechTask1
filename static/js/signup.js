document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        document.getElementById('confirm-button').click();
        
    }
});

document.getElementById('confirm-button').addEventListener('click', function() {

    const fullname = document.getElementById('fullname').value;
    const email = document.getElementById('email').value;

    

    if (email.includes('@')) {
        localStorage.setItem("fullname",fullname);
        localStorage.setItem("email",email);
        console.log(email);

        window.location.href ="/thanks";
    }

    else{
        alert('Incorrect Email')
    }
    
});