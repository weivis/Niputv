$("#frame-opne_leftnav").click(function () {
    $("#frame-left_nav").toggle("slow",function () {
        if ($(this).attr("style").toLowerCase().indexOf("none") == -1) {
            $("#frame-left_nav").show();
            $('.frame-common-right_content').css("width","calc(100% - 220px)");
        }
        else {
            $("#frame-left_nav").slideUp("slow");
            $('.frame-common-right_content').css("width","100%");
        }
    });
})