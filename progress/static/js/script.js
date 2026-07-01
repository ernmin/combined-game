document.querySelector('#userIDForm').addEventListener('submit', (event) => {
    event.preventDefault();
    ID_hyper_link()
    // submitID();
})


function submitID() {
    const userID = document.querySelector('#getID').value;
    // document.getElementById('displayResult').innerText = userID;
    return fetch('/rows', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ requestedUser: userID })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('displayResult').innerHTML = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function hyper_link() {
    const rows = document.querySelectorAll('table tbody tr')

    rows.forEach(row => {
    // Select the second cell (index 1, as JavaScript is 0-indexed)
    const secondCell = row.cells[1];
    
    if (secondCell) {
        // Get the plain text URL from the cell
        const url = secondCell.textContent.trim();
        
        // Ensure the cell is not empty before creating the link
        if (url) {
            // Rewrite innerHTML as a hyperlink
            secondCell.innerHTML = `<a href="${url}" target="_blank">${url}</a>`;
        }
    }
    const links = document.querySelectorAll('a');

    links.forEach((a_tag, index) => {
    a_tag.textContent = `Photo ${index + 1}`;
});
});
}

async function ID_hyper_link() {
    await submitID();
    hyper_link();
}


