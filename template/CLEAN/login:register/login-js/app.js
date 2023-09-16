document.addEventListener("DOMContentLoaded", function() {
    const mainDiv = document.querySelector(".main");
    setTimeout(() => {
        mainDiv.classList.add("active");
    }, 1000); // Delay for 1 second (adjust as needed)
});
