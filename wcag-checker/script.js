// --- 1. Element Selection ---
const textColorInput = document.getElementById('text-color-input');
const bgColorInput = document.getElementById('bg-color-input');
const previewBox = document.getElementById('preview-box');
const textHexValue = document.getElementById('text-hex-value');
const textRgbValue = document.getElementById('text-rgb-value');
const bgHexValue = document.getElementById('bg-hex-value');
const bgRgbValue = document.getElementById('bg-rgb-value');
const contrastRatioValue = document.getElementById('contrast-ratio-value');
const wcagAAStatus = document.getElementById('wcag-aa-status');
const wcagAAAStatus = document.getElementById('wcag-aaa-status');

// --- 2. Event Listeners ---
textColorInput.addEventListener('input', handleColorChange);
bgColorInput.addEventListener('input', handleColorChange);

// --- 3. Main Function ---
function handleColorChange() {
    const textColorHex = textColorInput.value.toUpperCase();
    const bgColorHex = bgColorInput.value.toUpperCase();

    previewBox.style.color = textColorHex;
    previewBox.style.backgroundColor = bgColorHex;

    const textColorRGB = hexToRgb(textColorHex);
    const bgColorRGB = hexToRgb(bgColorHex);

    const textColorLum = getLuminance(textColorRGB.r, textColorRGB.g, textColorRGB.b);
    const bgColorLum = getLuminance(bgColorRGB.r, bgColorRGB.g, bgColorRGB.b);
    
    const contrastRatio = calculateContrastRatio(textColorLum, bgColorLum);

    contrastRatioValue.innerText = `${contrastRatio.toFixed(2)} : 1`;
    checkWCAGStandards(contrastRatio);

    textHexValue.value = textColorHex;
    textRgbValue.value = `rgb(${textColorRGB.r}, ${textColorRGB.g}, ${textColorRGB.b})`;
    bgHexValue.value = bgColorHex;
    bgRgbValue.value = `rgb(${bgColorRGB.r}, ${bgColorRGB.g}, ${bgColorRGB.b})`;
}

// --- 4. Conversion Functions ---
function hexToRgb(hex) {
    let cleanHex = hex.replace("#", "");
    const r = parseInt(cleanHex.substring(0, 2), 16);
    const g = parseInt(cleanHex.substring(2, 4), 16);
    const b = parseInt(cleanHex.substring(4, 6), 16);
    return { r, g, b };
}

// --- 5. Contrast Calculation Functions ---
function getLuminance(r, g, b) {
    const a = [r, g, b].map((v) => {
        v /= 255;
        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
}

function calculateContrastRatio(lum1, lum2) {
    const L1 = Math.max(lum1, lum2);
    const L2 = Math.min(lum1, lum2);
    return (L1 + 0.05) / (L2 + 0.05);
}

// Helper function to avoid repetition
function updateStatus(element, passes) {
    element.innerText = passes ? 'PASS' : 'FAIL';
    element.style.color = passes ? 'green' : 'red';
}

function checkWCAGStandards(contrastRatio) {
    updateStatus(wcagAAStatus, contrastRatio >= 4.5); //
    updateStatus(wcagAAAStatus, contrastRatio >= 7); //
}

// --- 8. Copy Buttons ---
const copyButtons = document.querySelectorAll(".copy-btn");

copyButtons.forEach((button) => {
    // Using async/await for cleaner code
    button.addEventListener("click", async () => {
        const targetId = button.dataset.target;
        const targetInput = document.getElementById(targetId);
        
        try {
            await navigator.clipboard.writeText(targetInput.value);
            button.innerText = "Copied!";
            setTimeout(() => {
                button.innerText = "Copy";
            }, 2000);
        } catch (err) {
            console.error("Failed to copy text: ", err);
        }
    });
});