/**
 * Returns a formatted date with a specific format and locale
 * @param {Date} date - the date to format in locale
 * @param {string} format - the format of the date to return
 * @param {string} locale - the locale to convert from
 * @returns {string} the formatted date
 */
export const formatDateLocale = (date, format, locale) => {
  if (!(date instanceof Date)) {
    date = new Date(date);
  }
  return format(date, format, { locale });
};

/**
 * Returns a formatted string with the duration in minutes and hours from two dates
 * @param {Date} startDate - the starting date
 * @param {Date} endDate - the end date
 * @returns {string} the formatted hours and minutes string
 */
export const getDurationHoursMinutes = (startDate, endDate) => {
  const minutesTotal = differenceInMinutes(
    new Date(startDate),
    new Date(endDate)
  );
  const hours = Math.floor(minutesTotal / 60);
  const minutes = minutesTotal % 60;
  return `${hours}h ${minutes}m`;
};

/**
 * Returns a formatted string with the duration in minutes and hours from the total minutes
 * Returns the total hours from a given minutes amount
 * @param {int} minutesTotal - the number of minutes
 * @returns {string} the formatted minutes string
 */
export const getHoursMinutesFromMins = (minutesTotal) => {
  const hours = Math.floor(minutesTotal / 60);
  const minutes = minutesTotal % 60;
  if (hours > 0) {
    return `${hours}h ${minutes}m`;
  }
  return `${minutes}m`;
};

/**
 * Returns a formatted string with the hours and minutes from a date object
 * Returns the total hours from a given minutes amount
 * @param {Date} date - the date to parse
 * @returns {string} the formatted hours and minutes string
 */
export const getHoursMinutesFromDate = (date) => {
  let dateTmp = date;
  if (!(date instanceof Date)) {
    dateTmp = new Date();
  }
  return `${dateTmp.getHours()}h ${dateTmp.getMinutes()}m`;
};

/**
 * Returns a date ISO string from a given date, checks for timezone offset as well
 * @param {Date} date - the date to parse
 * @returns {string} the formatted ISO string
 */
export const getDateISO = (date) => {
  const offset = date.getTimezoneOffset();
  date = new Date(date.getTime() - offset * 60 * 1000);
  return date.toISOString().split("T")[0];
};
