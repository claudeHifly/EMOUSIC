var midiUpdate = function (time) {
    console.log(time);
}
var midiStop = function () {
    console.log("Stop");
}

function startPlaying() {
    $("#player").midiPlayer.play(song);
    $("#midiPlayer_play").css("display", "none");
    $("#midiPlayer_pause").css("display", "inline-block");
}

$(document).ready(function () {
    $("#player").midiPlayer({
        onUpdate: midiUpdate,
        onStop: midiStop
    });

    $("#midiPlayer_play").height(parseInt($("#midiPlayer_div").height() * 0.8));
    $("#midiPlayer_play").width($("#midiPlayer_play").height());
    $("#midiPlayer_pause").height(parseInt($("#midiPlayer_div").height() * 0.8));
    $("#midiPlayer_pause").width($("#midiPlayer_pause").height());
    $("#midiPlayer_stop").height(parseInt($("#midiPlayer_div").height() * 0.8));
    $("#midiPlayer_stop").width($("#midiPlayer_stop").height());
});

$(window).resize(function () {
    $("#midiPlayer_bar").width(parseInt($("#midiPlayer_div").width()) - 225);
});
