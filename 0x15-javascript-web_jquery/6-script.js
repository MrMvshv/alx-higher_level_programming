/*
 * updates the text color of the <header>
 * element to red (#FF0000) using jquery
 */
$(document).ready(function(){
    $('div#update_header').click(function(){
        $('header').html("New Header!!!");
    });
});

