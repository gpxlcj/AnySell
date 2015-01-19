// JavaScript Document
//所有的数据都通过该函数返回与获取。
function GetFromService2(Tag,AddressOfId)
{
	if(Tag != null)
	{
		var a ="梅6.电吹风-114.370505,30.542561_梅2.雨伞-114.37046,30.542817_梅3.数据库的书-114.371116,30.543292_梅4.飞利浦电吹风-114.371448,30.542639_梅5.一个大苹果-114.371942,30.542802_梅2.大棒子-114.37046,30.542817_梅2.雨伞-114.37046,30.542817";
	}
	if(AddressOfId != null)
	{
		if(AddressOfId == "001_17_01_01_001_0106")
		{var a ="梅2.电吹风-114.370505,30.542561_梅2.雨伞-114.37046,30.542817_梅2.数据库的书-114.371116,30.543292_梅4.飞利浦电吹风-114.371448,30.542639_梅5.一个大苹果-114.371942,30.542802_梅2.大棒子-114.37046,30.542817_梅2.雨伞-114.37046,30.542817";}
	}
	return a;			
}

function GetFromService0(Key,AddressOfId,Classify)
{
	var jsonObject={"status": 11101, "dormitories": [{"latitude":30.542561, "longitude": 114.370505, "dormitory_id": 33,"dormitory_name":"梅园六舍"}], "productions": [{"price": 11.0, "time": "2015-01-17 08:35:07.873055+00:00", "dormitory_id": 33, "number": 2, "title": "A","dormitory_name":"梅园六舍","id":"4300"}, {"price": 2.0, "time": "2015-01-17 08:34:52.904884+00:00", "dormitory_id": 33, "number": 2, "title": "B","dormitory_name":"梅园三舍","id":"4301"}]}

	return jsonObject;			
}

function GetFromService(Key,AddressOfId,Classify,dormitory_id)
{
	//var URL = "0.0.0.0:8080/api/purchase/research/?district=2012&dormitory=33&keyword=e&category=c";
	if (Key==null)
		Key = ""
	if (Classify==null)
		Classify = ""
	var a = $.ajax({
    		type:     "GET",
		url:      "http://0.0.0.0:8080/api/purchase/research/?district="+AddressOfId+"&dormitory="+dormitory_id+"&keyword="+Key+"&Classify="+Classify ,
		dataType: "json",
		async:    false,
		success:  function(data) {
			return data
    		}
	});
	a = a.responseJSON;
	return a;

}

