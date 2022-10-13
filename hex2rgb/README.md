Hex to RGB Converter
======
A simple Javascript program to convert hexcode into rgb or rgba.

To convert the hexcode:
```javascript
	/**
 	* @param {string} hex - the hexcode to covert with or without "#"
 	* @param {number} alpha optional* - the alpha number
	*/
	hex2rgb(hex, alpha);

	// Examples
	hex2rgb('FFF') // rgb(255, 255, 255) expected 
	hex2rgb('#070707', 0.5) // rgba(7, 7, 7, 0.5) expected
```

To run the program users can:
* Export the function into a project (or copy and paste)
* Run the file in vscode or browser if using console.log
* Using Node: `node Hex2Rgb.js`

If using vscode you should download the [Color Highlight][extension] extension to visualize the color in the editor.

[extension]: https://marketplace.visualstudio.com/items?itemName=naumovs.color-highlight