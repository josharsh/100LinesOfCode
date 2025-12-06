// SVG Icons
const iconCopy = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>`;
const iconCheck = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;

// DOM Elements
const textColorInput = document.getElementById("text-color-input");
const bgColorInput = document.getElementById("bg-color-input");
const previewBox = document.getElementById("preview-box");
const textHexValue = document.getElementById("text-hex-value");
const textRgbValue = document.getElementById("text-rgb-value");
const bgHexValue = document.getElementById("bg-hex-value");
const bgRgbValue = document.getElementById("bg-rgb-value");
const contrastRatioValue = document.getElementById("contrast-ratio-value");
const wcagAAStatus = document.getElementById("wcag-aa-status");
const wcagAAAStatus = document.getElementById("wcag-aaa-status");

// Event Listeners
[textColorInput, bgColorInput].forEach(el => el.addEventListener("input", handleColorChange));

function handleColorChange() {
    const textHex = textColorInput.value.toUpperCase(), bgHex = bgColorInput.value.toUpperCase();
    const textRGB = hexToRgb(textHex), bgRGB = hexToRgb(bgHex);
    previewBox.style.color = textHex;
    previewBox.style.backgroundColor = bgHex;
    const ratio = calculateContrastRatio(getLuminance(textRGB.r, textRGB.g, textRGB.b), getLuminance(bgRGB.r, bgRGB.g, bgRGB.b));
    contrastRatioValue.innerText = `${ratio.toFixed(2)} : 1`;
    checkWCAGStandards(ratio);
    textHexValue.value = textHex;
    textRgbValue.value = `rgb(${textRGB.r}, ${textRGB.g}, ${textRGB.b})`;
    bgHexValue.value = bgHex;
    bgRgbValue.value = `rgb(${bgRGB.r}, ${bgRGB.g}, ${bgRGB.b})`;
}

function hexToRgb(hex) {
    const h = hex.replace("#", "");
    return { r: parseInt(h.substring(0, 2), 16), g: parseInt(h.substring(2, 4), 16), b: parseInt(h.substring(4, 6), 16) };
}

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

function checkWCAGStandards(contrastRatio) {
    const updateStatus = (el, passes) => { el.innerText = passes ? "PASS" : "FAIL"; el.style.color = passes ? "green" : "red"; };
    updateStatus(wcagAAStatus, contrastRatio >= 4.5);
    updateStatus(wcagAAAStatus, contrastRatio >= 7);
}

// Copy buttons functionality
document.querySelectorAll(".copy-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
        const target = document.getElementById(btn.dataset.target);
        try {
            await navigator.clipboard.writeText(target.value);
            btn.innerHTML = iconCheck; btn.disabled = true;
            setTimeout(() => { btn.innerHTML = iconCopy; btn.disabled = false; }, 2000);
        } catch (err) { console.error("Failed to copy: ", err); }
    });
});

// EyeDropper functionality
async function pickColor(target) {
    if (!window.EyeDropper) { alert('Your browser does not support EyeDropper API.'); return; }
    try {
        const result = await new EyeDropper().open();
        target.value = result.sRGBHex.toUpperCase();
        handleColorChange();
    } catch (e) { console.log('Color selection cancelled'); }
}

// Manual input handlers
function rgbToHex(r, g, b) { return "#" + [r, g, b].map(x => { const h = x.toString(16); return h.length === 1 ? "0" + h : h; }).join(""); }
function handleManualInput(input, colorInput) {
    const v = input.value.trim().toUpperCase();
    if (v.startsWith("#") && /^#[0-9A-F]{6}$/i.test(v)) { colorInput.value = v; handleColorChange(); }
    else if (v.startsWith("RGB")) {
        const m = v.match(/RGB\((\d+),\s*(\d+),\s*(\d+)\)/);
        if (m) { const [, r, g, b] = m.map(Number); if (r <= 255 && g <= 255 && b <= 255) { colorInput.value = rgbToHex(r, g, b); handleColorChange(); } }
    }
}
[textHexValue, textRgbValue].forEach(el => el.addEventListener('blur', () => handleManualInput(el, textColorInput)));
[bgHexValue, bgRgbValue].forEach(el => el.addEventListener('blur', () => handleManualInput(el, bgColorInput)));

// Attach EyeDropper to buttons
document.getElementById('text-eye-dropper-btn')?.addEventListener('click', () => pickColor(textColorInput));
document.getElementById('bg-eye-dropper-btn')?.addEventListener('click', () => pickColor(bgColorInput));
document.getElementById('bg-eye-dropper-btn')?.addEventListener('click', () => pickColor(bgColorInput));