$(function() {

    placeholdertext();

    //accordion menu courses
    if ($(".actableheight").length) {

        $("h4").click(function() {
            $(this).parent().toggleClass('active');
        });

    }

    //login menu
    $("#loginlink").click(function(e) {
        //disable link click
        e.preventDefault();
        //show menu
        $("#regmenu").removeClass("active");
        $("#loginmenu").toggleClass("active");
    });

    //register menu
    $("#reglink").click(function(e) {
        //disable link click
        e.preventDefault();
        //show menu
        $("#loginmenu").removeClass("active");
        $("#regmenu").toggleClass("active");
    });

    $(window).resize(function() {
        placeholdertext();
    });
});

// change placeholder text homepage according to screensize (width)
function placeholdertext() {
    if ($(window).width() < 420) {
        $("#homejs").attr("placeholder", '"Computer Science"');
    } else if ($(window).width() < 720) {
        $("#homejs").attr("placeholder", '"Computer Science",  "2INC0"');
    } else if ($(window).width() < 980) {
        $("#homejs").attr("placeholder", '"Computer Science", "Web Analytics", "2INC0"');
    } else {
        $("#homejs").attr("placeholder", '"Computer Science",  "Web Analytics",  "Calculus",  "2INC0"');
    }
}
