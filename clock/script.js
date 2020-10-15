const deg = 6;
const hourHand = document.querySelector('.hourHand');
const minuteHand = document.querySelector('.minuteHand');
const secondHand = document.querySelector('.secondHand');


setInterval(() =>{

let day = new Date();
let hh = day.getHours() * 30;
let mm = day.getMinutes() * deg;
let ss = day.getSeconds() * deg;

hourHand.style.transform = `rotateZ(${(hh)+(mm/12)}deg)`;
minuteHand.style.transform = `rotateZ(${mm}deg)`;
secondHand.style.transform = `rotateZ(${ss}deg)`;

})

