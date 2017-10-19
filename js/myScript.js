(document).ready(function(){
 
	if( navigator.geolocation )
	 navigator.geolocation.getCurrentPosition(success);
	else
	 $("p").html("HTML5 Not Supported");
 
});
 
function success(position)
{
	$("p").html("Latitude: "+position.coords.latitude+
	            "<br />Longitude: "+position.coords.longitude+
				"<br />Accuracy: "+position.coords.accuracy);
}

