/*
 *  fetches the character name
 *  from the url and renders in html
 */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const result = JSON.parse(body);
  }
});

cName = result.name;

$('div#character').html(cName);
