
document.getElementById("calculator").onchange = function(){
    var bill = document.getElementById("bill").value;
    var tip = document.getElementById("tip").value;
   
    //validate input
    if (bill == 0 && tip == 0) {
      alert("Please enter values");
      return;
    }
 
    //Calculate tip
    var total = (bill * (tip/100));
    //round to two decimal places
    total = Math.round(total * 100) / 100;
    //next line allows us to always have two digits after decimal point
    total = total.toFixed(2);
    //Display the tip

    document.getElementById("output").innerHTML = "You should tip: $" + total;
    
  }
  
   