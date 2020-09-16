var str =
  "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.";
console.log(str.length);
var regex = /[."',-\s]/g;
var result = str.replace(regex, ' ');
var resul = result.replace(/  /g, '').toLowerCase();
var newStr = resul.split(' ');
newStr.sort();
let wordC = wordCounts(newStr);
// console.log(newStr);
function wordCounts(newStr) {
  let wordCount = [];
  let count = 1;
  newStr.forEach((word, index, newStr) => {
    if (newStr[index] == newStr[index + 1]) count++;
    else {
      wordCount.push(count);
      console.log(count + ' ' + newStr[index]);
      count = 1;
    }
  });
  return wordCount;
}
