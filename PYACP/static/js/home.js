/**
 * Created by Administrator on 2017/11/6.
 */

$(document).ready(function(){
    dropdownOpen();//调用
});
function dropdownOpen() {

    var $dropdownLi = $('li.dropdown');

    $dropdownLi.mouseover(function() {
        $(this).addClass('open');
    }).mouseout(function() {
        $(this).removeClass('open');
    });
}

//固定产品条，jquery老是出问题，故用js
window.onscroll = function(){
    var t = document.documentElement.scrollTop || document.body.scrollTop;
    var top_div = document.getElementById( "row_nav" );
    if( t >= 47 ) {
        top_div.classList.add('navbar-fixed-top');
    }
    else {
        top_div.classList.remove('navbar-fixed-top');
    }
};

// 登录时发送ajax请求，失败则获取字符串
$('#loginbutton').click(function () {
    var username = $('#loginname').val();
    var password = $('#loginpassword').val();
    var csrf_token=$.cookie('csrftoken');
    $.ajax({
        url:'http://127.0.0.1:8000/home/loginpage',
        data:{
            'username':username,
            'password':password,
            'csrfmiddlewaretoken':csrf_token
        },
        type:'POST',
        dataTpye:'json',
        success:function (data) {
            if (data['turn']){
                // 跳转到当前页
                location.replace('/home/center')
                // location.href='/home/center'
            }else {
                // 弹出提示 用户名/密码错误
                $('#loginwarning').html(data['error']).css('display','block');
            }
    }})
});
// 点击提交时ajax判断用户是否存在
$('#regbutton').click(function () {
    var username=$('#regname').val();
    var password = $('#regpassword').val();
    var passwrordagain = $('#regpasswrodagain').val();
    var email = $('#email').val();
    var captcha_reg = $("#captcha_reg").val();
    var hash_reg = $('#hash_reg').val();
    var csrf_token=$.cookie('csrftoken');

    $.ajax({
        url:'http://127.0.0.1:8000/home/reg',
        data:{
            'username': username,
            'password': password,
            'passwordagain': passwrordagain,
            'email':email,
            "captcha_reg": captcha_reg,
            'hash_reg': hash_reg,
            'csrfmiddlewaretoken':csrf_token
        },
        dataType:'json',
        type:'POST',
        success:function (data) {
            if (data['turn'])
            {
                // 跳转到当前页
                location.href='home/send_email'
            }
            else
            {
                $('#namewarning').hide();
                $('#passwordwarning').hide();
                $('#password2warning').hide();
                $('#emailwarning').hide();
                $('#captchawarning').hide();
                // 弹出提示 用户名/密码错误
                if(typeof (data['error_name'])!=='undefined')
                {
                    $('#namewarning').html(data['error_name']).css({'display':'block','color':'red'});
                }
                else if(typeof (data['error_password'])!=='undefined')
                {
                    $('#passwordwarning').html(data['error_password']).css({'display':'block','color':'red'});
                }
                else if(typeof (data['error_password_again'])!=='undefined')
                {
                    $('#password2warning').html(data['error_password_again']).css({'display':'block','color':'red'});
                }
                else if(typeof (data['error_email'])!=='undefined')
                {
                    $('#emailwarning').html(data['error_email']).css({'display':'block','color':'red'});
                }
                else if(typeof (data['error_captcha'])!=='undefined')
                {
                    $('#captchawarning').html(data['error_captcha']).css({'display':'block','color':'red'});
                }
            }
        }
    })
});

// 找回密码

$('#findbutton').click(function () {
    var username=$('#findname').val();
    var email=$('#findaddress').val();
    var newpassword=$('#newpassword').val();
    var captcha_findpassword = $("#captcha_findpassword").val();
    var hash_findpassword = $('#hash_findpassword').val();
    var csrf_token=$.cookie('csrftoken');

    $.ajax({
        url:'http://127.0.0.1:8000/home/findpassword',
        dataType:'json',
        type:'POST',
        data:{
            'username':username,
            'email':email,
            'newpassword':newpassword,
            "captcha_findpassword": captcha_findpassword,
            'hash_findpassword': hash_findpassword,
            'csrfmiddlewaretoken':csrf_token
        },
        success:function (data) {
            if(typeof(data['error_captcha'])!=='undefined')
            {
                $('#findcaptcha').html(data['error_captcha']).css({'display':'block','color':'red'})
            }
            else if(typeof(data['error_user'])!=='undefined')
            {
                $('#findwarning').html(data['error_user']).css({'display':'block','color':'red'})
            }
            else if(typeof(data['error_password'])!=='undefined')
            {
                $('#findwarning_password').html(data['error_user']).css({'display':'block','color':'red'})
            }
            else if(typeof(data['success']!=='undefined'))
            {
                location.href='/home/success_find'
            }
        }
    })

});

// 重新获取验证码
$('.re_captcha').click(function () {
    $.ajax({
        url:"http://127.0.0.1:8000/home/re_captcha",
        dataType:'json',
        type:'GET',
        success:function (data) {
            $('.captcha').attr({'src':data['imgage_url']});
            $('#id_reg_captcha_0').attr({'value':data['hashkey']});
        }
    })
});

// regrname 失去焦点时判断用户名是否合法
$('#regname').blur(function () {
    var username = $('#regname').val();
    var uPattern = /^[a-zA-Z0-9_-]{6,15}$/;
    var result = uPattern.test(username);
    if (result === true)
    {
        // 隐藏错误提示
        $('#namewarning').hide()
    }
    else
    {
        // 弹出提示 用户名/密码错误
        $('#namewarning').html('用户名不合法').css({'display':'block','color':'red'});
    }
});

// 找回密码的用户名验证
$('#findname').blur(function () {
    var username = $('#findname').val();
    var uPattern = /^[a-zA-Z0-9_-]{6,15}$/;
    var result = uPattern.test(username);
    if (result === true){
        // 隐藏错误提示
        $('#findwarning').hide();

    }else {
        // 弹出提示 用户名/密码错误
        $('#findwarning').html('用户名不合法！').css({'display':'block','color':'red'});
    }
});

// regpassword 失去焦点时判断密码是否合法
$('#regpassword').blur(function () {
    var password = document.getElementById('regpassword').value;
    var uPattern = /^[a-zA-Z0-9_-]{6,}$/;
    var result = uPattern.test(password);
    if (result === true){
        // 隐藏错误提示
        $('#passwordwarning').hide();

    }else {
        // 弹出提示 用户名/密码错误
        $('#passwordwarning').html('密码不合法').css({'display':'block','color':'red'});
    }
});
// regpasswrodagain 失去焦点时判断两次密码是否一样
$('#regpasswrodagain').blur(function () {
    var password = $('#regpassword').val();
    var passwordagain = $('#regpasswrodagain').val();
    if (password === passwordagain){
        $('#password2warning').hide();
    }else {
        $('#password2warning').html('两次输入密码不一样').css('display','block');
    }
});

// 注册的邮箱验证格式
$('#email').blur(function () {
    var email = $('#email').val();
    var uPattern = /^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}$/;
    var result = uPattern.test(email);
    if (result === true)
    {
        // 隐藏错误提示
        $('#emailwarning').hide()
    }
    else
    {
        // 弹出提示 用户名/密码错误
        $('#emailwarning').html('邮箱格式不合法！').css({'display':'block','color':'red'});
    }
});

//找回密码的邮箱格式验证
$('#findaddress').blur(function () {
    var email = $('#findaddress').val();
    var uPattern = /^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}$/;
    var result = uPattern.test(email);
    if (result === true)
    {
        // 隐藏错误提示
        $('#findwarning_email').hide()
    }
    else
    {
        // 弹出提示 用户名/密码错误
        $('#findwarning_email').html('邮箱格式不合法！').css({'display':'block','color':'red'});
    }
});

// 新的密码格式验证
$('#newpassword').blur(function () {
    var newpassword = $('#newpassword').val();
    var uPattern = /^[a-zA-Z0-9_-]{6,}$/;
    var result = uPattern.test(newpassword);
    if (result === true)
    {
        // 隐藏错误提示
        $('#findwarning_password').hide()
    }
    else
    {
        // 弹出提示 用户名/密码错误
        $('#findwarning_password').html('密码格式不合法！').css({'display':'block','color':'red'});
    }
});

// 回车登录

$(document).keypress(function(event) {
  if (event.keyCode===13)      //keyCode=13是回车键
  {
      var temp1=$('#loginpassword').val();
      var temp2=$('#regpassword').val();
      var temp3=$('#search').val();
      if(temp1!="")
      {
          $('#loginbutton').click();
      }
      else if(temp2!=null&&temp2!=undefined&&temp2!="")
      {
           $('#regbutton').click();
      }
      else if(temp3!=""&&temp2!=' ')
      {
          $('#btn_search').click();
      }
      else
      {

      }
  }
});