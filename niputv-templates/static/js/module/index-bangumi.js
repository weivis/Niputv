function bangumi_all(data) {
    $("#bangumi-all").prepend('<a href="/bangumi/donga/' + data['id'] + '" target="_blank"><div class="bangumi-anime content_a"><div class="bangumi-anime content_a-img"><img src="http://video-cover.niputv.com/bangumi/cover/min/' + data['cover'] + '" width="100%"></div><div class="bangumi-anime content_a-name">' + data['name'] + '</div><div class="bangumi-anime content_a-newvideopcs">更新到第' + data['video_statistics'] + '话</div></div></a>')
    var day = data['uploads_week'];
    $("#bangumi-"+ day +"day").prepend('<a href="/bangumi/donga/' + data['id'] + '" target="_blank"><div class="bangumi-anime content_a"><div class="bangumi-anime content_a-img"><img src="http://video-cover.niputv.com/bangumi/cover/min/' + data['cover'] + '" width="100%"></div><div class="bangumi-anime content_a-name">' + data['name'] + '</div><div class="bangumi-anime content_a-newvideopcs">更新到第' + data['video_statistics'] + '话</div></div></a>')
};

function get_bangumi() {
    $.getJSON('/bangumi/api/index-module',
        function (data, textStatus) {
            $.each((data),
            function () {
                bangumi_all(this)
            });
        });
};
get_bangumi();