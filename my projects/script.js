function searchResources() {
    const searchTerm = document.querySelector(".search-container input[type='text']").value;
    if (searchTerm) {
        alert(`Searching for resources related to: ${searchTerm}`);
    } else {
        alert("Please enter a search term.");
    }
}

