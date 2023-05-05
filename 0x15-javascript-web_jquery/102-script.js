/*
 * fetches and prints how to say “Hello”
 * depending on the language
 */
'use strict';
const proxyUrl = 'https://cors-anywhere.herokuapp.com/'; // proxy server URL
const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
const url = proxyUrl + apiUrl;

$(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    $.getJSON(${url}?lang=${languageCode}, (data) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
