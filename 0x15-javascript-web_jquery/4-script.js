/*
 * updates the text color of the <header>
 * element to red (#FF0000) using jquery
 */
$(document).ready(function(){

    $('#toggle_header').click(function(){

        $('header').toggleClass('red green');

    });

});

