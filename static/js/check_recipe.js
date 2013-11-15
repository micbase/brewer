var _user_profile_url = 'http://www.wealink.com/user/profile/';


function copy_obj1_text_to_obj2_text(obj1,obj2id){
    var _val = $(obj1).text();
    $("#"+obj2id).text(_val);
    return false;
}
function chooseLi(val,id){
    $('#'+id).val(val);
    $('#'+id+'Span').text(val);
    $('#'+id+'Ul li a').removeClass();
    $('.optionList').hide();
    return false;
}

function user_ingredient_edit(uid,id,categoryname,amount,unit,ingredientname){
    if(id>0){
        
        $("#li_ingredient_"+id).after($("#edit_ingredient_inputbox"));
        $("#li_ingredient_"+id).hide();
    }

    $("#id_ingredient_input_id").val(id);
    $("#categoryname").val(categoryname);
    $("#amount").val(amount);
    $("#unit").val(unit);
    $("#ingredientname").val(ingredientname);

    $("#edit_ingredient_inputbox").show();
    $('#id_save_ingredient').attr('disabled', false);

    $("#id_add_ingredient_btn").hide();
    $("#categoryname").focus();
    return false;
}
function cancel_ingredient_edit(id){
    $("#edit_ingredient_inputbox").hide();
    // $("#ingredient_2).hide();    
    $("#id_add_ingredient_btn").show();
    $('#id_save_ingredient').attr('disabled', false);

    var id = $.trim($("#id_ingredient_input_id").val());
    if(id && id!='' && id>0){
        $("#ingredient_"+id).show();

        // $("#id_add_ingredient_btn").after($("#edit_ingredient_inputbox"));
        $("#id_add_ingredient_btn").after($("#ingredient_2"));        
    }

    $("#id_ingredient_input_id").val(0);
    $("#ingredientname").val('');

    return false;
}

// function save_ingredient_add(uid){

//     $("#id_add_ingredient_btn").show();
//     $('#id_save_ingredient').hide();


//     var id = $.trim($("#id_ingredient_input_id").val());
//     if(id && id!='' && id>0){
//         $("#li_ingredient_"+id).show();
        
//         $("#id_add_ingredient_btn").after($("#edit_ingredient_inputbox"));
//     }

//     $("#id_ingredient_input_id").val(0);
//     $("#ingredientname").val('');

//     return false;
// }

// function save_ingredient_add(uid){
//     if(!(uid && uid>0)){
//         return false;
//     }

//     $('#id_save_ingredient').attr('disabled', true);

//     var new_ingredientname = $.trim($("#ingredientname").val());
//     if(!new_ingredientname || new_ingredientname.length<1){
//         ye_msg.open('荣誉证书名称不能为空。',3,2);
//         $('#id_save_ingredient').attr('disabled', false);
//         return false;
//     }

//     var _ingredient_id = $.trim($("#id_ingredient_input_id").val());
//     _ingredient_id = (!_ingredient_id) ? 0 : _ingredient_id;
//     var _url = _user_profile_url + 'save_ingredient_ajax/';
//     var _data = {
//         'uid':uid,
//         'id':_ingredient_id,
//         'ingredientname':new_ingredientname
//     };

//     var keywords = new_ingredientname;
//     try{
//         $.ajax({
//            type: "POST",
//            async: false,
//            url: _bd_root_url+'ajax/blockwords.php',
//            data: 'keywords='+keywords,
//            dataType: "json",
//            success: function(data){
//                 if(data.flag=='no'){
//                     jQuery.jMessageBox.show({
//                         title : '保存荣誉证书',
//                         message : '你的荣誉证书含有敏感词“'+data.msg+'”，我们将尽快审核，审核不通过会删除誉证书，确定保存吗？',
//                         yesButton : {
//                             click : function(){
//                                 jQuery.jMessageBox.hide();
//                                 $.post(_url, _data, function(data){
//                                     if(data.code==0){
//                                         //还原新增按钮与修改框位置
//                                         cancel_ingredient_edit(uid);
//                                         //显示新的培训经历
//                                         if(_ingredient_id>0){
//                                             $("#li_ingredient_"+_ingredient_id).replaceWith(data.html);
//                                         }else{
//                                             $("#id_add_ingredient_btn").before(data.html);
//                                         }
//                                         ye_msg.open(data.msg,3,1);
//                                     }else{
//                                         $('#id_save_ingredient').attr('disabled', false);
//                                         ye_msg.open(data.msg,3,3);
//                                     }
//                                 },'json');  
//                             }
//                         },
//                         cancelButton : {
//                             click : function(){
//                                 jQuery.jMessageBox.hide();
//                                 $('#id_save_ingredient').attr('disabled', false);
//                                 return false;
//                             }
//                         }
//                     });
//                     return false;
//                 }else{
//                     $.post(_url, _data, function(data){
//                         if(data.code==0){
//                             //还原新增按钮与修改框位置
//                             cancel_ingredient_edit(uid);
//                             //显示新的培训经历
//                             if(_ingredient_id>0){
//                                 $("#li_ingredient_"+_ingredient_id).replaceWith(data.html);
//                             }else{
//                                 $("#id_add_ingredient_btn").before(data.html);
//                             }
//                             ye_msg.open(data.msg,3,1);
//                         }else{
//                             $('#id_save_ingredient').attr('disabled', false);
//                             ye_msg.open(data.msg,3,3);
//                         }
//                     },'json');  
//                 }
//            }
//         }); 
//     }catch(err){
//         $('#id_save_ingredient').attr('disabled', false);
//     }

//     return false;
// }


function user_ingredient_del(id){
    $("#ingredient_"+id).remove();
    // if(id && id>0){
    //     var _url = _user_recipe_url + 'del_ingredient_ajax/';
    //     var _data = {'id':id};
    //     $.post(_url, _data, function(data){
    //         if(data.code==0){
    //             $("#li_ingredient_"+id).remove();
    //             ye_msg.open(data.msg,1,1);
    //         }else{
    //             ye_msg.open(data.msg,3,3);
    //         }
    //     },'json');
    // }
    return false;
}

function user_it_procedure_edit(uid,id,it_procedure_status,ids,idnames){
    if(id>0){
        
        $("#li_it_procedure_"+id).after($("#edit_it_procedure_inputbox"));
        $("#li_it_procedure_"+id).hide();
    }

    $("#edit_it_procedure_inputbox").show();
    $('#id_save_it_procedure').attr('disabled', false);
    $("#id_add_it_procedure_btn").hide();

    return false;
}

function cancel_it_procedure_edit(uid){
    $("#edit_it_procedure_inputbox").hide();
    $('#id_save_it_procedure').attr('disabled', false);
    $("#id_add_it_procedure_btn").show();

    var id = $.trim($("#it_id").val());
    if(id && id!='' && id>0){
        $("#li_it_procedure_"+id).show();
        
        $("#id_add_it_procedure_btn").after($("#edit_it_procedure_inputbox"));
    }

    $("#it_id").val(0);
    $('#id_itprocedure').val('');
    $('#id_itprocedure_name').val('');

    return false;
}

function save_it_procedure_add(uid){
    if(!(uid && uid>0)){
        return false;
    }   

    return false;
}


