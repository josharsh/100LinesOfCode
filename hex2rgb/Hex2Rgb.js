const hex2rgb = (hex, alpha) => {
	let tmp = hex;
	if(tmp.includes('#')) {tmp = tmp.replace('#', '');}

	let r = parseInt(tmp.length == 3 ? tmp.slice(0, 1).repeat(2) : tmp.slice(0, 2), 16);
	let g = parseInt(tmp.length == 3 ? tmp.slice(1, 2).repeat(2) : tmp.slice(2, 4), 16);
	let b = parseInt(tmp.length == 3 ? tmp.slice(2, 3).repeat(2) : tmp.slice(4, 6), 16);

	if(typeof alpha == 'number' == false && !isNaN(alpha)) {
		return 'Alpha param is not a number...';
	}

	if(alpha) {
		return `rgba(${r}, ${g}, ${b}, ${alpha})`
	};
	
	return `rgb(${r}, ${g}, ${b})`;
}

console.log(hex2rgb('FFF'))
console.log(hex2rgb('#070707', 0.5))