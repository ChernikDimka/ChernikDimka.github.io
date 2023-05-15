advice_url = "https://api.adviceslip.com/advice"
$("#main-header").click(function(){
	$.getJSON(advice_url,function(data){		
		advice = data["slip"]["advice"]
		set_secret_msg(advice);
	});
	
});
function set_secret_msg(msg){
	p = $("#second");
	p.html(msg);
	p.css("color","green");
}