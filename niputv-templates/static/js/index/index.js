function index_module_popular(data, type) {
    $(type).prepend('<div class="module-interchangeable-indexvideo-videolist main">' +
        '<a href="/watch/' + data['video_id'] + '" target="_blank">' +
        '<div class="module-interchangeable-indexvideo-videolist wp">' +
        '<div class="module-interchangeable-indexvideo-videolist cover"><img src="http://video-cover.niputv.com/' +
        data['video_cover'] + '" width="100%"></div>' +
        '<div class="module-interchangeable-indexvideo-videolist title">' + data['video_name'] +
        '</div>' +
        '<div class="module-interchangeable-indexvideo-videolist video_info">' +
        '' + data['play_statistics'] + '次播放 - ' + data['release_date'] + '' +
        '</div>' +
        '</div>' +
        '</a></div>')
};

$(document).ready(function () {
    $.getJSON('/api/index-content/module/all/0',
        function (data, textStatus) {
            $.each((data),
                function () {
                    var type = "#index_module_popular"
                    index_module_popular(this, type);
                });
        });
});

//MAD
function getdata_mad() {
    $.getJSON('/api/index-content/module/category/1',
        function (data, textStatus) {
            $.each((data),
                function () {
                    var type = "#index_module_mad"
                    index_module_popular(this, type);
                });
        });
}
getdata_mad();
