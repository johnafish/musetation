var fraction = 0;
$(document).ready(function(){
	var numerator = 0;
	var denominator = x.length;
	for (var i = 0; i < x.length; i++) {
		if(x[i]==0){
			numerator+=1;
		}
	};
	fraction = Math.round((numerator/denominator)*10000)/100
	console.log(fraction)
	$("#value").text(fraction)
	$("#share").append('<a href="https://twitter.com/share" class="twitter-share-button" id="twitter" data-url="http://github.com/johnafish/musetation" data-text="'+'I just finished meditating using museTation, and I had an overall efficiency of '+fraction+'%!" data-size="large">Tweet</a>')
});