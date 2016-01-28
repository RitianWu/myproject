// 百度地图API功能
var map = new BMap.Map("allmap");
var point = new BMap.Point(113.663221, 34.7568711);
map.centerAndZoom(point, 10);
map.enableScrollWheelZoom();
// 编写自定义函数,创建标注
function addMarker(point, label) {
    var marker = new BMap.Marker(point);
    map.addOverlay(marker);
    if (label) {
        marker.setLabel(label);
        //marker.setAnimation(BMAP_ANIMATION_BOUNCE); //跳动的动画
    }
}

var points = JSON.parse($("#points").val());
console.log(points.length)
// 循环向地图添加标注
for (var i = 0; i < points.length; i++) {
    var longitude = parseFloat(points[i].split(',')[0])
    var latitude = parseFloat(points[i].split(',')[1])
    var point = new BMap.Point(longitude, latitude);
    addMarker(point);
}
// var point = new BMap.Point(114.141787333333, 22.358083);
// addMarker(point);
// var point = new BMap.Point(114.1954895, 22.283283)
// addMarker(point);

var top_left_control = new BMap.ScaleControl({anchor: BMAP_ANCHOR_TOP_LEFT});// 左上角，添加比例尺
var top_left_navigation = new BMap.NavigationControl();  //左上角，添加默认缩放平移控件
var top_right_navigation = new BMap.NavigationControl({anchor: BMAP_ANCHOR_TOP_RIGHT, type: BMAP_NAVIGATION_CONTROL_SMALL});
map.addControl(top_left_control);
map.addControl(top_left_navigation);
map.addControl(top_right_navigation);
