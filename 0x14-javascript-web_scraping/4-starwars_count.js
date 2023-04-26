#!/usr/bin/node
/**
 * This script prints the number of movies
 * where the character “Wedge Antilles” is present.
 * uses  the Star wars API
 * first argument is API url
 */
const request = require('request');
const apiUrl = process.argv[2];
const character = 'https://swapi-api.alx-tools.com/api/people/18/';
let number = 0;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  } else {
    const result = JSON.parse(body);
    const list = result.results;

    list.forEach((movie) => {
      if (movie.characters.includes(character)) {
        number += 1;
      }
    });
    console.log(number);
    return;
  }
});
