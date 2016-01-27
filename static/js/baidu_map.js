// 百度地图API功能
var map = new BMap.Map("allmap");
var point = new BMap.Point(113.997584, 22.416254);
map.centerAndZoom(point, 15);
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
// 随机向地图添加25个标注
var point = new BMap.Point(114.201508333333, 22.3061733333333);
// var label = new BMap.Label("A", {
//     offset: new BMap.Size(20, -10)
// });
// addMarker(point, label);
addMarker(point);
var point = new BMap.Point(114.141787333333, 22.358083);
addMarker(point);
var point = new BMap.Point(114.1954895, 22.283283)
addMarker(point);

var top_left_control = new BMap.ScaleControl({anchor: BMAP_ANCHOR_TOP_LEFT});// 左上角，添加比例尺
var top_left_navigation = new BMap.NavigationControl();  //左上角，添加默认缩放平移控件
var top_right_navigation = new BMap.NavigationControl({anchor: BMAP_ANCHOR_TOP_RIGHT, type: BMAP_NAVIGATION_CONTROL_SMALL});
map.addControl(top_left_control);
map.addControl(top_left_navigation);
map.addControl(top_right_navigation);
