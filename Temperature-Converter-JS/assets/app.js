const celciusInput = document.querySelector("#celcius > input");
const fahreinheitInput = document.querySelector("#fahreinheit > input");
const kelvinInput = document.querySelector("#kelvin > input");

function roundNum(num) {
  return Math.round(num * 100) / 100;
}

function celciusToFahAndKelv() {
  const cTemp = parseFloat(celciusInput.value);
  const fTemp = cTemp * (9 / 5) + 32;
  const kTemp = cTemp + 273.15;
  fahreinheitInput.value = roundNum(fTemp);
  kelvinInput.value = roundNum(kTemp);
}

function fahreinheitToCelAndKelv() {
  const fTemp = parseFloat(fahreinheitInput.value);
  const cTemp = fTemp - 32 * (5 / 9);
  const kTemp = ((fTemp + 459.67) * 5) / 9;
  celciusInput.value = roundNum(cTemp);
  kelvinInput.value = roundNum(kTemp);
}

function kelvinToCelAndFah() {
  const kTemp = parseFloat(kelvinInput.value);
  const cTemp = kTemp - 273.15;
  const fTemp = (9 / 5) * (kTemp - 273) + 32;
  fahreinheitInput.value = roundNum(fTemp);
  celciusInput.value = roundNum(cTemp);
}

function main() {
  celciusInput.addEventListener("input", celciusToFahAndKelv);
  fahreinheitInput.addEventListener("input", fahreinheitToCelAndKelv);
  kelvinInput.addEventListener("input", kelvinToCelAndFah);
}

main();
