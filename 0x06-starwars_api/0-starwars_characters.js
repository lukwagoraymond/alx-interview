#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const options = {
  url: `https://swapi-api.alx-tools.com/api/films/${args[0]}/`
};

const loopChar = (url) => {
  const promise = new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const data = JSON.parse(body).name;
        resolve(data);
      } else reject(error);
    });
  });
  return promise;
};

request(options, async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const charList = JSON.parse(body).characters;
    try {
      const results = await Promise.all(charList.map(loopChar));
      results.forEach((e) => { console.log(e); });
    } catch (error) {
      console.error(error);
    }
  }
});
