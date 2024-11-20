function generatePassword() {
    const length = 12;
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
    let password = "";
    for (let i = 0; i < length; i++) {
        password += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    document.getElementById("passwordDisplay").innerText = password;
}

function stopPassword() {
    document.getElementById("passwordDisplay").innerText = "Password generation stopped!";
}

function clearPassword() {
    document.getElementById("passwordDisplay").innerText = "";
}