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

    museTation.set({
        "leftSine.freq": frequency,
        "rightSine.freq": frequency+delta
    });
});