// Add JavaScript to toggle the 'clicked' class when clicking the image
const dropdownImage = document.querySelector('.dropdown img');
if (dropdownImage) {
    dropdownImage.addEventListener('click', function() {
        const dropdown = this.parentElement;
        if (dropdown.classList.contains('clicked')) {
            dropdown.classList.remove('clicked');
        } else {
            dropdown.classList.add('clicked');
        }
    });
}


console.log("hello");
