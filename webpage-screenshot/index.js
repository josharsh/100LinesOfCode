const puppeteer = require("puppeteer");
const url = "<REPLACE_URL>"; //Replace the url with the website you want to capture

async function run() {
  let browser = await puppeteer.launch({ headless: true });
  let page = await browser.newPage();
  await page.goto(url, { waitUntil: "networkidle0", timeout: 60000 });
  await page.setViewport({ width: 1024, height: 800 });
  await page.screenshot({
    path: "./screenshot.jpg",
    type: "jpeg",
    fullPage: true,
  });
  await page.close();
  await browser.close();
}
run();
