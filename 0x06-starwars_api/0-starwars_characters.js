#!/usr/bin/node

const request = require('request');

/**
 * Fetches characters from a Star Wars movie and prints their names
 * @param {string} movieId - The ID of the Star Wars movie
 */
function getStarWarsCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      if (response.statusCode === 200) {
        const film = JSON.parse(body);
        film.characters.forEach(characterUrl => {
          request(characterUrl, (error, response, body) => {
            if (!error && response.statusCode === 200) {
              const character = JSON.parse(body);
              console.log(character.name);
            }
          });
        });
      } else {
        console.error('Failed to fetch movie data');
      }
    }
  });
}

const movieId = process.argv[2];
if (!movieId || isNaN(movieId)) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

getStarWarsCharacters(movieId);
