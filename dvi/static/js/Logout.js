// Open the popup
function openLogoutPopup(event) {
    event.preventDefault();
    document.getElementById('logoutPopupNav').style.display = 'block';
}

// Close the popup
function closeLogoutPopup() {
    document.getElementById('logoutPopupNav').style.display = 'none';
}

// Close the popup when clicking outside the content
function closePopupOutside(event) {
    if (event.target === document.getElementById('logoutPopupNav')) {
        closeLogoutPopup();
    }
}
