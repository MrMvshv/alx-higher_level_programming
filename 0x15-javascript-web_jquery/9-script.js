/*
 *  fetches the character name
 *  from the url and renders in html
 */
'use strict';

const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$(() => {
  $.get(`${url}`, (data, status) => {
    $('DIV#hello').html(data.hello);
  });
});
