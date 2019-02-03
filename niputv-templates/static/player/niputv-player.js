//初始化
//eval(function(p,a,c,k,e,d){e=function(c){return(c<a?"":e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)d[e(c)]=k[c]||e(c);k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1;};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p;}('2=\'1://0.5.4.3/\'',6,6,'pclfl90b9|http|videobucket|com|clouddn|bkt'.split('|'),0,{}))
videobucket = 'http://video-dns.niputv.com/'
//--------------------------------------------------------------------
//写入播放器组建
$("head").prepend('<style>' +
'/**播放器主体**/' +
'video::-webkit-media-controls{display:none !important;}' +
'.niputv-player{width: 100%;padding-bottom: 56.25%;height: 0;position: relative;background-color: #000}' +
'/**播放器video标签**/' +
'.niputv-player-video video{width: 100%;z-index: 10;position: absolute;z-index: 10;margin: auto;bottom: 0;top: 0}' + //height: 100%;
'/**播放器控件主体**/' +
'.niputv-player-control.main{width: calc(100% - 26px);padding-left: 13px;padding-right: 13px;padding-top: 97px; height: 80px; position: absolute;bottom: 0px;z-index: 90;color: #fff;left: 0;right: 0;margin: auto;background-image: url(/static/player/img/control-shon.png);background-repeat: repeat-x;background-position: 0px 28px}' +
'.niputv-player-control.bottom{height: 50px;position: absolute;bottom: 0px;left: 0;right: 0;width: calc(100% - 26px);margin: auto}' +
'/**播放结束**/' +
'.niputv-player-playover{position: absolute;top: 0;left: 0;right: 0;height: 70px;z-index: 99999999999;background-color: #00000050;display: none}' +
'.niputv-player-playover-v.title{font-size: 18px;padding-left: 15px;color: #fff;margin-top: 10px;float: left;width: 50%}' +
'.niputv-player-playover-v.rplay{width: 135px;height: 45px;border-radius: 5px;background-color: #00000050;margin-right: 13px;margin-top: 13px;float: right;cursor: pointer}' +
'/**播放器时间轴主体**/' +
'.niputv-player-control-timeline.main{width: 100%;height: 2px;border-radius: 20px;background-color: #ffffff60;margin-top: 28px;position: absolute;bottom: 0;}' +
'.niputv-player-control-timeline.filling{float: left;height: 100%;width: 0%;background-color: #ff4280;border-radius: 20px;}' +
'.niputv-player-control-timeline.main:hover{height: 6px;}' +
'/**顶层播放键**/' +
'.niputv-player-popu.topplay{position: absolute;z-index: 999;bottom: 15%;right: 5%}' +
'.niputv-player-popu.topplay-ico{width: 100px;height: 100px;}' +
'/**控件**/' +
'.niputv-player-control.play{width: 50px;height: 50px;float: left;}' +
'.niputv-player-control.time{height: 100%;float: left;margin-left: 0px;float: left;line-height: 50px;font-size: 12.5px;}' +
'.niputv-player-control.full_screen{width: 50px;height: 40px;float: right;margin-top: 4px;}' +
'.niputv-player-control.video_sharpness{width: 70px;height: 50px;float: right;text-align: center;line-height: 50px;font-size: 12.5px;cursor: pointer}' +
'/**音量**/' +
'.niputv-player-volume-poup{width: 50px;height: 120px;background-color: #00000050;position: absolute;right: 50px;bottom: 54px;display: none}' +
'.niputv-player-volume-poup:hover{display: block !important}' +
'.niputv-player-volume-poup_control{width: 6px;height: 90px;background-color: #ffffff60;margin: 0 auto;margin-top: 15px;border-radius: 20px;position: relative;overflow: hidden}' +
'.niputv-player-volume-poup_controlfilling{position: absolute;bottom: 0;left: 0;right: 0;width: 100%;height: 100%; background-color: #ff4280;border-radius: 20px;}' +
'/**.niputv-player-control.play:hover{background-position: -50px 0px !important}**/' +
'/**清晰度**/' +
'.niputv-player-sharpness-poup.main{width: 70px;position: absolute;bottom: 54px;right: 100px;}' +
'.niputv-player-sharpness-poup.a{width: 100%;height: 35px;background-color: #00000060;font-size: 12px;line-height: 35px;text-align: center;cursor: pointer}' +
'.niputv-player-sharpness-poup.a:hover{background-color: #ff4280}' +
'/**提示控件**/' +
'#sharpness-important{position: absolute;font-size: 14px;bottom: 65px}/**清晰度切换提示**/' +
'.niputv-player-popu.buffer{position: absolute;left: 15px;bottom: 65px;color: #Fff;font-size: 14px;display: none}/**加载提示**/' +
'</style>')

$("#player").prepend('<div class="niputv-player" id="niputv-player">' +
'<div class="niputv-player-playover" id="niputv-player-playover">' +
'<div class="niputv-player-playover-v rplay" id="controls-rplay">' +
'<div><div class="niputv-player-control play" style="background: url(/static/player/img/niputv-player-ico.png) -150px -2.5px no-repeat"></div></div>' +
'<div style="float:  left;line-height: 45px;color: #fff;">重新播放</div>' +
'</div>' +
'<div class="niputv-player-playover-v title">视频播放完毕</div>' +
'<div class="niputv-player-playover-v title" style="font-size: 14px;margin-top: 5px;">如果支持该作者记得给作者点赞！</div>' +
'</div>' +
'<div class="niputv-player-popu buffer">正在加载</div>' +
'<div class="niputv-player-popu topplay">' +
'<div style="background: url(/static/player/img/niputv-player-ico.png) 0px -250px no-repeat" class="niputv-player-popu topplay-ico" id="control-topplay"></div>' +
'</div>' +
'<div class="niputv-player-video"><video src="" id="video" controls="controls" autobuffer></video></div>' +
'<div class="niputv-player-control main" id="niputv-player-control">' +
'<div id="sharpness-important" style="display: none"></div>' +
'<div id="play-filling_all" style="height: 28px;width: 100%;position: relative" ;>' +
'<div class="niputv-player-control-timeline main"><div class="niputv-player-control-timeline filling" id="play-filling"></div></div>' +
'</div>' +
'<div class="niputv-player-control bottom">' +
'<div class="niputv-player-volume-poup" id="control-volume">' +
'<div class="niputv-player-volume-poup_control">' +
'<div class="niputv-player-volume-poup_controlfilling" role="progressbar" aria-valuemin="0" aria-valuemax="100"></div>' +
'</div>' +
'</div>' +
'<div class="niputv-player-sharpness-poup main" id="video_sharpness_list" style="display: none" onselectstart="return false"></div>' +
'<!--<div class="niputv-player-sharpness-poup a" data-sharpness="360P">360P</div>-->' +
'<div class="niputv-player-control play" style="background: url(/static/player/img/niputv-player-ico.png) 0px 0px no-repeat" id="control-play"></div>' +
'<div class="niputv-player-control time">' +
'<span id="play-nowtime">00:00</span> / <span id="play-total_length">00:00</span>' +
'</div>' +
'<div class="niputv-player-control full_screen" style="background: url(/static/player/img/niputv-player-ico.png) 0px -55px no-repeat" id="video-FullScreen"></div>' +
'<div class="niputv-player-control full_screen" style="background: url(/static/player/img/niputv-player-ico.png) 0px -105px no-repeat" id="control-volume_butt"></div>' +
'<div class="niputv-player-control video_sharpness" id="control-video_sharpness" onselectstart="return false"></div>' +
'</div></div></div>')

setTimeout(function () {
    //提取filekey
    function getFileName(path) {
        var index = path.lastIndexOf("\/");
        path = path.substring(index + 1, path.length);
        return path
    }

    //写入播放器清晰度选择
    function insert_video_sharpness(data) {
        if (data['type'] == true) {
            $("#video_sharpness_list").prepend('<div class="niputv-player-sharpness-poup a" data-sharpness="' + data[
                'datacalss'] + '">' + data['calss'] + '</div>')
        }
    }

    //视频播放缓冲提示
    $('#video').on('waiting', function () {
        $(".niputv-player-popu.buffer").fadeIn()
    });
    $('#video').on('canplay', function () {
        $(".niputv-player-popu.buffer").fadeOut()
    });

    //data-key='{"key": "2.mp4", "360": true, "480": true, "720": true,
    //"1080": true, "2k": false, "4k": false}

    //获取数据 数据格式化
    var getvideofile = $("#videokey").data("key")
    var videoptype_list = [{
            "calss": "360P",
            "datacalss": "360p",
            "type": getvideofile['360']
        },
        {
            "calss": "480P",
            "datacalss": "480p",
            "type": getvideofile['480']
        },
        {
            "calss": "720P",
            "datacalss": "720p",
            "type": getvideofile['720']
        },
        {
            "calss": "1080P",
            "datacalss": "1080p",
            "type": getvideofile['1080']
        },
        {
            "calss": "2K",
            "datacalss": "2k",
            "type": getvideofile['2k']
        },
        {
            "calss": "4K",
            "datacalss": "4k",
            "type": getvideofile['4k']
        },
    ]

    //获取视频720P清晰度
    var video_sharpness720p = getvideofile['720']
    //提取filekey
    var filekey = getFileName(getvideofile['key'])
    //解析filekey
    var videofilekey = filekey.substring(0, filekey.lastIndexOf("."));

    //视频清晰度优先排序
    if (getvideofile['360'] == true) {
        $("#control-video_sharpness").html("360P")
        $("#video").attr("src", videobucket + filevar + videofilekey + '-360p.mp4')
    }
    if (getvideofile['480'] == true) {
        $("#control-video_sharpness").html("480P")
        $("#video").attr("src", videobucket + filevar  + videofilekey + '-480p.mp4')
    }
    if (video_sharpness720p == true) {
        $("#control-video_sharpness").html("720P")
        $("#video").attr("src", videobucket + filevar  + videofilekey + '-720p.mp4')
    }

    //循环写入可选清晰度
    $.each((videoptype_list),
        function () {
            insert_video_sharpness(this)
        });

    /**播放器主体**/
    var video = document.getElementById("video");

    /**现在播放时间-视频总时长**/
    var play_nowtime = document.getElementById("play-nowtime");
    var play_total_length = document.getElementById("play-total_length");

    /**视频播放进度条**/
    var player_filling_all = document.getElementById("play-filling_all");
    var player_filling = document.getElementById("play-filling");

    /**播放控件**/
    var video_playbutt = document.getElementById("control-play");
    $('body, html').bind('mousemove', function (e) {
        $("#niputv-player-control").hover(function () {
            $("#niputv-player-control").stop(true, false).animate({
                'opacity': '1'
            });
        }, function () {
            $("#niputv-player-control").stop(true, false).animate({
                'opacity': '0'
            });
        });
    })

    //格式化时间
    function formatTime(time) {
        var hour = Math.floor(time / 3600);
        var other = time % 3600;
        var minute = Math.floor(other / 60);
        var second = (other % 60).toFixed(0);
        var showTime = hour + ':' + minute + ':' + second;
        return showTime;
    };

    //监听esc全屏退出
    $(window).keyup(function (event) {
        event = event || window.event;
        if (event.keyCode == 27) {
            exitFullscreen()
        };
        event.preventDefault();
        a = 0
        return a
    });

    //全屏按钮
    $('#video-FullScreen').on('click', function() {
        if (!document.webkitIsFullScreen) {
            $(".niputv-player").css("max-width", "100%")
            $(".niputv-player").css("max-height", "100%")
            $("#player").css({"position":"fixed","top":"0","bottom":"0","left":"0","right":"0","z-index":"99999999999999999"})
            $("body").css("overflow", "hidden")
    
            var ele = document.documentElement;
            if (ele.requestFullscreen) {
                ele.requestFullscreen();
                $("#niputv-player").requestFullscreen()
            } else if (ele.mozRequestFullScreen) {
                ele.mozRequestFullScreen();
                $("#niputv-player").mozRequestFullScreen()
            } else if (ele.webkitRequestFullScreen) {
                ele.webkitRequestFullScreen();
                $("#niputv-player").webkitRequestFullScreen()
            }
        } else {
            $(".niputv-player").css("max-width", "1280px")
            $(".niputv-player").css("max-height", "720px")
            $("#player").css({"position":"inherit","top":"inherit","bottom":"inherit","left":"inherit","right":"inherit","z-index":"inherit"})
            $("body").css("overflow", "inherit")
            var de = document;
            if (de.exitFullscreen) {
                de.exitFullscreen();
            } else if (de.mozCancelFullScreen) {
                de.mozCancelFullScreen();
            } else if (de.webkitCancelFullScreen) {
                de.webkitCancelFullScreen();
            }
        }
    });

    $(function(){
        $(window).keydown(function (event) {
           if (event.keyCode == 27) {
            $(".niputv-player").css("max-width", "1280px")
            $(".niputv-player").css("max-height", "720px")
            $("#player").css({"position":"inherit","top":"inherit","bottom":"inherit","left":"inherit","right":"inherit","z-index":"inherit"})
            var de = document;
            if (de.exitFullscreen) {
                de.exitFullscreen();
            } else if (de.mozCancelFullScreen) {
                de.mozCancelFullScreen();
            } else if (de.webkitCancelFullScreen) {
                de.webkitCancelFullScreen();
            }
           }
       });
   });

    //统一播放调用
    function play() {
        this.controls = true;
        if (video.paused) {
            video.play()
            video_playbutt.style.cssText = "background: url(/static/player/img/niputv-player-ico.png) -100px -0px no-repeat";
            $("#control-topplay").fadeOut()
            $("#niputv-player-playover").fadeOut()
        } else {
            $("#control-topplay").fadeIn()
            video.pause()
            video_playbutt.style.cssText = "background: url(/static/player/img/niputv-player-ico.png) 0px 0px no-repeat";
        }
    };

    //切换声音静音状态
    $('#control-volume_butt').on('click', function () {
        if (video.muted == true) {
            video.muted = false;
            $('#control-volume_butt').attr("style",
                "background: url(/static/player/img/niputv-player-ico.png) 0px -105px no-repeat")
        } else {
            video.muted = true;
            $('#control-volume_butt').attr("style",
                "background: url(/static/player/img/niputv-player-ico.png) 0px -155px no-repeat")
        }
    });

    //捕获音量条点击
    $('.niputv-player-volume-poup_control').on('click mousewheel DOMMouseScroll', function (e) {
        e = e || window.event;
        volumeControl(e);
        e.stopPropagation();
        return false;
    });

    //console.log($('video')[0].volume)

    volumedata = localStorage.getItem("niputv_player_volume");
    if(volumedata == null){
        $('video')[0].volume = 0.50;
        $('.niputv-player-volume-poup_controlfilling').css('height','50%');
        var percentage = 0;
    }else{
        $('video')[0].volume = parseFloat(volumedata);
        percentage = localStorage.getItem("niputv_player_ui")
        $('.niputv-player-volume-poup_controlfilling').css('height', percentage + '%');
    }

    //传入音量条点击更新音量
    function volumeControl(e) {

        e = e || window.event;
        var eventype = e.type;
        var delta = (e.originalEvent.wheelDelta && (e.originalEvent.wheelDelta > 0 ? 1 : -1)) || (e.originalEvent.detail &&
            (e.originalEvent.detail > 0 ? -1 : 1));
        var positions = 0;
        var percentage = 0;
        if (eventype == "click") {
            positions = $('.niputv-player-volume-poup_control').find('.niputv-player-volume-poup_controlfilling').offset()
                .top - e.pageY;
            percentage = 100 * (positions + $('.niputv-player-volume-poup_control').find(
                '.niputv-player-volume-poup_controlfilling').height()) / $('.niputv-player-volume-poup_control').height();
        } else if (eventype == "mousewheel" || eventype == "DOMMouseScroll") {
            percentage = 100 * ($('.niputv-player-volume-poup_control').find(
                '.niputv-player-volume-poup_controlfilling').height() + delta) / $(
                '.niputv-player-volume-poup_control').height();
        }
        if (percentage < 0) {
            percentage = 0;
        }

        if (percentage >= 100) {
            percentage = 100;
        }
        $('.niputv-player-volume-poup_controlfilling').css('height', percentage + '%');
        localStorage.setItem("niputv_player_ui", parseInt(percentage));
        //console.log(parseInt(percentage))

        var nowv = percentage / 100;
        $('video')[0].volume = nowv
        e.stopPropagation();
        e.preventDefault();
        localStorage.setItem('niputv_player_volume', $('video')[0].volume.toString());
    }
    //volumeControl(e)

    //音量悬浮显示
    var timer = null;
    $('#control-volume_butt').on('mouseover', function () {
        clearInterval(timer);
        $('#control-volume').css('display', 'block');
    });
    $('#control-volume_butt').on('mouseout', function () {
        clearInterval(timer);
        timer = setTimeout(function () {
            $('#control-volume').css('display', 'none');
        }, 200);
    });

    //播放键绑定
    $("#control-play").click(function () {
        play()
    })

    //最上层播放建绑定
    $("#control-topplay").click(function () {
        play()
        $("#control-topplay").fadeOut()
    })

    //点击视频主体绑定
    $("#video").click(function () {
        play()
    })

    //捕获进度条点击
    var timeDrag = false;
    $('#play-filling_all').mousedown(function (e) {
        timeDrag = true;
        updatebar(e.pageX);
    });
    $(document).mouseup(function (e) {
        if (timeDrag) {
            timeDrag = false;
            updatebar(e.pageX);
        }
    });
    $(document).mousemove(function (e) {
        if (timeDrag) {
            updatebar(e.pageX);
        }
    });

    //清晰度选择卡弹出隐藏
    $("#control-video_sharpness").click(function (e) {
        $("#video_sharpness_list").toggle()
    })

    //调用视频清晰度隐藏选项卡打开提示
    function sharpness_important(data) {
        $("#sharpness-important").fadeIn({
            duration: 300
        });
        $("#sharpness-important").html('正在为你切换清晰度至' + data)
    }

    //点中清晰度后调用选项卡处理和传入被点中的清晰度交由切换包处理
    $(function () {
        $('#video_sharpness_list').on('click', '.niputv-player-sharpness-poup.a', function () {
            data = $(this).data("sharpness")
            $('#control-video_sharpness').html(data);
            $("#video_sharpness_list").toggle()
            sharpness_important(data)
            video_sharpness(data)
        });
    });

    //解析视频key+清晰度组合新的地址进行视频加载地址切换
    function video_sharpness(sharpness) {
        //alert(sharpness)
        var currentTimeBak = video.currentTime;
        $("#video").attr("src", videobucket + filevar + videofilekey + '-' + sharpness + '.mp4')
        video.currentTime = currentTimeBak;
        play()
        $("#sharpness-important").html('以为你切换到' + sharpness)
        setTimeout(function () {
            $('#sharpness-important').fadeOut({
                duration: 1000
            }); //找到对应的标签隐藏
        }, 2200) //3000是表示3秒后执行隐藏代码
    }

    //统一进度条更新
    var updatebar = function (x) {
        var progress = $('#play-filling_all');
        var maxduration = video.duration;
        var position = x - progress.offset().left;
        var percentage = 100 * position / progress.width();

        if (percentage > 100) {
            percentage = 100;
        }
        if (percentage < 0) {
            percentage = 0;
        }

        //Update progress bar and video currenttime
        $('#play-filling').css('width', percentage + '%');
        video.currentTime = maxduration * percentage / 100;
    };

    //视频播放时间返回api 监听时间
    video.addEventListener("loadedmetadata", function () {
        var duration = video.duration;
        var showTime = formatTime(duration);
        play_total_length.innerHTML = showTime
    });

    //调用格式化时间传递新的时间格式到播放器
    video.addEventListener('timeupdate', function () {
        var currentTime = video.currentTime; //Get currenttime
        var showTime = formatTime(currentTime);
        var maxduration = video.duration; //Get myVideo duration
        var percentage = 100 * currentTime / maxduration; //in %
        player_filling.style.cssText = "width:" + percentage + "%";
        play_nowtime.innerHTML = showTime
    });

    //播放完成提示 重新播放按钮绑定
    $("#controls-rplay").click(function () {
        play()
    })

    //监听视频播放完成事件
    video.addEventListener('ended', function () {
        video_playbutt.style.cssText = "background: url(/static/player/img/niputv-player-ico.png) 0px 0px no-repeat";
        $("#niputv-player-playover").fadeIn()
    });
})