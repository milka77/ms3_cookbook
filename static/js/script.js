/* Adding new row function at the newrecipe form to the textarea fields */ 
function adjustHeight(el){
    el.style.height = (el.scrollHeight > el.clientHeight) ? (el.scrollHeight)+"px" : "41px";
}

/* Changing the background color for the navigation bar */
$(document).ready(function() {
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll > 225) {
            $('#nav').removeClass('cook-navbar');
            $('#nav').addClass('bg-light');
            $('#nav').addClass('navbar-light');
        } else {
            $('#nav').removeClass('bg-light');
            $('#nav').removeClass('navbar-light');
            $('#nav').addClass('cook-navbar');
        }
    })
}) 