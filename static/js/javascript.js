// Show the contact modal when the contact button is clicked
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
            // Reset the form
            document.getElementById('contactForm').reset();
            setTimeout(() => {
                document.getElementById('contactModal').style.display = 'none'; // Close modal after a few seconds
                document.getElementById('thankYouMessage').style.display = 'none'; // Hide thank you message
            }, 3000);
        } else {
            alert('Failed to send message.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Oops! Something went wrong.');
    });
};

// Show video modal when a video card is clicked
document.querySelectorAll('.video-card').forEach(card => {
    card.onclick = function() {
        const videoSrc = this.getAttribute('data-video-src');
        const videoModal = document.getElementById('videoModal');
        const videoElement = document.getElementById('modalVideo');
        
        videoElement.src = videoSrc;
        videoModal.style.display = 'block';
    };
});

// Close the video modal when the close button is clicked
document.getElementById('videoCloseBtn').onclick = function() {
    const videoModal = document.getElementById('videoModal');
    const videoElement = document.getElementById('modalVideo');
    
    videoModal.style.display = 'none';
    videoElement.src = ''; // Stop the video when modal closes
};

// Close the modal if the user clicks anywhere outside of the modal
window.onclick = function(event) {
    const videoModal = document.getElementById('videoModal');
    if (event.target == videoModal) {
        videoModal.style.display = 'none';
        document.getElementById('modalVideo').src = '';
    }
};