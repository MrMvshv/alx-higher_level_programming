/*
 * updates the text color of the <header>
 * element to red (#FF0000) using jquery
 */
$(document).ready(function(){
    $('div#add_item').click(function(){
        $('ul.my_list').append('<li>Item</li>');
    });
});

