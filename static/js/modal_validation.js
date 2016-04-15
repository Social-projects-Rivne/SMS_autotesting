//-----------------------------
//validation
//-----------------------------
function validate_field(event, field){

	if (typeof(field)==='undefined') field = this;
	//regexp
    var email = /^[a-z0-9]+([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/;
    var login = /^[A-Za-z0-9_]+$/;
    var school_name = /^(НВК|НВК-ліцей|ЗОШ|Школа|Гімназія) [№\'\"\-]{1}[А-Яа-яҐґЄєІіЇї0-9.,’\-\s]+[\'\"]?$/;
    var school_address = /^вул. [А-Яа-яҐґЄєІіЇї’\-\s]+[\'\"]{0,2}, \d+[а]?$/;
    var name  = /^[А-ЯҐЄІЇ]{1}[а-яґєії’\']+ [А-ЯҐЄІЇ]{1}[а-яґєії’\']+ [А-ЯҐЄІЇ]{1}[а-яґєії’\']+$/;
    var group_name  = /^[0-9]{1,2}[А-ЯҐЄІЇ]{1,2}$/;

    //for form on school page
    if($('.popup_inner_modal_box form').attr('action').indexOf('/school_') >= 0) {
		switch($(field).attr('name')){
			case 'name':
				if(!school_name.test($(field).val())){
					$(field).next().text('Некоректно введено назву.');
					return false;
				}
				else $(field).next().text('');
				break;
			case 'address':
				if(!school_address.test($(field).val())){
					$(field).next().text('Некоректно введено адресу.');
					return false;
				}
				else $(field).next().text('');
				break;
		}
    }

    //for form on teacher page
    if($('.popup_inner_modal_box form').attr('action').indexOf('/teacher_') >= 0) {
		switch($(field).attr('name')){
			case 'name':
				if(!name.test($(field).val())){
					$(field).next().text('Некоректно введено ім\'я.');
					return false;
				}
				else $(field).next().text('');
				break;
			case 'email':
				if(!email.test($(field).val())){
					$(field).next().text('Некоректно введено email.');
					return false;
				}
				else $(field).next().text('');
				break;
			case 'login':
				if(!login.test($(field).val())){
					$(field).next().text('Некоректно введено логін.');
					return false;
				}
				else $(field).next().text('');
				break;
			case 'role':
				if(!$(field).val()){
					$(field).next().text('Виберіть права.');
					return false;
				}
				else $(field).next().text('');
				break;
		}
    }

    //form for profile changing
    if($('.popup_inner_modal_box form').attr('action').indexOf('/profile') >= 0) {
		switch($(field).attr('name')){
			case 'name':
				if(!name.test($(field).val())){
					$(field).next().text('Некоректно введено ім\'я.');
					return false;
				}
				else $(field).next().text('');
				break;
			case 'email':
				if(!email.test($(field).val())){
					$(field).next().text('Некоректно введено email.');
					return false;
				}
				else $(field).next().text('');
				break;
			case 'login':
				if(!login.test($(field).val())){
					$(field).next().text('Некоректно введено логін.');
					return false;
				}
				else $(field).next().text('');
				break;
		}
    }

    //form for groups
    if($('.popup_inner_modal_box form').attr('action').indexOf('/director/group_') >= 0) {
		switch($(field).attr('name')){
			case 'name':
				if(!group_name.test($(field).val())){
					$(field).next().text('Некоректно введено назву.');
					return false;
				}
				else $(field).next().text('');
				break;
		}
    }

    //form for groups
    if($('.popup_inner_modal_box form').attr('action').indexOf('/director/student_') >= 0) {
		switch($(field).attr('name')){
			case 'name':
				if(!name.test($(field).val())){
					$(field).next().text('Некоректно введено ім\'я.');
					return false;
				}
				else $(field).next().text('');
				break;
		}
    }

    //form for manage teacher_subject_groups
    if($('.popup_inner_modal_box form').attr('action').indexOf('director/add_teacher_subject') >= 0) {
		switch($(field).attr('name')){
			case 'manage_teachers_select':
				if(!$(field).val()){
					$(field).next().text('Це обов\'язкове поле.');
					return false;
				}
				else $(field).next().text('');
				break;
		}
    }

    return true;
}