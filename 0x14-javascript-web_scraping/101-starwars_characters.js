#!/usr/bin/node
/**
 * This script prints all characters
 * of a star wars movie
 * uses the Star Wars API
 * first argument is movie id
 * Display one character name by line
 */
const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movie;

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request.get(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      const data = JSON.parse(body);
      console.log(data.name);
      printCharacters(characters, index + 1);
    }
  });
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const result = JSON.parse(body);
    const characters = result.characters;
    printCharacters(characters, 0);
  }
});
