function validatorRegister() {
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var password2 = document.getElementById('password-2').value;
    
    var errorMessages = {
        username: '',
        email: '',
        password: '',
        password2: ''
    };

    var usernameRegex = /^[a-zA-Zа-яА-ЯёЁіІїЇєЄ]+$/;
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    var passwordInvalidChars = /[.,\-+=]/; 

    if (username === '') {
        errorMessages.username = 'Ім’я користувача є обов’язковим.';
    } else if (!usernameRegex.test(username)) {
        errorMessages.username = 'Ім’я користувача може містити тільки букви.';
    }

    if (email === '') {
        errorMessages.email = 'Електронна пошта є обов’язковою.';
    } else if (!emailRegex.test(email)) {
        errorMessages.email = 'Невірний формат електронної пошти.';
    }

    if (password === '') {
        errorMessages.password = 'Пароль обов’язковий';
    } else if (password.length < 6) {
        errorMessages.password = 'Пароль має бути не менше 6 символів.';
    } else if (passwordInvalidChars.test(password)) {
        errorMessages.password = 'Пароль не повинен містити ., -=+= символів.';
    }

    if (password !== password2) {
        errorMessages.password2 = 'Паролі не співпадають.';
    }

    displayErrors(errorMessages);
    
    for (var key in errorMessages) {
        if (errorMessages[key] !== '') {
            return false;
        }
    }
    return true;
}

function displayErrors(errors) {
    for (var field in errors) {
        var errorElementId = field + '_error';
        var errorMessageElement = document.getElementById(errorElementId);
        
        if (errors[field] !== '') {
            if (!errorMessageElement) {
                var newErrorMessageElement = document.createElement('div');
                newErrorMessageElement.id = errorElementId;
                newErrorMessageElement.className = 'text-danger';
                newErrorMessageElement.innerText = errors[field];
                document.getElementById(field).parentNode.appendChild(newErrorMessageElement);
            } else {
                errorMessageElement.innerText = errors[field];
            }
        } else if (errorMessageElement) {
            errorMessageElement.remove();
        }
    }
}
