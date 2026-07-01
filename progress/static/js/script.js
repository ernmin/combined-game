document.querySelector('#userIDForm').addEventListener('submit', (event) => {
    event.preventDefault();
    submitID();
})


function submitID() {
    const userID = document.querySelector('#getID').value;
    // document.getElementById('displayResult').innerText = userID;
    fetch('/rows', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ requestedUser: userID })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('displayResult').innerText = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}



