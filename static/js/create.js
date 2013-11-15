
jQuery.fn.exists = function(){return this.length>0;}

$(function() {
    n = 1;
    $("#id_add_ingredient_btn").click(function(){

        $("#edit_ingredient_inputbox").append('<div class="border-bottom-2 cf" id="ingredient_'+n+'"><ul class="cf"><li ><span>category</span><input name="categoryname" id="categoryname_'+n+'" type="text" maxLength="20" value=""/></li><li ><span>Amount&nbsp;</span><input name="amount" id="amount_'+n+'" type="text" maxLength="10" value=""/></li><li ><span>Unit &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;</span><select name="unit" id="unit_'+n+'"><option selected="selected" value="lbs">lbs</option><option value="gal">gal</option><option value="oz">oz</option></select></li ><li ><span>Name&nbsp;&nbsp;&nbsp;</span><input name="ingredientname" id="ingredientname_'+n+'" type="text" maxLength="30" value=""/></li></ul></div>');
        n = n+1;
    });


    i = 1;
    $("#id_add_it_procedure_btn").click(function(){

        $("#edit_it_procedure_inputbox").append('<div class="border-bottom-2 cf" id="procedure_'+i+'"><ul class="cf"><li ><span>Title</span><input name="titlename" id="titlename_'+i+'" type="text" maxLength="20" value=""/></li><li ><span>Tag&nbsp;</span><input name="tag" id="tag_'+i+'" type="text" maxLength="10" value=""/></li><li ><span>content&nbsp;&nbsp;&nbsp;</span><input name="content" id="content_'+i+'" type="text" maxLength="50"></li></ul></div>');
        i = i+1;
    });

    $("#create_btn").click(function() {
        var id = 0;
        var all_category = '';
        var all_amount = '';
        var all_unit = '';
        var all_ingredientname = '';

        while (true) {
            var category_id = '#categoryname_' + id;
            var amount_id = '#amount_' + id;
            var unit_id = '#unit_' + id;
            var ingredientname_id = '#ingredientname_' + id;

            if ($(category_id).exists() && $(amount_id).exists() &&
                $(unit_id).exists() && $(ingredientname_id).exists()) {

                all_category += $(category_id).val() + ',';
                all_amount += $(amount_id).val() + ',';
                all_unit += $(unit_id).val() + ',';
                all_ingredientname += $(ingredientname_id).val() + ',';

                id++;
            }
            else
                break;
        }

        all_category = all_category.slice(0, -1);
        all_amount = all_amount.slice(0, -1);
        all_unit = all_unit.slice(0, -1);
        all_ingredientname = all_ingredientname.slice(0, -1);

        id = 0;
        var all_title = '';
        var all_tag = '';
        var all_content = '';

        while (true) {
            var title_id = '#titlename_' + id;
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
            recipe_name: $('#recipename').val(),
            source_name: all_ingredientname,
            source_variety: all_category,
            amount: all_amount,
            unit: all_unit,
            procedure_title: all_title,
            precedure_tag: all_tag,
            precedure_content: all_content
        }, function(data) {
            alert(data);
        });

    });

});  
