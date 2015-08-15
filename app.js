fluid.registerNamespace("museTation");
var enviro = flock.init();
enviro.start();

var museTation = flock.synth({
    synthDef: [
        {
            id: "leftSine",
            ugen: "flock.ugen.sinOsc",
            freq: 440,
            mul: 0.25
        },
        {
            id: "rightSine",
            ugen: "flock.ugen.sinOsc",
            freq:445,
            mul: 0.25
        }
    ]
 });

$("input").change(function(){
    console.log("click")
    var frequency = parseInt($("#frequency").val());
    var delta = parseInt($("#delta").val());
    var volume = parseFloat($("#volume").val());

    museTation.set({
        "leftSine.freq": frequency,
        "rightSine.freq": frequency+delta,
        "leftSine.mul": volume,
        "rightSine.mul": volume
    });
});

$(document).ready(function(){
    var file = "C:/Users/John/Desktop/musetation/file.txt";

    var reader = new FileReader();

    reader.onload = function(e) {
        var result = reader.result;
        console.log(result)
    }

    reader.readAsText(file);
});