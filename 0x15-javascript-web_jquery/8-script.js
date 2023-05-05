/*
 *  fetches the character name
 *  from the url and renders in html
 */
'use strict';

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$(document).ready(() => {
  const $list = $('ul#list_movies');

  fetch(`${url}`)
    .then(response => response.json())
    .then(data => {
      data.results.forEach(movie => {
        const $item = $('<li></li>').text(movie.title);
        $list.append($item);
      });
    })
    .catch(error => console.error(error));
});
