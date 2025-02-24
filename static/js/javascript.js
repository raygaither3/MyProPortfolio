// window.onload = () => {
//     emailjs.init("YOUR_PUBLIC_KEY");
// }

// document.getElementById('contactForm').onsubmit = function(event) {
//     event.preventDefault();

//     emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
//         .then(() => {
//             alert('Message sent successfully!');
//         })
//         .catch((error) => {
//             console.error('Failed to send message:', error);
//             alert('Oops! Something went wrong.');
//         });
// }

document.getElementById('contactBtn').onclick = function() {
    document.getElementById('contactModal').style.display = 'block';
};

// Close the modal when the close button is clicked
document.getElementById('closeBtn').onclick = function() {
    document.getElementById('contactModal').style.display = 'none';
};

// Close the modal if the user clicks anywhere outside of the modal
window.onclick = function(event) {
    if (event.target == document.getElementById('contactModal')) {
        document.getElementById('contactModal').style.display = 'none';
    }
};

// Handle form submission
document.getElementById('contactForm').onsubmit = function(event) {
    event.preventDefault();

    const formData = {
        userEmail: document.getElementById('userEmail').value,
        userMessage: document.getElementById('userMessage').value
    };

    fetch('/send-email', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            // Show thank you message
            document.getElementById('thankYouMessage').style.display = 'block';
            // Hide the form
            document.getElementById('contactForm').reset();
            setTimeout(() => {
                document.getElementById('contactModal').style.display = 'none'; // Close modal after a few seconds
                document.getElementById('thankYouMessage').style.display = 'none'; // Hide thank you message
            }, 3000);
        } else {
            alert('Failed to send message.');
        }
    })
    .catch(error => console.error('Error:', error));
};