#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const options = {
  url: `https://swapi-api.alx-tools.com/api/films/${args[0]}/`
};

const loopChar = (url) => {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body).name;
      console.log(data);
    } else console.error(error);
  });
};

request(options, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const charList = JSON.parse(body).characters;
    charList.forEach(loopChar);
  } else console.error(error);
});
