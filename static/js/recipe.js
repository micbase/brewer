function save_ingredient_note(id) {
    var new_note = $("#ingredient_note_input_" + id).val();
    $.post("/", { note: new_note });
    $("#ingredient_note_" + id).show();
    $("#ingredient_form_" + id).hide();
}

$(document).ready(function(){
    $(".ingredient_note").click(function(){
        var note_id = '#' + $(this).attr('id');
        var form_id = '#' + $(this).attr('id').replace("note", "form");
        var input_id = '#' + $(this).attr('id').replace("note", "note_input");

        var note = "Note";
        $.get("/recipe/1", function(data) {
            $(note_id).hide();
            $(input_id).val(data);

            $(form_id).removeClass("hidden");
            $(form_id).show();
        });
    });
}); 
