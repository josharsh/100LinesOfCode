const puppeteer = require('puppeteer');
const { default: PQueue } = require('p-queue');
const utilityFuncs = require('./utility');

const urls = [
	{
		name: 'HackerNews',
		dir: './hackernews',
		link: 'https://news.ycombinator.com/',
	},
];

const queue = new PQueue({
	concurrency: urls.length,
});

(async () => {
	// Open browser
	const browser = await puppeteer.launch({ headless: true });
	try {
		const scrapePage = async urlInfo => {
			const browserInstance = browser;
			try {
				const page = await browserInstance.newPage();
				await page.goto(urlInfo.link, {
					waitUntil: 'load',
					timeout: 0,
				});
				let news;
				switch (urlInfo.name) {
					case 'HackerNews':
						news = await utilityFuncs.scrapeHackerNews(page);
						break;
					default:
						utilityFuncs.handleError(
							browser,
							new Error('website not yet supported')
						);
				}

				utilityFuncs.saveDataInServer(urlInfo, news, page, browser);
				await page.screenshot({
					path: `${urlInfo.dir}/${urlInfo.name}-${utilityFuncs.parseDate()}.png`,
				});

				await page.close();
				const pages = await browser.pages();
				if (pages.length === 1) {
					utilityFuncs.handleSuccess(browser);
				}
			} catch (err) {
				utilityFuncs.handleError(browser, err);
			}
		};
		for (let url of urls) {
			queue.add(async () => scrapePage(url));
		}
	} catch (err) {
		utilityFuncs.handleError(browser, err);
	}
})();
