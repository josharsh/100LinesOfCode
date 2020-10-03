function startGame() {
  let heading;
  let buttons = document.getElementsByClassName("colorButton");
  let resetButton = document.getElementsByClassName("resetButton");

  heading = document.getElementById("colorValue");

  function makeColorValue() {
    return Math.round(Math.random() * 255);
  }

  function setButtonColor(button, red, green, blue) {
    button.setAttribute(
      "style",
      `background-color: rgb(${red},${green},${blue});`
    );
  }

  let anwserButton = Math.round(Math.random() * (buttons.length - 1));
  console.log(anwserButton);
  var answerMessage = document.getElementById("answer");

  for (let i = 0; i < buttons.length; i++) {
    let red = makeColorValue();
    let green = makeColorValue();
    let blue = makeColorValue();

    setButtonColor(buttons[i], red, green, blue);

    if (i == anwserButton) {
      heading.innerHTML = `(${red}, ${green}, ${blue})`;
    }

    buttons[i].addEventListener("click", function () {
      if (this == buttons[anwserButton]) {
        answerMessage.innerHTML = "Chính xác!";
      } else if (this != buttons[anwserButton]) {
        answerMessage.innerHTML = "Chưa đúng roài!";
      }
    });
  }
}
