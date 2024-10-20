const fullname = localStorage.getItem("fullname")
const email = localStorage.getItem("email")

document.getElementById("final-fullname").innerText = fullname;
document.getElementById("final-email").innerText = email;

fetch('http://127.0.0.1:5000/send_ticket', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        fullname: fullname,
        email: email
    })
})
.then(response => response.json())
.then(data => {
    console.log(data.status); // Should log "done"
})
.catch(error => {
    console.error('Error:', error);
})
