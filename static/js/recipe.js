jQuery.fn.exists = function(){return this.length>0;}

function save_ingredient_note(id) {
    var new_note = $("#ingredient_note_input_" + id).val();

    var tag_id = '#ingredient_tag_' + id;
    var note_id = "#ingredient_note_" + id;
    var form_id = "#ingredient_form_" + id;
    $.post("/ingredient_note/" + id, { note: new_note }, function(data) {
        if (! $(note_id).exists()) {
            new_note_tag = '<div style="display: none" id="ingredient_note_' + id +
                '" class="ingredient_note alert alert-warning">' + new_note + '</div>'
            $(tag_id).after(new_note_tag);
        }
        else {
            $(note_id).html(new_note);
        }

        $(note_id).fadeIn();
        $(form_id).hide();
    });
}

function save_procedure_note(id) {
    var new_note = $("#procedure_note_input_" + id).val();

    var tag_id = '#procedure_tag_' + id;
    var note_id = "#procedure_note_" + id;
    var form_id = "#procedure_form_" + id;
    $.post("/procedure_note/" + id, { note: new_note }, function(data) {
        if (! $(note_id).exists()) {
            new_note_tag = '<div style="display: none" id="procedure_note_' + id +
                '" class="procedure_note alert alert-warning">' + new_note + '</div>'
            $(tag_id).after(new_note_tag);
        }
        else {
            $(note_id).html(new_note);
        }

        $(note_id).fadeIn();
        $(form_id).hide();
    });
}

function save_recipe_note(id) {
    var new_note = $("#recipe_note_input_" + id).val();

    var tag_id = '#recipe_tag_' + id;
    var note_id = "#recipe_note_" + id;
    var form_id = "#recipe_form_" + id;
    $.post("/recipe_note/" + id, { note: new_note }, function(data) {
        if (! $(note_id).exists()) {
            new_note_tag = '<div style="display: none" id="recipe_note_' + id +
                '" class="recipe_note alert alert-warning">' + new_note + '</div>'
            $(tag_id).after(new_note_tag);
        }
        else {
            $(note_id).html(new_note);
        }

        $(note_id).fadeIn();
        $(form_id).hide();
    });
}
$(".ingredient_form").hide();
$(".procedure_form").hide();
$(".recipe_form").hide();

$(document).ready(function(){
    $(document).on('click', '.ingredient_note', function() {
        var id = parseInt($(this).attr('id').substring(16));
        var note_id = '#' + $(this).attr('id');
        var form_id = '#' + $(this).attr('id').replace("note", "form");
        var input_id = '#' + $(this).attr('id').replace("note", "note_input");

        $.get("/ingredient_note/" + id, function(data) {
            $(note_id).hide();
            $(input_id).val(data.note);

            $(form_id).fadeIn();
        });
    });

    $(document).on('click', '.procedure_note', function() {
        var id = parseInt($(this).attr('id').substring(15));
        var note_id = '#' + $(this).attr('id');
        var form_id = '#' + $(this).attr('id').replace("note", "form");
        var input_id = '#' + $(this).attr('id').replace("note", "note_input");

        $.get("/procedure_note/" + id, function(data) {
            $(note_id).hide();
            $(input_id).val(data.note);

            $(form_id).fadeIn();
        });
    });

    $(document).on('click', '.recipe_note', function() {
        var id = parseInt($(this).attr('id').substring(12));
        var note_id = '#' + $(this).attr('id');
        var form_id = '#' + $(this).attr('id').replace("note", "form");
        var input_id = '#' + $(this).attr('id').replace("note", "note_input");

        $.get("/recipe_note/" + id, function(data) {
            $(note_id).hide();
            $(input_id).val(data.note);

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

    $(".recipe").click(function(){
        var note_id = '#' + $(this).attr('id').replace("tag", "note");

        $(this).hide();
        if (! $(note_id).exists()) {
            var form_id = '#' + $(this).attr('id').replace("tag", "form");
            var input_id = '#' + $(this).attr('id').replace("tag", "note_input");

            $(input_id).val("");
            $(form_id).fadeIn();
        }
    });
}); 
