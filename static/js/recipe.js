jQuery.fn.exists = function(){return this.length>0;}

function save_ingredient_note(id) {
    var new_note = $("#ingredient_note_input_" + id).val();

    var tag_id = '#ingredient_tag_' + id;
    var note_id = "#ingredient_note_" + id;
    var form_id = "#ingredient_form_" + id;
    $.post("/", { note: new_note });

    // TODO: put in the post success function

    if (! $(note_id).exists()) {
        new_note_tag = '<div style="display: none" id="ingredient_note_' + id +
            '" class="ingredient_note alert alert-warning">' + new_note + '</div>'
        $(tag_id).after(new_note_tag);
    }

    $(note_id).fadeIn();
    $(form_id).hide();

    // *****
}

function save_procedure_note(id) {
    var new_note = $("#procedure_note_input_" + id).val();

    var tag_id = '#procedure_tag_' + id;
    var note_id = "#procedure_note_" + id;
    var form_id = "#procedure_form_" + id;
    $.post("/", { note: new_note });

    // TODO: put in the post success function

    if (! $(note_id).exists()) {
        new_note_tag = '<div style="display: none" id="procedure_note_' + id +
            '" class="procedure_note alert alert-warning">' + new_note + '</div>'
        $(tag_id).after(new_note_tag);
    }

    $(note_id).fadeIn();
    $(form_id).hide();

    // *****
}

$(".ingredient_form").hide();
$(".procedure_form").hide();

$(document).ready(function(){
    $(document).on('click', '.ingredient_note', function() {
        var note_id = '#' + $(this).attr('id');
        var form_id = '#' + $(this).attr('id').replace("note", "form");
        var input_id = '#' + $(this).attr('id').replace("note", "note_input");

        var note = "Note";
        $.get("/recipe/1", function(data) {
            $(note_id).hide();
            $(input_id).val(data);

            $(form_id).fadeIn();
        });
    });

    $(".ingredient").click(function(){
        var note_id = '#' + $(this).attr('id').replace("tag", "note");

        if (! $(note_id).exists()) {
            var form_id = '#' + $(this).attr('id').replace("tag", "form");
            var input_id = '#' + $(this).attr('id').replace("tag", "note_input");

            $(input_id).val("");
            $(form_id).fadeIn();
        }
    });

    $(".procedure").click(function(){
        var note_id = '#' + $(this).attr('id').replace("tag", "note");

        if (! $(note_id).exists()) {
            var form_id = '#' + $(this).attr('id').replace("tag", "form");
            var input_id = '#' + $(this).attr('id').replace("tag", "note_input");

            $(input_id).val("");
            $(form_id).fadeIn();
        }
    });
}); 
