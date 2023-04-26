#!/usr/bin/node
/**
 * This script prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 * uses  the Star wars API
 * endpoint -> https://swapi-api.alx-tools.com/api/films/:id
 */
const request = require('request');
const id = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const url = baseUrl + id;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const result = JSON.parse(body);
    console.log(result.title);
  }
});
