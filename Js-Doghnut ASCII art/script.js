const pre = document.createElement("pre");
document.body.appendChild(pre);

let var1 = 0, var2 = 0;
setInterval(() => {
    var1 += .07,
    var2 += .03; const a = [...new Array(1760)
    ].map((a, r) => r % 80 === 79 ? "\n" : " "), r =
            new Array(1760).fill(0), t = Math.cos(var1),
        e = Math.sin(var1), n = Math.cos(var2), o = Math.sin
            (var2); for (let s = 0; s < 6.28; s +=
                .07) {
                    const c = Math.cos(s), h = Math
                        .sin(s); for (let s = 0; s < 6.28;
            s += .02) {
                const v = Math.sin(s), M =
                    Math.cos(s), i = c + 2, l = 1 / (v * i * e + h
                        * t + 5), p = v * i * t - h * e, d = 0 | 40 + 30 * l *
                            (M * i * n - p * o), m = 0 | 12 + 15 * l * (M * i * o + p * n)
                , f = 0 | 8 * ((h * e - v * c * t) * n - v * c * e - h * t - M * c * o),
                y = d + 80 * m; m < 22 && m >= 0 && d >= 0 && d < 79 && l >
                    r[y] && (r[y] = l, a[y] = ".,-~:;=!*#$@"
                    [f > 0 ? f : 0])
        }
    } pre.innerHTML =
        a.join("")
}, 50);





const funs = new Funs("light");
funs.signature();