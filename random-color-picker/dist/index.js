"use strict";
const getRandomColor = () => {
    const color = Math.floor(Math.random() * 16777215).toString(16);
    return `#${color.toUpperCase()}`;
};
const newColor = getRandomColor();
console.log(newColor);
//# sourceMappingURL=index.js.map