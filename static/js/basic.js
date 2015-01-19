// JavaScript Document
//改变div状态
var isTag0 = "";//对应标签
var isTag1 = "";//对应地址
var isTag2 = "";//对应分类Key,AddressOfId,Classify
var isTag3 = "";

function ChangeColor(changediv,color,e)
{
	$("#"+changediv).css("background",color);
}

//

function TurnOut()
{
	
		$('.theme-popover-mask').fadeIn(100);
		$('.theme-popover').slideDown(200);
}

function Disappear()
{
	
		$('.theme-popover-mask').fadeOut(100);
		$('.theme-popover').slideUp(200);
}

//通过服务器端获取另外13个产品推介信息
function GetAntherThirteen()
{
}

//功能的开启关闭
	//添加标记点
function StartPointPaint(id1,color1,id2,color2)
{
	map.addEventListener("click", showInfo);
	ChangeColor(id1,color1);
	ChangeColor(id2,color2);
	
}
function StopPointPaint(id1,color1,id2,color2)
{
	map.removeEventListener("click", showInfo);	
	ChangeColor(id1,color1);
	ChangeColor(id2,color2);
}
	//鼠标测距
function StartGetMouseDis(id1,color1,id2,color2)
{
	ChangeColor(id1,color1);
	ChangeColor(id2,color2);
	myDis = new BMapLib.DistanceTool(map);
	myDis.open();  //开启鼠标测距	
	
}

function StopGetMouseDis(id1,color1,id2,color2)
{
	ChangeColor(id1,color1);
	ChangeColor(id2,color2);
	myDis.close();  //关闭鼠标测距
}
//添加矩形选框
function StartAddPolygon()
{
	
}

function AreaChoiceFirst(id1,id2,id3)
{
	$("#"+id1).fadeIn(100);
	$("#"+id1).slideDown(200);
	if($("#"+id2).css("display") == "block")
	{
		$("#"+id2).css("display","none");
	}
	if($("#"+id3).css("display") == "block")
	{
		$("#"+id3).css("display","none");
	}
}
//返回坐标点，并调用函数写出来在地图上
function GetCoordinate1(id)
{
	var productions = GetFromService(null,id,cor);
	AddContent(productions);//需要从服务器返回id对应的名字字
	ClearChooseDiv('connect-map-id');
	AddRecDiv(Name);
}

function SearchOccurByDormitory(id)
{
	var i=0;
	var j=0;
	ClearChooseDiv('connect-map-id');
	isTag3 = id;
	var jsonObject = GetFromService(isTag0,isTag1,isTag2, isTag3);
	while(jsonObject.dormitories[i] != null)
	{
		var x = jsonObject.dormitories[i].longitude;
		var y = jsonObject.dormitories[i].latitude;
		var id = jsonObject.dormitories[i].dormitory_id;
		var name = jsonObject.dormitories[i].dormitory_name;
		if(i==0)
		{
			LocateAsCenter(x,y);
			CloseTag("close3");
			AddContent(name,"close3");//需要从服务器返回id对应的名字
		}
		showPoint(x,y,id);			
		i++;
	}
	while(jsonObject.productions[j] != null)
	{
		var Price = jsonObject.productions[j].price;
		var PubTime = jsonObject.productions[j].time;
		var DormId = jsonObject.productions[j].dormitory_id;
		var DormName = jsonObject.productions[j].dormitory_name;
		var ProNum = jsonObject.productions[j].number;
		var ProName = jsonObject.productions[j].title;
		var id = jsonObject.productions[j].id;
		AddRecDiv(DormName+":"+"￥"+Price+"  "+ProName+"×"+ProNum,id);
		j++;
	}	
}
function GetCoordinate(id)
{
	var i=0;
	var j=0;
	ClearChooseDiv('connect-map-id');
	isTag1 = id;
	var jsonObject = GetFromService(isTag0,isTag1,isTag2, isTag3);
	while(jsonObject.dormitories[i] != null)
	{
		var x = jsonObject.dormitories[i].longitude;
		var y = jsonObject.dormitories[i].latitude;
		var id = jsonObject.dormitories[i].dormitory_id;
		var name = jsonObject.dormitories[i].dormitory_name;
		if(i==0)
		{
			LocateAsCenter(x,y);
			CloseTag("close1");
			AddContent(name,"close1");//需要从服务器返回id对应的名字
		}
		showPoint(x,y,id);			
		i++;
	}
	while(jsonObject.productions[j] != null)
	{
		var Price = jsonObject.productions[j].price;
		var PubTime = jsonObject.productions[j].time;
		var DormId = jsonObject.productions[j].dormitory_id;
		var DormName = jsonObject.productions[j].dormitory_name;
		var ProNum = jsonObject.productions[j].number;
		var ProName = jsonObject.productions[j].title;
		var id = jsonObject.productions[j].id;
		AddRecDiv(DormName+":"+"￥"+Price+"  "+ProName+"×"+ProNum,id);
		j++;
	}	
}

function GetCoordinate2(id){
	
	var a = GetFromService(null,id);
	AddContent(id);//需要从服务器返回id对应的名字
	var EachMail = new Array();
	EachMail = a.split("_");
	ClearChooseDiv('connect-map-id');
	for(i=0;i<EachMail.length;i++)
	{
		var CutSide = new Array();
		CutSide = EachMail[i].split("-");
		Name = CutSide[0];
		AddRecDiv(Name);
		Coordinate = CutSide[1];
		var CoordinateTwice = new Array();
		CoordinateTwice = Coordinate.split(",");
		x=CoordinateTwice[0];
		y=CoordinateTwice[1];
		if(i==0)
		{
			LocateAsCenter(x,y);
		}
			showPoint(x,y,id);		
	}
	}

//添加了搜索限制之后，需要向服务器发送一条请求，告诉服务器用户添加了限制。
//function AddContent(ConTent)
//{
	//for(var i = 0;i<4;i++)
	//{
		//if($("#Close"+i).css("display") == "none")
	//	{
		//	document.getElementById("Close"+i).innerHTML += ConTent;
			//$("#Close"+i).css("display","block");
			//return 0;		
		//}		
	//}	
//}
function AddContent(ConTent,idName)
{
		var pDiv=document.createElement('div');
		pDiv.className = 'onefive-div-tagsmall';
		var pa = document.createElement('a');
		pa.className = 'close';
		pa.innerHTML = '×';
		pDiv.id = idName;				
		document.getElementById("tag_div").appendChild(pDiv);
		document.getElementById(pDiv.id).innerHTML += ConTent;
		pa.addEventListener("click",function(){CloseTag(pDiv.id);});
		pDiv.appendChild(pa);		
}
//显示推荐的信息
function AddRecDiv(Intro,id)
{
	var newDiv=document.createElement("div");
	newDiv.className = "connect_map_intro";
	var txt = document.createTextNode(Intro);
	newDiv.addEventListener("click",function(){window.open('/p/'+id.toString()+'/');});
	newDiv.appendChild(txt);
	document.getElementById("connect-map-id").appendChild(newDiv);
}

//关闭之后需要向服务器发送一条请求，告诉服务器用户的限定少了。
function CloseTag(ID)
{
	//var content = document.getElementById(ID).text();
	//alert(content);
	if(ID == "close0")
	{
		var isTag0 = null;
	}
	if(ID == "close1")
	{
		var isTag1 = null;
	}
	if(ID == "close2")
	{
		var isTag2 = null;
	}
	if(ID == "close3")
	{
		var isTag3 = null;
	}
	$("#"+ID).remove();	
	
}
//清空推荐的信息
function ClearChooseDiv(divName)
{
	document.getElementById(divName).innerHTML = "";
}

function SearchSubmit(id)
{
	var Tag=document.getElementById(id).value;
	CloseTag("close0");
	AddContent(Tag,"close0");
	isTag0 = Tag;
	var i=0;
	var j=0;
	ClearChooseDiv('connect-map-id');
	var jsonObject = GetFromService(isTag0,isTag1,isTag2, isTag3);
	while(jsonObject.dormitories[i] != null)
	{
		var x = jsonObject.dormitories[i].longitude;
		var y = jsonObject.dormitories[i].latitude;
		var id = jsonObject.dormitories[i].dormitory_id;
		if(i==0)
		{
			LocateAsCenter(x,y);
		}
		showPoint(x,y,id);			
		i++;
	}
	while(jsonObject.productions[j] != null)
	{
		var Price = jsonObject.productions[j].price;
		var PubTime = jsonObject.productions[j].time;
		var DormId = jsonObject.productions[j].dormitory_id;
		var DormName = jsonObject.productions[j].dormitory_name;
		var ProNum = jsonObject.productions[j].number;
		var ProName = jsonObject.productions[j].title;
		var id = jsonObject.productions[j].id;
		AddRecDiv(DormName+":"+"￥"+Price+"  "+ProName+"×"+ProNum,id);
		j++;
	}	
}

function ClassifyChoice(id)
{
	var Tag=document.getElementById(id).innerText;
	CloseTag("close2");
	AddContent(Tag,"close2");
	isTag2 = Tag;
	var i=0;
	var j=0;
	ClearChooseDiv('connect-map-id');
	var jsonObject = GetFromService(isTag0,isTag1,isTag2, isTag3);
	while(jsonObject.dormitories[i] != null)
	{
		var x = jsonObject.dormitories[i].longitude;
		var y = jsonObject.dormitories[i].latitude;
		var id = jsonObject.dormitories[i].dormitory_id;
		if(i==0)
		{
			LocateAsCenter(x,y);
		}
		showPoint(x,y,id);			
		i++;
	}
	while(jsonObject.productions[j] != null)
	{
		var Price = jsonObject.productions[j].price;
		var PubTime = jsonObject.productions[j].time;
		var DormId = jsonObject.productions[j].dormitory_id;
		var DormName = jsonObject.productions[j].dormitory_name;
		var ProNum = jsonObject.productions[j].number;
		var ProName = jsonObject.productions[j].title;
		var id = jsonObject.productions[j].id;
		AddRecDiv(DormName+":"+"￥"+Price+"  "+ProName+"×"+ProNum,id);
		j++;
	}	
}

function SearchSubmit1(id)
{
	
}

//类目标签
function AddTermDiv(id)
{
	$("#"+id).fadeIn(100);
}
function ChangeAndMakeSure(id)
{
	document.getElementById('itemChoice').innerHTML = "";
	$('#itemChoice').append($("#"+id).text());
	$('#itemChoiceFirst').css("display","none");
}


//

//

//

//

//

//

//

//

//

//单个物品售卖栏仅有
function OverWhichPic(id)
{
	for(i=0;i<4;i++)
	{
		$("#"+"linkDownpic"+i).css("visibility","hidden");
	}
	$("#"+"link"+id).css("visibility","visible");
}

//规划步行路线
function GetAddressName(id1,id2)
{
	var Name1=document.getElementById(id1).value;
	var Name2=document.getElementById(id2).value;
	OnWalk(Name1,Name2);
}