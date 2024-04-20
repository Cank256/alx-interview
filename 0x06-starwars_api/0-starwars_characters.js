#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = 'https://swapi-api.hbtn.io/api/films/';

request(`${apiUrl}${movieId}/`, { json: true }, (err, res, data) => {
  if (err) {
    console.log('Error:', err);
    return;
  }

  if (res.statusCode !== 200) {
    console.log(`Status Code: ${res.statusCode}`);
    return;
  }

  data.characters.forEach((url) => {
    request(url, { json: true }, (err, res, character) => {
      if (err) {
        console.log('Error:', err);
        return;
      }

      if (res.statusCode !== 200) {
        console.log(`Status Code: ${res.statusCode}`);
        return;
      }

      console.log(character.name);
    });
  });
});
