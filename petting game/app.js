// Choses random image file from the "images" folder
function getRandomAnimal() {
    var src = "images/animal_";
    src += ( Math.floor(Math.random()*53) + ".jpg" );
    return src; 
}

var clickedTime;
var createdTime;
var reactionTime; 

// Create the image to be clicked in a random position of the screen
function makeAnimal() {
    var time=Math.random()*3000;
    
    setTimeout(function() {
        var animalPosX = Math.random()*(document.getElementById('game').clientWidth - 205);
        var animalPosY = Math.random()*(document.getElementById('game').clientHeight - 205);
        document.getElementById("animal").style.left = animalPosX + "px";
        document.getElementById("animal").style.top = animalPosY + "px";

        var animalSrc = getRandomAnimal();
        document.getElementById("animal").src = animalSrc;

        document.getElementById("animal").style.display = "block";
    
        createdTime=Date.now();
    }, time); 
}

// When clicked, the images disapears, the time the person took to click it is registered and another image is created
document.getElementById("animal").onclick=function() {
    clickedTime=Date.now();
    
    reactionTime=(clickedTime-createdTime)/1000;
    document.getElementById("printReactionTime").innerHTML="You took " + reactionTime + " seconds to pet this animal.";
    this.style.display="none";
    
    makeAnimal(); 
}
makeAnimal();