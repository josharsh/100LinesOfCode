let expression;
let firstVal = true;
let output_win = document.getElementsByClassName('output-win')[0];

const getkey = (key)=>{
        if(firstVal){
                if(key == '='){
                        output_win.innerHTML = "INVALID OPERATION";
                        expression = "";
                        firstVal = true;
                }
                else{
                        expression = key;
                        output_win.innerHTML = key; 
                        firstVal = false;
                }
        }
        else{
                if(key != '='){
                        expression += key;
                        output_win.innerHTML = expression; 
                }        
                else{
                        try{
                                let result = eval(expression).toString();
                                output_win.innerHTML = result;
                                expression = result; 
                                firstVal = false; 
                        }
                        catch(err){
                                output_win.innerHTML = "INVALID OPERATION";
                                expression = "";
                                firstVal = true;
                        }
                }
        }
}

const getClr = ()=>{
        output_win.innerHTML = "";
        expression = "";
        firstVal = true;
}

const leftPar = ()=>{
        lp =  document.getElementById('btn-leftPar').value;
        if(firstVal){
                expression = lp;
                output_win.innerHTML = lp;
                firstVal = false;
        } else {
                expression += lp;
                output_win.innerHTML = expression;
        }
}
const rightPar = ()=>{
        rp =  document.getElementById('btn-rightPar').value;
        if(firstVal){
                expression = rp;
                output_win.innerHTML = rp;
                firstVal = false;
        } else {
                expression += rp;
                output_win.innerHTML = expression;
        }
}

const getDecimal = ()=>{
        if(expression == "" || expression == undefined || firstVal){
                expression = "0.";
                output_win.innerHTML = "0.";
                firstVal = false;
        }
        else{
                
                let lastOperatorIndex = Math.max(expression.lastIndexOf('+'), expression.lastIndexOf('-'), 
                                               expression.lastIndexOf('*'), expression.lastIndexOf('/'),
                                               expression.lastIndexOf('('));
                let currentNumber = expression.substring(lastOperatorIndex + 1);
                
                if(!currentNumber.includes('.')){
                        expression += ".";
                        output_win.innerHTML = expression;
                }
        }
}