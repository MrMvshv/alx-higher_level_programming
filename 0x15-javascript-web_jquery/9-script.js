/*
 *  fetches the character name
 *  from the url and renders in html
 */
'use strict';
const proxyUrl = 'https://cors-anywhere.herokuapp.com/'; // proxy server URL
const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr'; // API URL
const url = proxyUrl + apiUrl; // combine the URLs

$(() => {
  $.get(`${url}`, (data, status) => {
    $('DIV#hello').html(data.hello);
  });
});
