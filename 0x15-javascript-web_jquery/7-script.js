/*
 *  fetches the character name
 *  from the url and renders in html
 */
'use strict';

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$(document).ready(() => {
  fetch(`${url}`)
    .then(response => response.json())
    .then(data => $('DIV#character').html(data.name))
    .catch(error => console.error(error));
});
