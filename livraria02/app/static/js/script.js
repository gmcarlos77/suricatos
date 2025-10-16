const loginForm = document.querySelector(".login-form");
const registerForm = document.querySelector(".register-form");
const wrapper = document.querySelector(".wrapper");
const loginTitle = document.querySelector(".title-login");
const registerTitle = document.querySelector(".title-register");
const signUpBtn = document.querySelector("#SignUpBtn");
const signInBtn = document.querySelector("#SignInBtn");

// Funções para alternar formulários (não alterei)
function loginFunction() {
    loginForm.style.left = "50%";
    loginForm.style.opacity = 1;
    registerForm.style.left = "150%";
    registerForm.style.opacity = 0;
    wrapper.style.height = "500px";
    loginTitle.style.top = "50%";
    loginTitle.style.opacity = 1;
    registerTitle.style.top = "50px";
    registerTitle.style.opacity = 0;
}

function registerFunction() {
    loginForm.style.left = "-50%";
    loginForm.style.opacity = 0;
    registerForm.style.left = "50%";
    registerForm.style.opacity = 1;
    wrapper.style.height = "580px";
    loginTitle.style.top = "-60px";
    loginTitle.style.opacity = 0;
    registerTitle.style.top = "50%";
    registerTitle.style.opacity = 1;
}

// Função para mostrar mensagem de erro
function setError(input, message) {
    const inputBox = input.parentElement;
    const errorSpan = inputBox.querySelector(".error-message");
    errorSpan.textContent = message;
    input.classList.add("error");
}

function clearError(input) {
    const inputBox = input.parentElement;
    const errorSpan = inputBox.querySelector(".error-message");
    errorSpan.textContent = "";
    input.classList.remove("error");
}

// Validação em tempo real para login
function validateLoginField(input) {
    const value = input.value.trim();

    if (!value) {
        setError(input, "Campo obrigatório");
        return false;
    }

    if (input.id === "log-email") {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            setError(input, "Email inválido");
            return false;
        }
    }

    clearError(input);
    return true;
}

// Validação em tempo real para registro
function validateRegisterField(input) {
    const value = input.value.trim();

    if (!value) {
        setError(input, "Campo obrigatório");
        return false;
    }

    if (input.id === "reg-name") {
        const nameRegex = /^[a-zA-ZÀ-ÿ\s]+$/;
        if (!nameRegex.test(value)) {
            setError(input, "Somente letras permitidas");
            return false;
        }
    }

    if (input.id === "reg-email") {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            setError(input, "Email inválido");
            return false;
        }
    }

    if (input.id === "reg-pass") {
        if (value.length < 6) {
            setError(input, "Senha deve ter pelo menos 6 caracteres");
            return false;
        }
    }

    if (input.id === "confi-pass") {
        const pass = document.getElementById("reg-pass").value.trim();
        if (value !== pass) {
            setError(input, "Senhas não coincidem");
            return false;
        }
    }

    clearError(input);
    return true;
}

// Validação completa do formulário login
function validateLogin() {
    const emailInput = document.getElementById("log-email");
    const passInput = document.getElementById("log-pass");

    const emailValid = validateLoginField(emailInput);
    const passValid = validateLoginField(passInput);

    return emailValid && passValid;
}

// Validação completa do formulário registro
function validateRegister() {
    const nameInput = document.getElementById("reg-name");
    const emailInput = document.getElementById("reg-email");
    const passInput = document.getElementById("reg-pass");
    const confPassInput = document.getElementById("confi-pass");

    const nameValid = validateRegisterField(nameInput);
    const emailValid = validateRegisterField(emailInput);
    const passValid = validateRegisterField(passInput);
    const confPassValid = validateRegisterField(confPassInput);

    return nameValid && emailValid && passValid && confPassValid;
}

// Adiciona listeners para validação em tempo real nos inputs
document.querySelectorAll(".login-form .input-field").forEach(input => {
    input.addEventListener("input", () => validateLoginField(input));
});
document.querySelectorAll(".register-form .input-field").forEach(input => {
    input.addEventListener("input", () => validateRegisterField(input));
});

signInBtn.addEventListener("click", function(e) {
    if (!validateLogin()) {
        e.preventDefault(); // só previne se não for válido
    }
});
signUpBtn.addEventListener("click", function(e) {
    if (!validateRegister()) {
        e.preventDefault();
    }
});
