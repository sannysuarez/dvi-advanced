document.addEventListener('DOMContentLoaded', function() {
    // Function to generate a username from the user's full name
    function generateUsername(fullName) {
        const nameParts = fullName.trim().split(' ');
        const firstName = nameParts[0] || '';
        const lastName = nameParts[nameParts.length - 1] || ''; // Get the last name in case of multiple names

        // Get the first 3 letters of the first name
        const firstPart = firstName.substring(0, 3).toLowerCase();

        // Get the first 3 or 4 letters of the last name
        const lastPart = lastName.length >= 4 ? lastName.substring(0, 4).toLowerCase() : lastName.substring(0, 3).toLowerCase();

        // Generate random 4 digits
        const randomDigits = Math.floor(1000 + Math.random() * 9000); // Random 4-digit number

        // Combine parts to form the username
        return `${firstPart}${lastPart}${randomDigits}`;
    }

    // Event listener for the 'full_name' input field
    document.getElementById('full_name').addEventListener('input', function() {
        const fullName = this.value.trim(); // Get the full name entered by the user

        if (fullName) {
            const generatedUsername = generateUsername(fullName); // Generate username
            document.getElementById('username').value = generatedUsername; // Set the generated username to the 'username' input field
        } else {
            // Clear the username field if the full name input is empty
            document.getElementById('username').value = '';
        }
    });
});
