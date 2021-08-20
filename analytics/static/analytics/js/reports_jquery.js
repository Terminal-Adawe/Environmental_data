 $(document).ready(function(){

    var returnedData = getDetails();

 })



// Get details on reports and structure them
 function getDetails(){
    console.log("Details ... ")
  jQuery.ajaxSetup({
              headers: {
                'X-CSRF-TOKEN': jQuery('meta[name="csrf-token"]').attr('content')
              }
          });

          jQuery.ajax({
            url: '/analytics/get-reports/',
            type: 'GET',
            dataType    : 'json',
                error: function(xhr, desc, err) {
            //console.log(xhr);
            //console.log("Details: " + desc + "\nError:" + err);
      }
            })
          .done(function(data) {
            
            //console.log("returned data is "+JSON.stringify(data));

            console.log("jquery reports response is ")
            console.log(data)

            structure_data_in_html(data);

            return data;
          });
    }


function structure_data_in_html(data){
    console.log("Do I even structure html? ")
    var html = "<div class='row'><div class='col-lg-12 col-12'><h3>Select a report to add to</h3></div></div>";

            $('#report_list_jquery').before(html)

            data.map((report,i)=>{
                console.log(report)
                html = "<div class='row my-2' key={i} style='padding-bottom:8px'><div class='col-lg-12 col-md-12 col-sm-12 col-12'><button class='btn addToReport_btn' type='button'>"+report.report_name+"</button></div></div>";

                $('#report_list_jquery').after(html)
            })

            $('.addToReport_btn').off("click").on("click",addToReport)
}


function addToReport(){
    let the_id = document.getElementById("report_id").value
    if(document.querySelector(".table_id")){
        the_id = document.querySelector(".table_id").value;
    } 
    const category = $("#report_cat").val()
    const report_name = $(this).html();
    const module_id = $("#report_table_type").val();
        console.log("Report name is ")
        console.log($(this).html())
        console.log(the_id)
        console.log(jQuery('meta[name="csrf-token"]').attr('content'))



    jQuery.ajaxSetup({
              headers: {
                'X-CSRFToken': jQuery('meta[name="csrf-token"]').attr('content')
              }
          });

          var formData = {"the_id" : the_id,"category" : category,"reportName" : report_name, "module_id" : module_id};

            let form_data = new FormData();

            form_data.append('the_id', the_id)
            form_data.append('category', category)
            form_data.append('reportName', report_name)
            form_data.append('module_id', module_id)
          //console.log('about to send '+formData.accountnumber+" to get code.");

          jQuery.ajax({
            url: '/analytics/api/add_to_report/',
            type: 'POST',
            data:formData,
            dataType    : 'json',
            // processData : false,
                error: function(xhr, desc, err) {
            //console.log(xhr);
            //console.log("Details: " + desc + "\nError:" + err);
      }
            })
          .done(function(data) {
            
            console.log("returned data is ");
            console.log(data);

            $('#reports').modal('toggle');
            $('#results_modal').modal('toggle');

            return data;
          });

    }
