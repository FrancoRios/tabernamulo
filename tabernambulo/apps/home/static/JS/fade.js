$(document).ready(function(){
    $(window).scroll(function(){
        $("#carouselExampleIndicators").css("opacity", 1 - $(window).scrollTop() / $('#carouselExampleIndicators').height());
    });
});