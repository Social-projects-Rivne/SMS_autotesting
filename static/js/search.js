	$(document).ready(function () {
		$('body').on('click', '#search .btn', search);
		
	});

	function search(){
		if(document.location.pathname.indexOf('schools_list') >= 0){
			var current_url = 'school_search';

			jQuery('#list').load('/mainteacher/schools_list #list > *', function(){
				ajax_search(current_url);
			});
		}
		if(document.location.pathname.indexOf('teachers_list') >= 0){
			var current_url = 'teacher_search';

			jQuery('#list').load('/mainteacher/teachers_list #list > *', function(){
				ajax_search(current_url);
			});
		}
		
	}
	function ajax_search(current_url){
		var text = $('#search :input[name=search_text]').val();

		$.ajax({
			type:'GET',
			url: current_url,
			data: { 'search_text': text },
			datatype: 'application/json',
			success: function(sersverResponse_data, textStatus_ignored, jqXHR_ignored){
				var idx = new Array;
				jQuery.each(sersverResponse_data, function(i, val) {
				  console.log(i + ' ' + val.id.toString());
				  idx.push(val.id.toString());
				});
				
				$row = $('tbody tr');
				$row.each(function(){
					if(idx.indexOf($(this).attr('id')) < 0){
						$(this).remove();
					}
				});
				
			},
			errors: function(msg){
				alert(msg);
			},
		});
	}