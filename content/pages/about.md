title: About

I'm Jordi Burgos, I'm from Paiporta, near Valencia in Spain.

<div id="map-canvas" style="height: 300px; width:100%;">
</div>

I'm a developer, curious about coding and technology.

I work with Java and Oracle. In the spare time I like to play with Python, Django and new try things.


<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&sensor=false"></script>

<script>
var map;
function initialize() {
  var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(39.431035,-0.414678),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  
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
