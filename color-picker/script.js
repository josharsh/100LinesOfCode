// Get DOM elements
const colorInput = document.getElementById("color-input");
const hexValue = document.getElementById("hex-value");
const rgbValue = document.getElementById("rgb-value");
const hslValue = document.getElementById("hsl-value");

// Event listener for the color input to update color values
colorInput.addEventListener("input", () => {
    const newColorHex = colorInput.value.toUpperCase();
    hexValue.value = newColorHex;

    // Convert HEX to RGB and HSL
    const newColorRGB = hexToRgb(newColorHex);
    const newColorHSL = rgbToHsl(newColorRGB.r, newColorRGB.g, newColorRGB.b);

    // Update the input fields with the new color values
    rgbValue.value = `rgb(${newColorRGB.r}, ${newColorRGB.g}, ${newColorRGB.b})`;
    hslValue.value = `hsl(${newColorHSL.h}, ${newColorHSL.s}%, ${newColorHSL.l}%)`;
});

// Function to convert a HEX color to its RGB equivalent
function hexToRgb(hex) {
    // Remove '#' if present
    let cleanHex = hex.replace("#", "");
    // Parse the R, G, and B components
    const r = parseInt(cleanHex.substring(0, 2), 16);
    const g = parseInt(cleanHex.substring(2, 4), 16);
    const b = parseInt(cleanHex.substring(4, 6), 16);
    return { r, g, b };
}

// Function to convert an RGB color to its HSL equivalent
function rgbToHsl(r, g, b) {
    // Normalize RGB values to be between 0 and 1
    r /= 255;
    g /= 255;
    b /= 255;
    const max = Math.max(r, g, b);
    const min = Math.min(r, g, b);
    let h, s, l = (max + min) / 2;

    if (max === min) {
        // Achromatic (grayscale)
        h = s = 0;
    } else {
        const d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch (max) {
            case r:
                h = (g - b) / d + (g < b ? 6 : 0);
                break;
            case g:
                h = (b - r) / d + 2;
                break;
            case b:
                h = (r - g) / d + 4;
                break;
        }
        h /= 6;
    }

    // Return HSL values rounded to the nearest integer
    return {
        h: Math.round(h * 360),
        s: Math.round(s * 100),
        l: Math.round(l * 100),
    };
}

// Get all elements with the class 'copy-btn'
const copyButtons = document.querySelectorAll(".copy-btn");

// Add a click event listener to each copy button
copyButtons.forEach((button) => {
    button.addEventListener("click", () => {
        // Get the target input field from the button's data attribute
        const targetId = button.dataset.target;
        const targetInput = document.getElementById(targetId);
        const textToCopy = targetInput.value;

        // Use the Clipboard API to copy the text
        navigator.clipboard
            .writeText(textToCopy)
            .then(() => {
                // Provide user feedback on successful copy
                button.innerText = "Copied!";
                setTimeout(() => {
                    button.innerText = "Copy";
                }, 2000);
            })
            .catch((err) => {
                // Log an error if the copy fails
                console.error("Failed to copy text: ", err);
            });
    });
});