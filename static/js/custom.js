// return values of sliders
$(function(){
	window.prettyPrint && prettyPrint();

    $('#select_range').slider({
      formater: function(value) {
        return value + '%';
      }
    });

    $('#select_burn').slider({
      formater: function(value) {
        return '≤ ' + number_with_commas(value) + ' totes per hour';
      }
    });   
});

// makes numbers comma-separated
function number_with_commas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

// matches height of bootstrap columns
$(function(){
  $('.match').matchHeight();
});

// fixes width issue introduced by datatable's scrolling option
$(function() {
  $('.table').css('width', '100%');
});

// adds padding to datatable's info option
$(function() {
    $('.dataTables_info').css({'padding': '16px 0px 6px 8px'});
});

// keeps dropdown selection after submit via localstorage
$(function() {
    var curr_fc = localStorage.getItem("curr_fc");
    if(curr_fc != null) {
        $("select[name=fc]").val(curr_fc);
    }
    $("select[name=fc]").on("change", function() {
        localStorage.setItem("curr_fc", $(this).val());
    });
});

//keep radio selection after submit
