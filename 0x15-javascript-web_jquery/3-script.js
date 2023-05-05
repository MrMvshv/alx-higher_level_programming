/*
 * updates the text color of the <header>
 * element to red (#FF0000) using jquery
 */
const head = $('header');
const red = $('div#red_header');

red.on( "click", function() {
  head.addClass("red");
});
