#!/usr/bin/node
/**
 * This script prints all characters
 * of a star wars movie
 * uses  the Star wars API
 * first argument is movie id
 * Display one character name by line
 */
const request = require('request');
const movie = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movie;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const result = JSON.parse(body);
    const list = result.characters;

    list.forEach((actor) => {
      request.get(actor, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else {
          const data = JSON.parse(body);
          console.log(data.name);
        }
      });
    });
  }
});
