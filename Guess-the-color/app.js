const makeColorValue = () => {
	return Math.round(Math.random() * 255);
};

function setButtonColor(button, red, green, blue) {
	button.setAttribute(
		'style',
		`background-color: rgb(${red},${green},${blue});`
	);
}
const makeColors = () => {
	let buttons = document.getElementsByClassName('colorButton');
	let anwserButton = Math.round(Math.random() * (buttons.length - 1));
	var answerMessage = document.getElementById('answer');

	for (let i = 0; i < buttons.length; i++) {
		let red = makeColorValue();
		let green = makeColorValue();
		let blue = makeColorValue();

		if (green === red) {
			while (green === red) {
				green = makeColorValue();
			}
		}
		if (blue === red || green) {
			while (blue === red || green) {
				blue = makeColorValue();
			}
		}

		setButtonColor(buttons[i], red, green, blue);

		if (i == anwserButton) {
			heading.innerHTML = `(${red}, ${green}, ${blue})`;
		}

		buttons[i].addEventListener('click', function () {
			if (this == buttons[anwserButton]) {
				answerMessage.innerHTML = 'Chính xác!';
			} else if (this != buttons[anwserButton]) {
				answerMessage.innerHTML = 'Chưa đúng roài!';
			}
		});
	}
};

function startGame() {
	let heading;
	let resetButton = document.getElementsByClassName('resetButton');
	heading = document.getElementById('colorValue');
	makeColorValue();
	setButtonColor();
	makeColors();
}

module.exports = {
	startGame,
	makeColorValue,
	makeColors,
	setButtonColor,
};
