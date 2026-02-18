let expression;
let firstVal = true;
let output_win = document.getElementsByClassName('output-win')[0];

const adjustFontSize = (element) => {
        const maxWidth = element.offsetWidth;
        const text = element.textContent || element.innerText;
        const baseFontSize = 24;
        const minFontSize = 12;
        
        element.style.fontSize = baseFontSize + 'px';
        
        if (element.scrollWidth > maxWidth && text.length > 0) {
                const ratio = maxWidth / element.scrollWidth;
                let newFontSize = Math.max(minFontSize, Math.floor(baseFontSize * ratio * 0.9));
                element.style.fontSize = newFontSize + 'px';
        } else {
                element.style.fontSize = baseFontSize + 'px';
        }
};

const formatExpression = (expr) => {
        if(!expr) return expr;
        return expr.replace(/\*\*/g, '^');
};

const getkey = (key)=>{
        if(output_win.innerHTML === "INVALID OPERATION" && key != '='){
                expression = "";
                firstVal = true;
        }
        
        if(firstVal){
                if(key == '='){
                        output_win.innerHTML = "INVALID OPERATION";
                        adjustFontSize(output_win);
                        expression = "";
                        firstVal = true;
                }
                else{
                        expression = key;
                        output_win.innerHTML = formatExpression(key); 
                        adjustFontSize(output_win);
                        firstVal = false;
                }
        }
        else{
                if(key != '='){
                        expression += key;
                        output_win.innerHTML = formatExpression(expression); 
                        adjustFontSize(output_win);
                }        
                else{
                        try{
                                let result = eval(expression).toString();
                                output_win.innerHTML = result;
                                adjustFontSize(output_win);
                                expression = result; 
                                firstVal = false; 
                        }
                        catch(err){
                                output_win.innerHTML = "INVALID OPERATION";
                                adjustFontSize(output_win);
                                expression = "";
                                firstVal = true;
                        }
                }
        }
}

const getClr = ()=>{
        output_win.innerHTML = "";
        output_win.style.fontSize = 'x-large';
        expression = "";
        firstVal = true;
}

const leftPar = ()=>{
        if(output_win.innerHTML === "INVALID OPERATION"){
                expression = "";
                firstVal = true;
        }
        
        lp =  document.getElementById('btn-leftPar').value;
        if(firstVal){
                expression = lp;
                output_win.innerHTML = lp;
                adjustFontSize(output_win);
                firstVal = false;
        } else {
                expression += lp;
                output_win.innerHTML = formatExpression(expression);
                adjustFontSize(output_win);
        }
}
const rightPar = ()=>{
        if(output_win.innerHTML === "INVALID OPERATION"){
                expression = "";
                firstVal = true;
        }
        
        rp =  document.getElementById('btn-rightPar').value;
        if(firstVal){
                expression = rp;
                output_win.innerHTML = rp;
                adjustFontSize(output_win);
                firstVal = false;
        } else {
                expression += rp;
                output_win.innerHTML = formatExpression(expression);
                adjustFontSize(output_win);
        }
}

const getDecimal = ()=>{
        if(output_win.innerHTML === "INVALID OPERATION"){
                expression = "";
                firstVal = true;
        }
        
        if(expression == "" || expression == undefined || firstVal){
                expression = "0.";
                output_win.innerHTML = "0.";
                adjustFontSize(output_win);
                firstVal = false;
        }
        else{
                let tempExpr = expression.replace(/\*\*/g, '##');
                let lastOperatorIndex = Math.max(tempExpr.lastIndexOf('+'), tempExpr.lastIndexOf('-'), 
                                               tempExpr.lastIndexOf('*'), tempExpr.lastIndexOf('/'),
                                               tempExpr.lastIndexOf('('));
                let currentNumber = expression.substring(lastOperatorIndex + 1);
                
                if(!currentNumber.includes('.')){
                        expression += ".";
                        output_win.innerHTML = formatExpression(expression);
                        adjustFontSize(output_win);
                }
        }
}

const getSqrt = ()=>{
        if(output_win.innerHTML === "INVALID OPERATION"){
                expression = "";
                firstVal = true;
        }
        
        try{
                let valueToSqrt;
                if(expression == "" || expression == undefined || firstVal){
                        valueToSqrt = parseFloat(output_win.innerHTML);
                } else {
                        valueToSqrt = eval(expression);
                }
                
                if(valueToSqrt < 0 || isNaN(valueToSqrt)){
                        output_win.innerHTML = "INVALID OPERATION";
                        adjustFontSize(output_win);
                        expression = "";
                        firstVal = true;
                } else {
                        let result = Math.sqrt(valueToSqrt).toString();
                        output_win.innerHTML = result;
                        adjustFontSize(output_win);
                        expression = result;
                        firstVal = false;
                }
        }
        catch(err){
                output_win.innerHTML = "INVALID OPERATION";
                adjustFontSize(output_win);
                expression = "";
                firstVal = true;
        }
}