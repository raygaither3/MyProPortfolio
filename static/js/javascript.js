window.onload = () => {
    emailjs.init("YOUR_PUBLIC_KEY");
}

document.getElementById('contactForm').onsubmit = function(event) {
    event.preventDefault();

    emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', this)
        .then(() => {
            alert('Message sent successfully!');
        })
        .catch((error) => {
            console.error('Failed to send message:', error);
            alert('Oops! Something went wrong.');
        });
}