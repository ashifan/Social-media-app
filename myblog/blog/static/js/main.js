
$(document).ready(function(){
	$('.likes').click(function(event){
		event.preventDefault();
		var element=$(this);
		$.ajax({
			url : '/blog/like_category/',
			type : 'GET',
			data : { like_id: element.attr("data-like-id")},
			success : function(response){
				element.html(' ' + response)
			}
		});
	});


	$('.dislikes').click(function(event){
		event.preventDefault();
		var element=$(this);
		$.ajax({
			url : '/blog/unlike_category/',
			type : 'GET',
			data : { dislike_id: element.attr("data-dislike-id")},
			success : function(response){
				element.html(' ' + response)
			}
		});
	});

});



