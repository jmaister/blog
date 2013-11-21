title: About Me
icon:torso

Hi.

I'm [Jordi Burgos](http://jordiburgos.com). I'm from Paiporta, near Valencia in Spain.

I'm a software engineer, curious about programming and technology.

I work mainly with Java and Oracle. Also I like to play with Javascript, Python, Django, ...

<div id="map_canvas" style="height: 300px; width:100%; padding:25px;">
</div>

<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>

<script>
var map;
function initialize() {
  var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(39.431035,-0.414678),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);
  
	var paiporta = new google.maps.LatLng(39.431035,-0.414678);
	var marker = new google.maps.Marker({
		map:map,
		draggable:false,
		animation: google.maps.Animation.DROP,
		position: paiporta
	});
}
google.maps.event.addDomListener(window, 'load', initialize);
</script>
