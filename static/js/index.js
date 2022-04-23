$('#cover-spin').show()
$(document).ready(function(){$('#cover-spin').hide();})

var modename = function(name){

	$('#cover-spin').show();
	$("#modename").html(name.textContent);
	$("#modename").fadeIn("slow");

	if (name.textContent =="Paricipants"){
		$("#maincontainer").load("participants")
	}
	else if (name.textContent =="Home"){
		$("#maincontainer").load("home")
	}
	else if (name.textContent =="Manage Patient"){
		$("#maincontainer").load("patientsmgr")
	}
	else{
		$("#maincontainer").html("<h5 class='text-center'>No Data Found</h5>")
	}
	$('#cover-spin').hide();
}
$("#modename").html("");
const uri = "http://localhost:5678/"
