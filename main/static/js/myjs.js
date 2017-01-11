$(function() {
  $(function(){
      $("#majorjs").change(function(){
        $.getJSON("/items/",{id: $(this).val(), view: 'json'}, function(j) {
          var options = '<option value="">--------&nbsp;</option>';
          for (var i = 0; i < j.length; i++) {
            options += '<option value="' + j[i].optionValue + '">' + j[i].optionDisplay + '</option>';
          }
          $("#coursejs").html(options);
          $("#coursejs option:first").attr('selected', 'selected');
        })
        $("#coursejs").attr('selected', 'selected');
      })
    })
});
