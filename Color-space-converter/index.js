function rgbToHSL(r, g, b) {
    r /= 255;
    g /= 255;
    b /= 255;

    const min = Math.min(r, g, b);
    const max = Math.max(r, g, b);

    const luminanceRange = max - min;
    const totalLuminance = max + min;
    const _2totalLuminence = 2 - totalLuminance;
    let h, s, l = totalLuminance / 2;

    if (min === max) {
        h = s = 0;
    } else {
        s = l > 0.5 ? luminanceRange / _2totalLuminence : luminanceRange / totalLuminance;
        if (r === max) {
            h = (g - b) / luminanceRange + (g < b ? 6 : 0);
        } else if (g === max) {
            h = (b - r) / luminanceRange + 2;
        } else if (b === max) {
            h = (r - g) / luminanceRange + 4;
        }
        h = Math.round(h * 60);
        if (h < 0) h += 360;
    }
    return [h, Math.round(s * 100), Math.round(l * 100)];
}

function rgbToCmyk(R, G, B) {
    (R /= 255), (G /= 255), (B /= 255)
    const max = Math.max(R, G, B);
    let K = (1 - max),
        C = ((1 - R - K) / (1 - K)) * 100,
        M = ((1 - G - K) / (1 - K)) * 100,
        Y = ((1 - B - K) / (1 - K)) * 100
    return [~~C, ~~M, ~~Y, ~~(K * 100)];
}

function hslToRgb(H, S, L) {
    (S /= 100), (L /= 100)
    const chroma = (1 - 1 * Math.abs((2 * L) - 1)) * S,
        H_ = (H / 60),
        X = chroma * (1 - 1 * Math.abs((H_ % 2) - 1));
    let R1,
        G1,
        B1;
    if (0 <= H_ && H_ <= 1) {
        R1 = chroma, G1 = X, B1 = 0
    } else if (1 <= H_ && H_ < 2) {
        R1 = X, G1 = chroma, B1 = 0
    } else if (2 <= H_ && H_ < 3) {
        R1 = 0, G1 = chroma, B1 = X
    } else if (3 <= H_ && H_ < 4) {
        R1 = 0, G1 = X, B1 = chroma
    } else if (4 <= H_ && H_ < 5) {
        R1 = X, G1 = 0, B1 = chroma
    } else if (5 <= H_ && H_ < 6) {
        R1 = chroma, G1 = 0, B1 = X
    }
    let m = L - (chroma / 2)
    let R = (R1 + m) * 255,
        G = (G1 + m) * 255,
        B = (B1 + m) * 255
    return [~~R, ~~G, ~~B]
}

function cmykToRgb(C, M, Y, K) {
    (C /= 100), (M /= 100), (Y /= 100), (K /= 100)
    let R = Math.round(255 * (1 - C) * (1 - K)),
        G = Math.round(255 * (1 - M) * (1 - K)),
        B = Math.round(255 * (1 - Y) * (1 - K));
    return [R, G, B]
}

function hslToCmyk(H, S, L) {
    let toRGB = hslToRgb(H, S, L)
    return rgbToCmyk(toRGB[0], toRGB[1], toRGB[2])
}

function cmykToHsl(C, M, Y, K) {
    toRGB = cmykToRgb(C, M, Y, K)
    return rgbToHSL(toRGB[0], toRGB[1], toRGB[2]);
}


module.exports = {rgbToHSL, rgbToCmyk, hslToRgb, cmykToRgb, hslToCmyk, cmykToHsl}