let location_array

 $(document).ready(function(){
 	const location_i = document.querySelector('.location').value

 	location_array = location_i.split(",")

 	$('.report_image').off('click').on('click',function(){
 		var image_url = $(this).attr("src")

 		$('.modal_image').attr("src",image_url)

 		console.log('image source is ')
 		console.log(image_url)
 	})


 	$('.mg-zoom').off('click').on('click',function(){
 		console.log("image url ")
 		var image_url = $(this).parent().siblings('.thumb-image').children('img').attr("src")
 		
 		console.log("image url is "+image_url)

 		$('.modal_image').attr("src",image_url)

 		console.log('image source is ')
 		console.log(image_url)
 	})

 });

 let map;

	function initMap() {
		console.log("Location is "+location_array[0]+" and "+location_array[1])

		const myLatLng = { lat: parseInt(location_array[0]), lng: parseInt(location_array[1]) };

		var mapOptions = {
		  zoom: 13,
		  center: myLatLng
		}

		map = new google.maps.Map(document.getElementById("map"), mapOptions);


	  new google.maps.Marker({
    	position: myLatLng,
    	map,
    	title: "Report taken here",
  	});

	  // marker.setMap(map);

	  google.maps.event.addDomListener(window, 'load', initMap);
	}

