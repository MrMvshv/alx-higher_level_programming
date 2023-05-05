/*
 * fetches and prints how to say “Hello”
 * depending on the language
 */
'use strict';

const url = 'https://www.fourtonfish.com/hellosalut/hello/';

$(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();
    $.getJSON(${url}?lang=${languageCode}, (data) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
