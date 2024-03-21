let theFirstspan=document.querySelector(".omenText");
let imgDiv=document.querySelector(".second");
let frwrd=document.querySelector(".forward");
let bck=document.querySelector(".backward");
const omen=document.querySelector(".omenImg");
const viper=document.querySelector(".viperImg");
const agentLock=document.querySelector("button");
const abilityOne=document.querySelector(".firstAbility");
const abilitytwo=document.querySelector(".secondAbility");
const abilitythree=document.querySelector(".thirdAbility");
let viperAudio=new Audio("ViperPick.mp3.mpeg");
let omenAudio=new Audio("OmenPick.mp3.mpeg");
const theAbility=document.querySelector(".abilities");
// const theSecondspan=document.querySelector(".viper");
// const secondDiv=document.querySelector(".second");
frwrd.addEventListener("click",()=>{
    omen.src="viper full.png";
    imgDiv.style.background=' linear-gradient(90deg, rgba(39,168,80,1) 0%, rgba(25,89,16,1) 100%)';
    theFirstspan.innerText="Welcome to my world";
    abilityOne.src="2-viper-basic-ability-poison-cloud.png";
    abilityOne.style.background='green';
    abilitytwo.src="1-viper-basic-ability-snake-bite.png";
    abilitytwo.style.background='green';
    abilitythree.src="3-viper-signature-ability-toxic-screen.png";
    abilitythree.style.background='green';
})
bck.addEventListener("click",()=>{
    if(omen.src="viper full.png"){
        omen.src="omen full.png";   
    imgDiv.style.background=' linear-gradient(90deg, rgba(4,12,65,1) 0%, rgba(9,36,121,1) 57%, rgba(9,36,121,1) 75%, rgba(9,36,121,1) 97%)';
    theFirstspan.innerText="I am the begginning, I am the End!";
    abilityOne.src="3-omen-signature-ability-dark-cover.png";
    abilityOne.style.background='#2c6fa7';
    abilitytwo.src="2-omen-basic-ability-paranoia.png";
    abilitytwo.style.background='#2c6fa7';
    abilitythree.src="1-omen-basic-ability-shrouded-step.png";
    abilitythree.style.background='#2c6fa7';
 
}
})

agentLock.addEventListener("click",()=>{
    if(omen.src==viper.src){
        viperAudio.play();
    }
    else{
        omenAudio.play();
    }
})

theFirstspan.innerText="I am the begginning, I am the End!";

// theSecondspan.innerText="Welcome to my world!";
// viperAudio.volume=0.3;
// secondDiv.addEventListener("mouseover",()=>{
//     //viperAudio.play();
//     //secondDiv.style.opacity=0;
// })


//viper's abilities
//omen ka smoke!
//reyna ki abilities
//pop up bubble when hovered


