const loginForm = document.getElementById("login-form");
const registerForm = document.getElementById("reg-form");
const showRegisterLink = document.getElementById("show-reg");
const showLoginLink = document.getElementById("show-login");
const titleLogin = document.getElementById("title-login");
const titleRegister = document.getElementById("title-register");

showRegisterLink.addEventListener("click", (e) => {
    e.preventDefault();
    loginForm.classList.remove("form--active");
    registerForm.classList.add("form--active");
    titleLogin.classList.remove("title--active");
    titleRegister.classList.add("title--active");
});

showLoginLink.addEventListener("click", (e) => {
    e.preventDefault();
    registerForm.classList.remove("form--active");
    loginForm.classList.add("form--active");
    titleRegister.classList.remove("title--active");
    titleLogin.classList.add("title--active");
});