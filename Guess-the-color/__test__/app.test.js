const { makeColorValue, makeColors, setButtonColor } = require('../app');

describe('Testing app functionality', () => {
	it('Gets a random number when maleColorValue() is called', () => {
		let random1 = makeColorValue();
		let random2 = makeColorValue();

		expect(random1 !== random2).toBe(true);
	});
	it('number should not be larger than 255', () => {
		let random1 = makeColorValue();

		expect(random1 < 255).toBe(true);
	});
	it('testing makeColor()', () => {
		makeColors();

		expect(setButtonColor()).toBeCalledWith(makeColors());
	});
});
