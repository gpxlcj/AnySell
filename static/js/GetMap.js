// JavaScript Document
//获取地图

var map;
var myDis;
var address;
// 创建地图实例
function Map(){
	map = new BMap.Map("container");            
	map.centerAndZoom(new BMap.Point(114.37139, 30.544742), 18);	
	map.addControl(new BMap.NavigationControl());// 开启标注工具
	map.enableScrollWheelZoom();  
    var overlays = [];
	var overlaycomplete = function(e){
        overlays.push(e.overlay);
    };
    var styleOptions = {
        strokeColor:"red",    //边线颜色。
        fillColor:"red",      //填充颜色。当参数为空时，圆形将没有填充效果。
        strokeWeight: 3,       //边线的宽度，以像素为单位。
        strokeOpacity: 0.8,	   //边线透明度，取值范围0 - 1。
        fillOpacity: 0.4,      //填充的透明度，取值范围0 - 1。
        strokeStyle: 'solid' //边线的样式，solid或dashed。
    }
    //实例化鼠标绘制工具
    var drawingManager = new BMapLib.DrawingManager(map, {
        isOpen: false, //是否开启绘制模式
        enableDrawingTool: true, //是否显示工具栏
        drawingToolOptions: {
            anchor: BMAP_ANCHOR_TOP_RIGHT, //位置
            offset: new BMap.Size(-30,0), //偏离值
            scale: 0.8 //工具栏缩放比例
        },
        circleOptions: styleOptions, //圆的样式
        polylineOptions: styleOptions, //线的样式
        polygonOptions: styleOptions, //多边形的样式
        rectangleOptions: styleOptions //矩形的样式
    });  
	 //添加鼠标绘制工具监听事件，用于获取绘制结果
    drawingManager.addEventListener('overlaycomplete', overlaycomplete);
    function clearAll() {
		for(var i = 0; i < overlays.length; i++){
            map.removeOverlay(overlays[i]);
        }
        overlays.length = 0   
    }	
	}

//获取坐标点

function showInfo(e){
	var point = new BMap.Point(e.point.lng,e.point.lat);	
	var removeMarker = function(e,ee,marker){
		map.removeOverlay(marker);
	}
	//创建右键菜单
	var markerMenu=new BMap.ContextMenu();
	markerMenu.addItem(new BMap.MenuItem('删除',removeMarker.bind(marker)));	
	var marker = new BMap.Marker(point);
	map.addOverlay(marker);
	marker.addContextMenu(markerMenu);	
	}




//获取中文地址
function GetAddress(point){
	var geoc = new BMap.Geocoder(); 
	geoc.getLocation(point, function(rs){
			var addComp = rs.addressComponents;  	
			address =  addComp.province + ", " + addComp.city + ", " + addComp.district + ", " + addComp.street + ", " + addComp.streetNumber; 		
		})
}

function ClassPoint(point,id)
{
	//var SelfPoint = new Object;
	//SelfPoint.
	this.IdName = id;
	//SelfPoint.
	this.marker = new BMap.Marker(point);
	//SelfPoint.
	this.GetIdName = function(){return this.IdName;};      
	//SelfPoint.
	this.AddPoint = function(){map.addOverlay(this.marker);};   
	//SelfPoint.
	this.AddListener = 
	function(How,What){this.marker.addEventListener(How,What);};     
}

function showPoint(x,y,ID){
	var point = new BMap.Point(x, y);	
	//var removeMarker = function(e,ee,marker){
		//map.removeOverlay(marker);
	//}
	//创建右键菜单
	//var markerMenu=new BMap.ContextMenu();
	//markerMenu.addItem(new BMap.MenuItem('删除',removeMarker.bind(marker)));	
	var marker = new ClassPoint(point,ID);
	marker.AddPoint();
	//var label = new BMap.Label(ID,{offset:new BMap.Size(20,-10)});
	//marker.setLabel(label);
	//marker.addContextMenu(markerMenu);	
	marker.AddListener("click",getAttr);
	function getAttr(){
		var p = marker.GetIdName();       //获取marker的位置
		//alert(p);
		//clearOverlays();
		SearchOccurByDormitory(p); 
		 }
}
//定位到中心点	
function LocateAsCenter(x,y){
	map.panTo(new BMap.Point(x,y)); 
	}
	
function removeMarker(e,ee,marker)
{
	map.removeOverlay(marker);
}
		

function OnWalk(Name1,Name2)
{
	var transit = new BMap.DrivingRoute(map, {
		renderOptions: {
			map: map,
			panel: "r-result",
			enableDragging : true //起终点可进行拖拽
		},  
	});
	transit.search(Name1,Name2);
}
