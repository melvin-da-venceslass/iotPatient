
var search = function () {

    var pid = $("#patient_id").val();
    if (pid != "" && pid != null) {
        var d = { "pid": pid };
        $.ajax({
            type: 'post',
            url: uri + "getPatient",
            data: JSON.stringify(d),
            contentType: "application/json; charset=utf-8",
            traditional: true,
            success: function (data) {
                if (data.status == "success") {
                    localStorage.setItem("create", false)
                    console.log(data.pid)
                    $("#patient_idf").val(data.pid)
                    $("#patient_idf").attr("disabled", "disabled")

                    $("#patient_name").val(data.name)
                    $("#patient_name").attr("disabled", "disabled")

                    $("#patient_add").val(data.address)
                    $("#patient_add").attr("disabled", "disabled")

                    $("#patient_type").val(data.type).change()
                    $("#patient_type").attr("disabled", "disabled")

                    $("#modify_button").show();
                    $("#delete_button").show();
                    
                    $("#form_right").show()
                }
                else if (data.status == "no-user") {
                    if(localStorage.getItem("create")==='true'){
                  
                    $("#patient_name").val("")
                    $("#patient_add").val("")
                    $("#patient_type").val("").change()
                    $("#form_right").show()
                    alert("No User found!")}
                    localStorage.setItem("create", true)
                    
                    
                    
                }
                else {
                    $("#form_right").hide()
                }
            },

        });
    }
    else {
        alert("Patient id cannot be empty")
    }

}

var modify = function () {
    localStorage.setItem("modify", true)
    $("#patient_name").removeAttr("disabled")
    $("#patient_add").removeAttr("disabled")
    $("#patient_type").removeAttr("disabled")

}

var userpush = function(data){
    var dn = data
    $.ajax({
        type: 'post',
        url: uri + "savePatient",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        traditional: true,
        success: function (data) {
            if (data.status == "success") {
                alert(dn.operation+" Success!")
                $("#form_right").hide()
            }
            else {
                $("#form_right").hide()
            }
        }

    })
}


var savechanges = function () {
    if (localStorage.getItem("modify") == 'true') {
        var data = {
            "pid": $("#patient_idf").val(),
            "name": $("#patient_name").val(),
            "address": $("#patient_add").val(),
            "type": $("#patient_type").find(":selected").text(),
            "operation": "modify"
        }
        userpush(data)
    }
    else if (localStorage.getItem("create") == 'true') {
            var data = {
                "pid": $("#patient_idf").val(),
                "name": $("#patient_name").val(),
                "address": $("#patient_add").val(),
                "type": $("#patient_type").find(":selected").text(),
                "operation": "create"
        }
        userpush(data)

    }
    else {
        alert("Access denied")
    }

    
    localStorage.setItem("modify", 'false')
}


var create = function(){
    search()
    if (localStorage.getItem("create")==='true'){
        $("#patient_name").removeAttr("disabled")
        $("#patient_add").removeAttr("disabled")
        $("#patient_type").removeAttr("disabled")
        $("#patient_idf").attr("disabled", "disabled")
        $("#patient_idf").val($("#patient_id").val())
        $("#patient_name").val("")
        $("#patient_add").val("")
        $("#patient_type").val("").change()
        $("#form_right").show()
    }
    
    
}

var deletes = function(){
    search()
    if (localStorage.getItem("create")==='false'){
       data = { "pid": $("#patient_idf").val(),
        "name": $("#patient_name").val(),
        "address": $("#patient_add").val(),
        "type": $("#patient_type").find(":selected").text(),
        "operation": "delete"}
        userpush(data)
}

        


}


$("#modify_button").hide();
$("#delete_button").hide();

$("#search_button").on('click', search);
$("#modify_button").on('click', modify);
$("#create_button").on('click', create);
$("#delete_button").on('click', deletes);
$("#save_changes").on('click', savechanges);

localStorage.setItem("modify", 'false')
localStorage.setItem("create", 'false')
$("#form_right").hide()