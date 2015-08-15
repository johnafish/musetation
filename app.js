(function () {
    fluid.registerNamespace("museTation");
    var enviro = flock.init();

    museTation.play = function () {
        var mySynth = flock.synth({
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
                    freq: 444,
                    mul: 0.25
                }
            ]
        });

        enviro.start();
    };
}());