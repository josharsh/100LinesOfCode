// --- 1. Seleção dos Novos Elementos ---
const textColorInput = document.getElementById('text-color-input');
const bgColorInput = document.getElementById('bg-color-input');

// Seletores da área de resultado
const contrastRatioValue = document.getElementById('contrast-ratio-value');
const wcagAAStatus = document.getElementById('wcag-aa-status');
const wcagAAAStatus = document.getElementById('wcag-aaa-status');

// --- 2. Event Listeners ---
// Precisamos ouvir mudanças nos DOIS seletores
textColorInput.addEventListener('input', handleColorChange);
bgColorInput.addEventListener('input', handleColorChange);

// --- 3. Função Principal de Orquestração ---
function handleColorChange() {
    const textColorHex = textColorInput.value;
    const bgColorHex = bgColorInput.value;

    // --- PRÓXIMOS PASSOS (A FAZER) ---
    // 1. Converter HEX para RGB (já temos a função)
    const textColorRGB = hexToRgb(textColorHex);
    const bgColorRGB = hexToRgb(bgColorHex);

    // 2. Calcular a Luminância de cada cor (PRECISAMOS CRIAR)
    //    Esta é a fórmula que você pesquisou no W3C
    const textColorLum = getLuminance(textColorRGB.r, textColorRGB.g, textColorRGB.b);
    const bgColorLum = getLuminance(bgColorRGB.r, bgColorRGB.g, bgColorRGB.b);

    // 3. Calcular a Taxa de Contraste (PRECISAMOS CRIAR)
    //    Esta é a segunda fórmula que você pesquisou
    const contrastRatio = calculateContrastRatio(textColorLum, bgColorLum);

    // 4. Atualizar a UI (PRECISAMOS FAZER)
    contrastRatioValue.innerText = `${contrastRatio.toFixed(2)} : 1`;
    checkWCAGStandards(contrastRatio);
}

// --- 4. Funções de Conversão (Reutilizada) ---
// Esta função veio do nosso MVP anterior
function hexToRgb(hex) {
    let cleanHex = hex.replace("#", "");
    const r = parseInt(cleanHex.substring(0, 2), 16);
    const g = parseInt(cleanHex.substring(2, 4), 16);
    const b = parseInt(cleanHex.substring(4, 6), 16);
    return { r, g, b };
}

// --- 5. Funções de Cálculo de Contraste (A FAZER) ---
// (Aqui vamos adicionar getLuminance, calculateContrastRatio, e checkWCAGStandards)

// Esta função implementa a fórmula de Luminância Relativa do W3C
//
function getLuminance(r, g, b) {
    // 1. Normaliza os valores 0-255 para o intervalo 0-1
    const a = [r, g, b].map((v) => {
        v /= 255; // Converte para sRGB
        // Aplica a fórmula de linearização
        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    
    // 2. Aplica os coeficientes da fórmula principal
    // L = 0.2126 * R + 0.7152 * G + 0.0722 * B
    //
    return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
}

// Esta função implementa a fórmula de Taxa de Contraste do W3C
//
function calculateContrastRatio(lum1, lum2) {
    // Encontra qual luminância é a mais clara (L1) e a mais escura (L2)
    const L1 = Math.max(lum1, lum2);
    const L2 = Math.min(lum1, lum2);

    // Aplica a fórmula
    const ratio = (L1 + 0.05) / (L2 + 0.05);

    return ratio;
}

// Esta função verifica a taxa contra os padrões WCAG
// e atualiza a UI.
function checkWCAGStandards(contrastRatio) {
    // Verifica o Nível AA (Taxa de 4.5)
    if (contrastRatio >= 4.5) {
        wcagAAStatus.innerText = 'PASS';
        wcagAAStatus.style.color = 'green';
    } else {
        wcagAAStatus.innerText = 'FAIL';
        wcagAAStatus.style.color = 'red';
    }
    
    // Verifica o Nível AAA (Taxa de 7.0)
    if (contrastRatio >= 7) {
        wcagAAAStatus.innerText = 'PASS';
        wcagAAAStatus.style.color = 'green';
    } else {
        wcagAAAStatus.innerText = 'FAIL';
        wcagAAAStatus.style.color = 'red';
    }
}