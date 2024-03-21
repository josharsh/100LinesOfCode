let expression;
let firstVal = true;
let output_win = document.getElementsByClassName('output-win')[0];

const getkey = (key)=>{
        if(firstVal){
                if(key == '='){
                        output_win.innerHTML = "INVALID OPERATION";
                        expression = "";
                }

                else{
                        expression = key;
                        output_win.innerHTML += key;
                        firstVal = false;
                }
        }
        else{
                if(key != '='){
                        expression += key;
                        output_win.innerHTML += key;
                }        
                else{
                        try{

                                output_win.innerHTML = eval(expression).toString();                
                        }

                        catch(err){
                                output_win.innerHTML = "INVALID OPERATION";
                                expression = "";
                        }
                }
        }
}

const getClr = ()=>{
        output_win.innerHTML = "";
        expression = "";
}

const leftPar = ()=>{
        lp =  document.getElementById('btn-leftPar').value;
        output_win.innerHTML += lp;
        expression += lp;
}
const rightPar = ()=>{
        rp =  document.getElementById('btn-rightPar').value;
        output_win.innerHTML += rp;
        expression += rp;
}
