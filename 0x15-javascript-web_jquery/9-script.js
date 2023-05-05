/*
 *  fetches the character name
 *  from the url and renders in html
 */
'use strict';

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(document).ready(() => {
  fetch(`${url}`, { mode: 'no-cors' })
    .then(response => response.json())
    .then(data => {
      $('div#hello').text(data.hello);
    })
    .catch(error => console.error(error));
});
