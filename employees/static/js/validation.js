function validateForm(event) {
    let isValid = true;
    const errorMessages = [];

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const mobile = document.getElementById("mobile").value.trim();
    const designation = document.getElementById("designation").value.trim();
    const gender = document.querySelector('input[name="gender"]:checked');
    const courses = document.querySelectorAll('input[name="courses"]:checked');

    if (!/^[a-zA-Z\s]+$/.test(name)) {
        isValid = false;
        errorMessages.push("Name must contain alphabets only.");
    }

    if (!/^\S+@\S+\.\S+$/.test(email)) {
        isValid = false;
        errorMessages.push("Please enter a valid email.");
    }

    if (!/^\d{10}$/.test(mobile)) {
        isValid = false;
        errorMessages.push("Mobile number must be exactly 10 digits.");
    }

    if (designation === "") {
        isValid = false;
        errorMessages.push("Please select a designation.");
    }

    if (!gender) {
        isValid = false;
        errorMessages.push("Please select a gender.");
    }

    if (courses.length === 0) {
        isValid = false;
        errorMessages.push("Please select at least one course.");
    }

    const errorContainer = document.getElementById("error-messages");
    errorContainer.innerHTML = "";
    if (!isValid) {
        event.preventDefault();
        errorMessages.forEach((msg) => {
            const p = document.createElement("p");
            p.style.color = "red";
            p.innerText = msg;
            errorContainer.appendChild(p);
        });
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", validateForm);
    }
});
