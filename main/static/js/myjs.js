$(function() {

    //accordion menu courses
    if ( $(".actableheight").length ) {

        $("h4").click( function() {
            $(this).parent().toggleClass('active');
        });

    }

    //login menu
    $("#loginlink").click( function(e) {
        //disable link click
        e.preventDefault();
        //show menu
        $("#regmenu").removeClass("active");
        $("#loginmenu").toggleClass("active");
    });

    //register menu
    $("#reglink").click( function(e) {
        //disable link click
        e.preventDefault();
        //show menu
        $("#loginmenu").removeClass("active");
        $("#regmenu").toggleClass("active");
    });
});
