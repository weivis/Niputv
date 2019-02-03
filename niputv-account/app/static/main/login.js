    $("head").prepend('<style>body{background-image: url(http://picdns.niputv.com/account/background/20181025.jpg);background-position: center;margin: 0}' +
    '.page-wp{max-width: 1600px;width: 90%;margin: 0 auto;overflow: hidden;position: relative}' +
    '.logo{float: left;}' +
    '.top{height: 465px;width: 100%;background-image: url(/static/img/header-shon.png);background-repeat: repeat-x;overflow: hidden}' +
    '.header{margin-top: 50px;}' +
    '.headernav{float: right}' +
    '.headernav a{float: right;color: #fff;margin-left: 30px;font-size: 14px;}' +
    'a{text-decoration: none}' +
    '.footer{position: absolute;bottom: 50px;left: 0;right: 0;color: #fff;font-size: 12px;}' +
    '.loginbox{width: 320px;height: 277px;position: absolute;right: 0;top: 0; bottom: 0;margin: auto; background-image: url(/static/img/login-backgroundcolor.png);border-radius: 5px 5px 5px 5px;overflow: hidden;}' +
    '.login-inputnbox{height: 227px;width: 100%}' +
    '.loginbutt{width: 100%;height: 50px;background-color: #e40056;font-size: 14px;color: #fff;text-align: center;line-height: 50px;border-radius: 5px;}' +
    '.login-inputwp{width: calc(100% - 40px);margin: 0 auto;margin-bottom: 20px;}' +
    '.login-title{width: 100%;height: 63px;font-size: 14px;color: #fff;line-height: 63px;}' +
    '.login-input{border-radius: 5px;background-color: #fff;width: 100%;height: 39px;border: 0px;padding-left: 10px;}</style>')
    $("#login").click(function () {
        if ($("#account").val() == '') {
            alert('账号不能为空')
        } else {
            if ($("#password").val() == '') {
                alert('密码不能为空')
            } else {
                $.ajax({
                    url: '#', //api
                    type: 'POST',
                    data: JSON.stringify({
                        "account": $("#account").val(),
                        "password": $("#password").val(),
                        "login_long": $("#login_long").is(':checked'),
                    }), //数据
                    async: true,
                    cache: false,
                    contentType: "application/json; charset=utf-8",
                    processData: false,
                    dataType: 'json',
                    success: function (returndata) {
                        if (returndata['code'] == 1){
                            $(window).attr('location','http://www.niputv.com/');
                        }else{
                            alert(returndata['text'])
                        }
                    },
                    error: function (returndata) {
                        alert('系统繁忙')
                    }
                });
            }
        }
    })