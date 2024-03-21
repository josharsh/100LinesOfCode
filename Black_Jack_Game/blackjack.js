let first_card = Math.floor(Math.random() * 13) + 1;
/*let second_card = Math.floor(Math.random() * 13) + 1;
let third_card = Math.floor(Math.random() * 13) + 1;*/
let win = false;
let cards = [first_card];
//let sum = first_card + second_card;
let sum = first_card;
let chance = false;

let starting11 = document.getElementById("starting1") + "starting game";
let message2 = document.getElementById("message1")
let message = "";
let sum2 = document.getElementById("sum1");
let numb3 = document.getElementById("numbers1");
let playing = false;



function game_starting() {
    if (sum < 21) {
        message = "New Card";
        chance = true;
    } else if (sum === 21) {
        message = "Great";
        win = true;
    } else
        message = "Out of Game";
    playing = true;

    message1.innerText = message;
    sum1.innerText = ("Sum: " + sum);
    numbers1.textContent = (numbers1.innerText + first_card + " ");
    document.getElementById("start").disabled = true;


}

function new_card() {
    if (playing == true) {
        cards.push(Math.floor(Math.random() * 13) + 1);
        sum = sum + cards[cards.length - 1];
        if (cards[cards.length - 1] === 11) {
            cards[cards.length - 1] = "J";
        }
        if (cards[cards.length - 1] === 12) {
            cards[cards.length - 1] = "Q";
        }
        if (cards[cards.length - 1] === 13) {
            cards[cards.length - 1] = "K";
        }
        if (sum >= 21) {
            document.getElementById("new_card").disabled = true;
        }


        document.getElementById("numbers1").innerText = "Cards are: ";
        for (let i = 0; i < cards.length; i++) {
            document.getElementById("numbers1").innerText = (numbers1.innerText + " " + cards[i] + " ");
        }
        // sum += third_card;
        if (sum < 21) {
            message = "New card";
        } else if (sum === 21) {
            message = "Great";
            win = true;
        } else
            message = "Out of Game";

        message1.innerText = message;
        sum1.innerText = ("Sum: " + sum);
        //numbers1.textContent = " Cards are " + first_card + " " +

    } else {
        alert(" First click on start button to play");
    }


}

function reset() {

    document.getElementById("message1").innerText = "Want to play a game";
    document.getElementById("sum1").innerText = "Sum:";
    document.getElementById("numbers1").innerText = "Numbers are";


}