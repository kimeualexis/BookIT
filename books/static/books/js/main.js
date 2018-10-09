$('ul li a').click(function() {
    $(this).addClass('active').siblings().removeClass('active');
});