/*
 *  fetches and prints how to say “Hello”
 *  depending on the language
 */
$(document).ready(function () {
  function translateHello() {
    const langCode = $('#language_code').val();

    const proxyUrl = 'https://cors-anywhere.herokuapp.com/'; // proxy server URL
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/';
    const url = proxyUrl + apiUrl + '?lang=${langCode}';

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translateHello);

  $('#language_code').keydown(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
