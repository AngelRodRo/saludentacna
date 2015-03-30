/**
 * Created by angel on 29/03/15.
 */
//
//$("#search_clinic").on('click', function(){
//    //alert("Hola mundo")
//});

$(document).ready(function(){
    $("#form1").submit(function(){

    })
})

function getName2URL(){

    var name = $("#name_clinic").val();
    //alert(name);
    parent.location = "/resultado/"+name+"/";
}