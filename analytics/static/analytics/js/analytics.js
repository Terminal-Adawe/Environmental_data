let location_array

 $(document).ready(function(){
 	console.log("I appear")

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

 	// Date selector processsing

 	var dtToday = new Date();
    
    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    if(month < 10)
        month = '0' + month.toString();
    if(day < 10)
        day = '0' + day.toString();
    
    var maxDate = year + '-' + month + '-' + day;
    // alert(maxDate);
    $('#todate').attr('max', maxDate);
    $('#fromdate').attr('max', maxDate);

    $('#fromdate').change(function(){
    	console.log('date change'+$(this).val());
    	$('#todate').attr('min', $(this).val());
    });

    $('#todate').change(function(){
    	console.log('date change'+$(this).val());
    	$('#fromdate').attr('max', $(this).val());
    });

    // Fin

    // Export all selected
    $(".export-all-selected").off("click").on("click",function(){
    	const module_s = $(this).siblings("#module_s").val();
    	console.log("Module is "+module_s);
    	$("#module_name").val(module_s);
        $("#modal_report_type").val("default");
    	console.log("Module is "+$("#module_name").val());
    })

    $(".scheduler").off("click").on("click",function(){
        $('#scheduler').modal("toggle")

        // Set task type in modal
        $('#task_type').val($(this).data("type"))
        console.log("data attrib is "+$('#task_type').val())
    })

    $(".edit_user_btn").off("click").on("click",function(){
        console.log("You have clicked")
        console.log($(this).children(".username").val())

        const username = $(this).children(".username").val()
        const email = $(this).children(".email").val()
        const first_name = $(this).children(".first_name").val()
        const last_name = $(this).children(".last_name").val()

        var form_fields = document.querySelectorAll(".form-control"), i;

        for (i = 0; i < form_fields.length; ++i) {
            if(form_fields[i].name=="username"){
                form_fields[i].value = username
            }
            if(form_fields[i].name=="email"){
                form_fields[i].value = email
            }
            if(form_fields[i].name=="first_name"){
                form_fields[i].value = first_name
            }
            if(form_fields[i].name=="last_name"){
                form_fields[i].value = last_name
            }
        }


    })

    // All code should be above the code below since it picks location
    // and location has not been implemented in all the templates
    const location_i = document.querySelector('.location').value

 	location_array = location_i.split(",")
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

