const { createCanvas } = require("canvas");
const MD5 = require("crypto-js/md5");
const express = require("express");
const app = express();
const port = process.env.PORT || "8000";
app.use(express.static("client"));

app.get("/api/:name", (req, res) => {
  image = generate(req.params.name);
  res.json({ img: image });
});

app.listen(port);

function generate(name) {
  const canvas = createCanvas(200, 200);
  const ctx = canvas.getContext("2d");
  let hash = MD5(name).toString();
  let props = {};
  props.bgcolor = hash.substring(0, 4);
  props.facecolor = hash.substring(4, 8);
  props.eyecolor = hash.substring(8, 12);
  props.mouthcolor = hash.substring(12, 16);
  props.lefteyesize = map(
    parseInt(hash.substring(16, 20), 16) % 50,
    0,
    50,
    10,
    50
  );
  props.righteyesize = map(
    parseInt(hash.substring(20, 24), 16) % 50,
    0,
    50,
    10,
    50
  );
  props.mouthsize = map(
    parseInt(hash.substring(24, 28), 16) % 50,
    0,
    50,
    10,
    30
  );
  ctx.fillStyle = `#${props.bgcolor}`;
  ctx.fillRect(0, 0, 200, 200);
  ctx.translate(100, 100);
  ctx.strokeStyle = "#000000";
  ctx.fillStyle = `#${props.facecolor}`;
  ctx.beginPath();
  ctx.arc(0, 0, 50, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  ctx.fillStyle = `#${props.eyecolor}`;
  ctx.beginPath();
  ctx.arc(-20, 0, props.lefteyesize / 2, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(20, 0, props.righteyesize / 2, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();
  ctx.fillStyle = `#${props.mouthcolor}`;
  ctx.beginPath();
  ctx.arc(0, 30, props.mouthsize / 2, 0, 2 * Math.PI);
  ctx.fill();
  ctx.stroke();

  return canvas.toDataURL();
}
function map(n, start1, stop1, start2, stop2) {
  const newval = ((n - start1) / (stop1 - start1)) * (stop2 - start2) + start2;
  return newval;
}
