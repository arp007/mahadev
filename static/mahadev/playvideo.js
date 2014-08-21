(function(){
        var myVideo = _V_("example_video_1");

        var playVidoBySrc = function(src){
            var video = document.getElementsByTagName('video')[0];
            video.src = src;
            myVideo.load();
            myVideo.play();
        };
        var get_series = function(seqIndex){
            var ajax = {
        	url:location.href + seqIndex,
        	method:'GET',
        	success: function(data){
                        playVidoBySrc(data.link);
        	},
        	statusCode:{
        		404 : function(){
        			console.log("page not found");
        		}
        	}

            };

            $.ajax(ajax);

        };
        var vid_seq = 1;

        get_series(vid_seq);

        $(".seqNum").click(function(){
            idVal = $(this).attr('id');
            vid_seq = idVal;
            get_series(vid_seq);
        });

        myVideo.on("ended", function(){
            vid_seq = vid_seq + 1;
        	get_series(vid_seq);
		
        }); 

})();

