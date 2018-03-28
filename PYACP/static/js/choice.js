/**
 * Created by Twy on 2017/11/22.
 */
$(document).ready(function(){

    // 添加选择选中的样式
	$('.list-group-item').click(function(){
		var answer=$(this).text();
		$(this).parent().children().removeClass('active');
		$(this).addClass('active');
		$(this).parent().children('input').attr({'value':answer});
	});

	// AJAX POST数据到后台
    $('#submit').click(function () {
        var answers = {};
        var errors = [];
        var errors_list = [];
        var patt1=new RegExp("[0-9a-zA-Z,]+");
        var csrf_token=$.cookie('csrftoken');
        for(var i=1;i<=5;i++)
        {
             answers[i]=$('#answer'+i).val();
        }
        var json_answer=JSON.stringify(answers);

        $.ajax({
            url:'course_choice/',
            data:{
                'answers':json_answer,
                'csrfmiddlewaretoken':csrf_token
            },
            type:'POST',
            dataTpye:'json',
            success:function (data) {
                for(var i=1;i<=5;i++)
                {
                    $('#choice_title'+i).attr({'style':'color:black;'});
                    if(typeof (data[i])!=='undefined')
                    {
                        $('#choice_title'+i).attr({'style':'color:red;'});
                        errors.push(i);
                    }
                }
                errors_list=JSON.stringify(errors);
                a=patt1.exec(errors_list.toString());
                alert('第'+patt1.exec(errors_list.toString())+'题错误！请更改')
            }
        })
    });
});