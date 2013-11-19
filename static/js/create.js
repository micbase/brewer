jQuery.fn.exists = function(){return this.length>0;}

$(function() {
    ingredient_index = 1;
    procedure_index = 1;

    $("#id_add_ingredient_btn").click(function(){

        $("#ingredient_container").append('<div id="ingredient_' + ingredient_index + '">\
            <hr>\
            <div class="form-group">\
                <input class="form-control" name="category" id="category_' +
                    ingredient_index + '" type="text" placeholder="Category">\
            </div>\
            <div class="form-group">\
                <input class="form-control" name="amount" id="amount_' + ingredient_index +
                    '" type="text" placeholder="Amount">\
            </div>\
            <div class="form-group">\
                <select class="form-control" name="unit" id="unit_' + ingredient_index + '">\
                    <option selected="selected" value="lbs">lbs</option>\
                    <option value="gal">gal</option>\
                    <option value="oz">oz</option>\
                </select>\
            </div>\
            <div class="form-group">\
                <input class="form-control" name="ingredient_name" id="ingredient_name_'
                + ingredient_index + '" type="text" placeholder="Name">\
            </div>\
        </div>');

        ingredient_index++;
        $("#id_delete_ingredient_btn").show();
    });

    $("#id_delete_ingredient_btn").click(function(){
        ingredient_index--;
        if (ingredient_index > 1){
            $("#ingredient_" + n).remove();
        } else if (ingredient_index == 1){
            $("#ingredient_" + ingredient_index).remove();
            $("#id_delete_ingredient_btn").hide();
        }
    });

    $("#id_add_procedure_btn").click(function() {
        $("#procedure_container").append('<div id="procedure_' + procedure_index + '">\
            <hr>\
            <div class="form-group">\
                <input class="form-control" name="title" id="title_' +
                    procedure_index + '" type="text" placeholder="Title">\
            </div>\
            <div class="form-group">\
                <input class="form-control" name="tag" id="tag_' + procedure_index +
                    '" type="text" placeholder="Tag">\
            </div>\
            <div class="form-group">\
                <input class="form-control" name="content" id="content_' +
                    procedure_index + '" type="text" placeholder="Content">\
            </div>\
        </div>');

        procedure_index++;
        $("#id_delete_procedure_btn").show();
    });

    $("#id_delete_procedure_btn").click(function() {
        procedure_index--;
        if (procedure_index > 1) {
            $("#procedure_" + procedure_index).remove();
        } else if (procedure_index == 1) {
            $("#procedure_" + procedure_index).remove();
            $("#id_delete_procedure_btn").hide();
        }
    });

    $("#create_btn").click(function() {
        var id = 0;
        var all_category = '';
        var all_amount = '';
        var all_unit = '';
        var all_ingredient_name = '';

        while (true) {
            var category_id = '#category_' + id;
            var amount_id = '#amount_' + id;
            var unit_id = '#unit_' + id;
            var ingredient_name_id = '#ingredient_name_' + id;

            if ($(category_id).exists() && $(amount_id).exists() &&
                $(unit_id).exists() && $(ingredient_name_id).exists()) {

                all_category += $(category_id).val() + ',';
                all_amount += $(amount_id).val() + ',';
                all_unit += $(unit_id).val() + ',';
                all_ingredient_name += $(ingredient_name_id).val() + ',';

                id++;
            }
            else
                break;
        }

        all_category = all_category.slice(0, -1);
        all_amount = all_amount.slice(0, -1);
        all_unit = all_unit.slice(0, -1);
        all_ingredient_name = all_ingredient_name.slice(0, -1);

        id = 0;
        var all_title = '';
        var all_tag = '';
        var all_content = '';

        while (true) {
            var title_id = '#title_' + id;
            var tag_id = '#tag_' + id;
            var content_id = '#content_' + id;

            if ($(title_id).exists() && $(tag_id).exists() &&
                $(content_id).exists()) {

                all_title += $(title_id).val() + ',';
                all_tag += $(tag_id).val() + ',';
                all_content += $(content_id).val() + ',';

                id++;
            }
            else
                break;
        }

        all_title = all_title.slice(0, -1);
        all_tag = all_tag.slice(0, -1);
        all_content = all_content.slice(0, -1);

        $.post("/create_recipe", {
            recipe_name: $('#recipe_name').val(),
            source_name: all_ingredient_name,
            source_variety: all_category,
            amount: all_amount,
            unit: all_unit,
            procedure_title: all_title,
            procedure_tag: all_tag,
            procedure_content: all_content
        }, function(data) {
            if (data.success) {
                window.location.href = data.redirect;
            }
            else {
                alert("Input Error");
            }
        });

    });

});
