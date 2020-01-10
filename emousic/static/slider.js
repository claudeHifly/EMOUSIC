$(function () {
    $("#measure_data").val(JSON.stringify(measure_data));
    $("#checked_approach").val($( "input:checked" ).val());

    $("#slider-range").slider({
        range: true,
        min: 1,
        max: measures,
        values: [1, measures],
        slide: function (event, ui) {
            // $("#amount").val(ui.values[0] + " - " + ui.values[1]);
            $("#amount").html(ui.values[0] + " - " + ui.values[1]);
            $("#min_measure").val(ui.values[0]);
            $("#max_measure").val(ui.values[1]);
        },
        create: function(event, ui) {
            update_function();
        },
        stop: function(event, ui) {
            update_function();
        }
    });



    // $("#amount").val($("#slider-range").slider("values", 0) + " - " + $("#slider-range").slider("values", 1));
    $("#amount").html($("#slider-range").slider("values", 0) + " - " + $("#slider-range").slider("values", 1));
    $("#min_measure").val($("#slider-range").slider("values", 0));
    $("#max_measure").val($("#slider-range").slider("values", 1));
});

var update_function = function() {
    $.ajax({
        url: '/emousic/get_moodtags/',
        data: {
          'track_id': $("#track_id").val(),
          'min': $("#slider-range").slider("values", 0),
          'max': $("#slider-range").slider("values", 1),
          'approach': $("#checked_approach").val(),
        },
        dataType: 'json',
        success: function (data) {
            $("#table_pleasantness").html(data.compact_tuple[0]);
            $("#table_attention").html(data.compact_tuple[1]);
            $("#table_sensitivity").html(data.compact_tuple[2]);
            $("#table_aptitude").html(data.compact_tuple[3]);
            $("#table_moodtag_1").html(data.compact_tuple[4]);
            $("#table_moodtag_2").html(data.compact_tuple[5]);
            $("#table_polarity").html(data.compact_tuple[6]);
        }
      });
}