var information_btn = document.getElementById('index-top-information_fun');
var information_popup = document.getElementById('index-top_information-div');
var usermp_header = document.getElementById('index-top_head-ui');
var usermp_popup = document.getElementById('index-top_user-div');
var infoclose = document.getElementById('index-top_information-close-margin');

/*1.信息弹窗触发*//*2.信息弹窗显示*/
document.addEventListener('click', function(e) {
    if (e.target !== information_btn ) {
    information_popup.style.display = 'none';
  }
});

information_popup.addEventListener('click', function(e) {
  e.stopPropagation();
})

information_btn.addEventListener('click', function(e) {
  var status1 = information_popup.style.display;

  if (status1 === 'none') {
    information_popup.style.display = 'block';
  } else {
    information_popup.style.display = 'none';
  }
})

/*头像触发-用户个人名片状态*/
document.addEventListener('click', function(e) {
  if (e.target !== usermp_header) {
    usermp_popup.style.display = 'none';
  }
});

usermp_popup.addEventListener('click', function(e) {
  e.stopPropagation();
})

usermp_header.addEventListener('click', function(e) {
  var status2 = usermp_popup.style.display;

  if (status2 === 'none') {
    usermp_popup.style.display = 'block';
  } else {
    usermp_popup.style.display = 'none';
  }
})


infoclose.addEventListener('click', function(){
	usermp_popup.style.display = 'none';
})
