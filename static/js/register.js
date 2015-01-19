// JavaScript Document
function isnull(id1,id2)
{
	if(document.getElementById(id1).value.length == 0)
	{
		document.getElementById(id2).innerHTML = "请输入";
		 document.getElementById(id1).focus();
	}
	else
		 {
			 document.getElementById(id2).innerHTML = "";
		}
}
function checkpassword(id1,id2)
{
	var value1 = document.getElementById(id1).value;
	var value2 = document.getElementById(id2).value;
	if(value1 != value2)
	{
		document.getElementById('notsame').innerHTML = "两次输入不相同";
		document.getElementById(id1).focus();
	}
	else
		 {
			 document.getElementById('notsame').innerHTML = "";
			 isnull(id2,'notsame')
		}
}

function isemail(id){ 
  		 var strEmail = document.getElementById(id).value;
         var regEmail = /^([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\-|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
         var matchArray = strEmail.match(regEmail);
         if(matchArray == null){
                document.getElementById('notmail').innerHTML = "不是一个邮箱";
                document.getElementById(id).focus();
               
         }
		 else
		 {
			 document.getElementById('notmail').innerHTML = "";
			 isnull(id,'notmail')
		}
  }
 
function submitrigster()
{
	id = document.getElementById('yonghuming').value;
	pa = document.getElementById('password1').value;
	ad = document.getElementById('mailaddress').value;
	$.ajax({
		'type': 'POST',
		'url': '/account/register',
		'data': {'username': id, 'password': pa, 'email': ad, }
		},function(data){
			return data;
	}
	)
}