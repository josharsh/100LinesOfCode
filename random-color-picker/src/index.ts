const getRandomColor = () : String => {
    const color: String = Math.floor(Math.random()*16777215).toString(16);
    return `#${color.toUpperCase()}`;
}

const newColor: String = getRandomColor();

console.log(newColor)