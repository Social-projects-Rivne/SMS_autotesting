$(document).ready(function () {
//-----------------------------
//event
//-----------------------------
	$('body').on('click', '.modal-dialog', create_popup);
//-----------------------------
});
//-----------------------------
//modal dialog
//-----------------------------

function create_popup() {
 	href = $(this).attr('href');

	add_block_page();
	add_popup_box(href);

	$('.popup_modal_box').fadeIn();
	return false;
}

function add_block_page() {
	//append div for modal window into body
	var block_page = $('<div class="popup_block_page"></div>');
	$(block_page).appendTo('body');
}

function add_popup_box(href) {

    var pop_up = $('<div class="popup_modal_box"><a href="#" class="popup_modal_close">x</a><div class="popup_inner_modal_box"></div></div>');

	$(pop_up).appendTo('.popup_block_page');
	//load form into modal div
	$('.popup_inner_modal_box').load(href, function() {
		//where to send the request?
		$('.popup_inner_modal_box form').attr('action', href);
		//event form
		$('body').on('change', 'input', validate_field);

		if (href.match('update')) {
			//confirm and save form in case of updating
			$('body').on('submit', '.popup_modal_box', confirm_box);
		} else {
			//save form in case of adding
			$('body').on('submit', '.popup_modal_box', save_form);
		}
	});
	//button for close modal
	$('.popup_modal_close').click(function() {
		$(this).parent().fadeOut().remove();
		$('.popup_block_page').fadeOut().remove();
	});
}

function confirm_box() {
	//validate all fields
	var $inputs = $(this).find(':input');
	var is_correct;
	$inputs.each(function(){
		if(!validate_field(null, this)) {
			is_correct =  false;
		}
	})
	if (is_correct == false ) {
		return false;
	}

	//confirmation dialog
	var answer = confirm('Ви дійсно хочете зберегти зміни?');

	if (!answer) {
		return false;
	}
}

//-----------------------------
//ajax send request
//-----------------------------
function save_form(href) {

	//validate all fields
	var $inputs = $(this).find(':input');
	var is_correct;
	$inputs.each(function(){
		if(!validate_field(null, this)){
			is_correct =  false;
		}
	})
	if (is_correct == false ) {
		return false;
	}
	href = $('.popup_inner_modal_box form').attr('action');
	if(!href.math('/$'))
		href = href + '/';
	//send request
	$.ajax({
	    url: href,
	    type: $('.popup_inner_modal_box form').attr('method'),
	    data: JSON.stringify($('.popup_inner_modal_box form').serialize()),
	    success: function(response, status, request) {
	    	//...
	    }
	});
};

//-----------------------------