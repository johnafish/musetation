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
$("#frequency").change(function(){
    $("#frequencyval").text($(this).val())
})
$("#delta").change(function(){
    $("#deltaval").text($(this).val())
})
$("#volume").change(function(){
    $("#volumeval").text(parseFloat($(this).val())*100)
})
$("#start").click(function(){
    $("form").slideUp();
    $(this).slideUp();
    $("#stop").slideDown();
    $(".timer").slideDown();
    $(".timer").TimeCircles().start();
})
$(".timer").TimeCircles({start: false,  time: { Days: { show: false } }});
// $(document).ready(function(){
//     console.log(x)
//     console.log(museData)
// });