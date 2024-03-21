const passwordInput = document.getElementById("password");
const passwordStrengthList = document.getElementById("password-strength-list");
const passwordStrengthScore = document.getElementById(
    "password-strength-score"
);
const hidePasswordButton = document.getElementById("hide-password");

passwordInput.addEventListener("change", processPassword);
hidePasswordButton.addEventListener("change", changePasswordVisibility);

function processPassword(event) {
    const password = event.target.value;

    let passwordCriterias = {
        length: getLengthStrength(password),
        number: getNumberStrength(password),
        uppercase: getUppercaseStrength(password),
        lowercase: getLowercaseStrength(password),
        symbol: getSymbolStrength(password),
    };

    updateStrengthInfo(passwordCriterias);
}

function getLengthStrength(password) {
    if (password.length > 15) {
        return 20;
    } else if (password.length > 11) {
        return 13;
    } else if (password.length > 8) {
        return 6;
    } else {
        return 0;
    }
}

function getNumberStrength(password) {
    const numberRegexWeak = /(\w*\d\w*){2}/;
    const numberRegexMedium = /(\w*\d\w*){3}/;
    const numberRegexStrong = /(\w*\d\w*){4}/;

    if (numberRegexStrong.test(password)) {
        return 20;
    } else if (numberRegexMedium.test(password)) {
        return 13;
    } else if (numberRegexWeak.test(password)) {
        return 6;
    } else {
        return 0;
    }
}

function getUppercaseStrength(password) {
    const uppercaseRegexWeak = /(\w*[A-Z]\w*){2}/;
    const uppercaseRegexMedium = /(\w*[A-Z]\w*){3}/;
    const uppercaseRegexStrong = /(\w*[A-Z]\w*){4}/;

    if (uppercaseRegexStrong.test(password)) {
        return 20;
    } else if (uppercaseRegexMedium.test(password)) {
        return 13;
    } else if (uppercaseRegexWeak.test(password)) {
        return 6;
    } else {
        return 0;
    }
}

function getLowercaseStrength(password) {
    const lowercaseRegexWeak = /(\w*[a-z]\w*){2}/;
    const lowercaseRegexMedium = /(\w*[a-z]\w*){3}/;
    const lowercaseRegexStrong = /(\w*[a-z]\w*){4}/;

    if (lowercaseRegexStrong.test(password)) {
        return 20;
    } else if (lowercaseRegexMedium.test(password)) {
        return 13;
    } else if (lowercaseRegexWeak.test(password)) {
        return 6;
    } else {
        return 0;
    }
}

function getSymbolStrength(password) {
    const symbolRegexWeak = /(\w*[^A-Za-z0-9]\w*){2}/;
    const symbolRegexMedium = /(\w*[^A-Za-z0-9]\w*){3}/;
    const symbolRegexStrong = /(\w*[^A-Za-z0-9]\w*){4}/;

    if (symbolRegexStrong.test(password)) {
        return 20;
    } else if (symbolRegexMedium.test(password)) {
        return 13;
    } else if (symbolRegexWeak.test(password)) {
        return 6;
    } else {
        return 0;
    }
}

function updateStrengthInfo(criterias) {
    passwordScore =
        criterias.length +
        criterias.number +
        criterias.uppercase +
        criterias.lowercase +
        criterias.symbol;
    passwordStrengthScore.textContent = "Strength: " + passwordScore + "/100";

    passwordStrengthList.innerHTML = "";

    Object.keys(criterias).forEach((criteria) => {
        const listItem = document.createElement("li");
        strength = getStrengthByScore(criterias[criteria]);
        listItem.classList.add(stringToClass(strength), "bold");
        listItem.textContent = `${criteria.toUpperCase()}: ${strength}`;
        passwordStrengthList.appendChild(listItem);
    });
}

function getStrengthByScore(score) {
    if (score >= 20) {
        return "Strong";
    } else if (score >= 13) {
        return "Medium";
    } else if (score >= 6) {
        return "Weak";
    } else {
        return "Very Weak";
    }
}

function stringToClass(string) {
    return string.toLowerCase().replace(/ /g, "-");
}

function changePasswordVisibility(event) {
    if (event.target.checked) {
        passwordInput.type = "password";
    } else {
        passwordInput.type = "text";
    }
}
