const loginForm = document.getElementById("login-form");
const registerForm = document.getElementById("reg-form");
const showRegisterLink = document.getElementById("show-reg");
const showLoginLink = document.getElementById("show-login");

showRegisterLink.addEventListener("click", (e) => {
    e.preventDefault();
    loginForm.classList.remove("form--active");
    registerForm.classList.add("form--active");
});

showLoginLink.addEventListener("click", (e) => {
    e.preventDefault();
    registerForm.classList.remove("form--active");
    loginForm.classList.add("form--active");
});