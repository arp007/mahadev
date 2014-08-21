(function(){
        var series_id = $("#series_id").val();
        var ajax = {
        	url:'/1',
        	method:'GET'

        };
        $.ajax(ajax).success(function(){
        	console.log("success");
        })

})();

