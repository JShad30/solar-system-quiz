/* Changing the colour of the navbar area on scroll */

$(function () {
    $(document).scroll(function () {
        var $nav = $(".top-bar");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});