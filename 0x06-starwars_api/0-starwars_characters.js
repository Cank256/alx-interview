#!/usr/bin/node

const request = require('request');

/**
 * Fetches characters from a Star Wars movie and prints their names
 * @param {string} movieId - The ID of the Star Wars movie
 */
async function getStarWarsCharacters (movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  try {
    const movieResponse = await new Promise((resolve, reject) => {
      request(movieUrl, (error, response, body) => {
        if (error) reject(error);
        else if (response.statusCode === 200) resolve(JSON.parse(body));
        else reject(new Error('Failed to fetch movie data'));
      });
    });

    const characters = await Promise.all(movieResponse.characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) reject(error);
          else if (response.statusCode === 200) {
            const character = JSON.parse(body);
            resolve(character.name);
          } else {
            reject(new Error('Failed to fetch character data'));
          }
        });
      });
    }));

    console.log(characters.join('\n'));
  } catch (error) {
    console.error('Error:', error);
  }
}

const movieId = process.argv[2];
if (!movieId || isNaN(movieId)) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

getStarWarsCharacters(movieId);
