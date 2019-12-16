var selectedID = "target";
var inputID = "search-field"; 
var targetInitialHTML;
var targetContentCheck = 0; 
function stripTags( string ) {
        "use strict"; 
        var re = /<[^>]+>/ig;
        
            
        var match = [], mask = [], space = " ", exe, spacer;
        while ( (exe = re.exec(string)) !== null ){
            spacer = [];
            match.push(exe);
            while (spacer.length !== exe[0].length) { spacer.push(space); }
            mask.push(spacer.join(""));
        }


        for (var i = 0; i < match.length; i++) {
            string = string.replace(match[i], mask[i]);
        }

        return string;

    }


    var highlightClass = "highlightjs",
        highlightRe = new RegExp(highlightClass,"ig"),
        spaceRe = /\s+/,
        spaceRe2 = /\s+$/,
        before = "<span style=\"display: inline-block; position: relative;\"><span class=\"" + highlightClass + "\" style=\"display: block; background: yellow; box-shadow: 0px 0px 1px rgb(120,120,120);\">", 
        after = "</span></span>",
        contentError = "The ID selector '" + selectedID + "' does not exist in the DOM. Please define a valid ID selector in the user settings of the script and reload the page.";
    

   function highlightProcess( tag , content , term ) {

            var block = document.getElementById( tag );

            if (highlightRe.test( block.innerHTML )) {
                
                block.innerHTML = content;
                
            }
            
          
            if ( term.length < 2 ) { 
                
                return;
            
           
            } else {
               
              
                var re = new RegExp(term,"ig");
               
               
                var start = [];
                var end =[];
                var match;

              
                while ((match = re.exec(stripTags(content))) !== null) {
                    start.push(match.index);
                    end.push(match.index + term.length);
                }
                
               
                if (start.length!==0) {
                    
                   
                    start = start.reverse();
                    end = end.reverse();
                    
                 
                    var wordArray = content.split("");
                    
                 
                    for (var k = 0; k < start.length; k++) {
                        wordArray.splice(end[k], 0, after);
                        wordArray.splice(start[k], 0, before);
                    }
                 
                    block.innerHTML = wordArray.join("");
                  
                    var tabIdx = document.getElementsByClassName( highlightClass );
                    for (var i = 0; i < tabIdx.length; i++) {
                        tabIdx[i].setAttribute('tabindex', i+2);
                    }

                }

            } 
   
  document.getElementById(selectedID).innerHTML = targetInitialHTML;
  setup();
} 