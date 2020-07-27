const chalk = require('chalk');
const fs = require('fs');

const error = chalk.keyword('red');
const success = chalk.keyword('green');

const parseDate = () => {
	today = new Date();
	let hh = today.getHours();
	let dd = today.getDate();
	let mm = today.getMonth() + 1; //As January is 0.
	let yyyy = today.getFullYear();

	if (dd < 10) dd = '0' + dd;
	if (mm < 10) mm = '0' + mm;
	return `${hh}-${dd}-${mm}-${yyyy}`;
};

const handleError = async (browser, err) => {
	console.log(error(err));
	await browser.close();
	console.log(error('Browser closed'));
};

const handleSuccess = async browser => {
	await browser.close();
	console.log(success('Browser closed'));
	console.log(success('Scraped successfully'));
};

const scrapeHackerNews = async page => {
	try {
		await page.waitForSelector('a.storylink');

		const news = await page.evaluate(() => {
			const titleNodeList = document.querySelectorAll(`a.storylink`);
			const ageList = document.querySelectorAll(`span.age`);
			const scoreList = document.querySelectorAll(`span.score`);
			const titleLinkArray = [];
			for (let i = 0; i < titleNodeList.length; i++) {
				titleLinkArray[i] = {
					title: titleNodeList[i].innerText.trim(),
					link: titleNodeList[i].getAttribute('href'),
					age: ageList[i].innerText.trim(),
					score: scoreList[i].innerText.trim(),
				};
			}
			return titleLinkArray;
		});

		return news;
	} catch (err) {
		handleError(err);
	}
};

const saveDataInServer = (urlInfo, news) => {
	if (!fs.existsSync(urlInfo.dir)) {
		fs.mkdirSync(urlInfo.dir);
	}

	fs.writeFile(
		`${urlInfo.dir}/${urlInfo.name}-${parseDate()}.json`,
		JSON.stringify(news),
		err => {
			if (err) throw err;
			console.log(success('saved!'));
		}
	);
};

module.exports = {
	parseDate,
	handleError,
	handleSuccess,
	scrapeHackerNews,
	saveDataInServer,
};
