function runClock() {
    let currentTime = new Date();
    let secondRotate = (currentTime.getSeconds() / 60) * 360;
    let minuteRotate = (currentTime.getMinutes() / 60) * 360;
    let hourRotate = ((currentTime.getHours() + (currentTime.getMinutes() / 60)) / 12) * 360;

    let secondHand = document.querySelector(".secondHand");
    let minuteHand = document.querySelector(".minuteHand");
    let hourHand = document.querySelector(".hourHand");
    secondHand.style.transform = `rotate(${secondRotate}deg) translateY(-30%)`;
    minuteHand.style.transform = `rotate(${minuteRotate}deg) translateY(-50%)`;
    hourHand.style.transform = `rotate(${hourRotate}deg) translateY(-50%)`;
}

setInterval(runClock, 1000);