$(document).ready(function () {

    //-----------------------------
    //event
    //-----------------------------
    $('body').on('change', '.school_dir_sel', ChangeDirector);
    $('body').on('change', '.school_select', ChangeSchool);
    $('body').on('change', '.role_select', ChangeRole);
    $('body').on('change', '.group_select', ChangeGroup);
    $('body').on('change', '.state_select', ChangeState);
    $('body').on('change', '#manage_teachers_select', CheckTeacherSubject);
    $('body').on('change', '#inputName', CheckGroupName);
    $('body').on('change', '#inputSchoolName', CheckSchoolName);
    $('body').on('change', '#inputLogin', CheckUnique);
    $('body').on('change', '#inputEmail', CheckUnique);

    //-----------------------------
    //setup CSRF token
    //-----------------------------
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
               }
           }
       }
       return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    //-----------------------------
});

//-----------------------------
//ajax post
//-----------------------------
function ChangeDirector() {
    var director = $(this).val();
    var id = $(this).closest('tr').attr('id');
    //-----------------------------
    $.ajax({
        url: window.location.pathname,
        data: {
            id: $(this).closest('tr').attr('id'),
            director: $(this).val()
        },
        type: 'POST',
        success: function(msg) {
            //...
        },
        errors: function(msg) {
            alert(msg);
        }
    })
}

function ChangeSchool() {
    var school = $(this).val();
    var id = $(this).closest('tr').attr('id');
    //-----------------------------
    $.ajax({
        url: window.location.pathname,
        data: {
            id: $(this).closest('tr').attr('id'),
            school: $(this).val()
        },
        type: 'POST',
        success: function(msg) {
            //...
            location.reload(true);
        },
        errors: function(msg) {
            alert(msg);
        }
    })
}

function ChangeRole() {
    var role = $(this).val();
    var id = $(this).closest('tr').attr('id');
    //-----------------------------
    $.ajax({
        url: window.location.pathname,
        data: {
            id: $(this).closest('tr').attr('id'),
            role: $(this).val()
        },
        type: 'POST',
        success: function(msg) {
            //...
            location.reload(true);
        },
        errors: function(msg) {
            alert(msg);
        }
    })
}

function ChangeGroup() {
    var group = $(this).val();
    var id = $(this).closest('tr').attr('id');
    //-----------------------------
    $.ajax({
        url: window.location.pathname,
        data: {
            id: $(this).closest('tr').attr('id'),
            group: $(this).val()
        },
        type: 'POST',
        success: function(msg) {
            location.reload(true);
        },
        errors: function(msg) {
            alert(msg);
        }
    })
}

function ChangeState() {
    var state = $(this).val();
    var id = $(this).closest('tr').attr('id');
    //-----------------------------
    $.ajax({
        url: window.location.pathname,
        data: {
            id: $(this).closest('tr').attr('id'),
            state: $(this).val()
        },
        type: 'POST',
        success: function(msg) {
            location.reload(true);
        },
        errors: function(msg) {
            alert(msg);
        }
    })
}

function CheckTeacherSubject() {
    $.ajax({
        url: window.href,
        type:'POST',
        'async': true,
        'dataType': 'json',
        data: {
            value : $(this).val()
        },
        statusCode: {
            400: function() {
                if ((window.href).indexOf('add_teacher_subject_group/') >= 1 ) {
                    $('#error_message').text('Викладач вже веде даний предмет в цьому класі.');
                }
                else {
                    $('#error_message').text('Даний викладач вже веде вибраний предмет.');
                }
                $('#add_button').attr("disabled", true);
            },
            200: function() {
                $('#error_message').text('');
                $('#add_button').prop("disabled", false);
            }
        }
    });
}

function CheckGroupName() {
    $.ajax({
        url: window.href,
        type: 'POST',
        'async': true,
        'dataType': 'json',
        data: {
            value : $(this).val()
        },
        statusCode: {
            400: function() {
                $('#error_message').text('Клас з такою назвою вже існує.');
                $('#add_button').attr("disabled", true);
            },
            200: function() {
                $('#error_message').text('');
                $('#add_button').prop("disabled", false);
            }
        }
    });
}


function CheckUnique(){
    var form = $(this).closest("form");
    var login = $('#inputLogin').val();

    $.ajax({
        url: form.attr('action'),
        type: 'POST',
        data: {
            field: $(this).attr('name'),
            value: $(this).val()
        },
        statusCode: {
            400: function(data){
                var field = jQuery.parseJSON(data.responseText)

                if(field.field == 'login'){
                    $('#inputLogin').next().text(field.status.toString());
                }
                if(field.field == 'email'){
                    $('#inputEmail').next().text(field.status.toString());
                }
                $('button[type=submit]', form).attr("disabled", "");
            },
            200: function(data){
                $('button[type=submit]', form).removeProp('disabled');
            }
        }
    });
    return false;
}


function CheckSchoolName() {
    $.ajax({
        url: window.href,
        type: 'POST',
        'async': true,
        'dataType': 'json',
        data: {
            value : $(this).val()
        },
        statusCode: {
            400: function() {
                $('#error_message').text('Школа з такою назвою вже існує.');
                $('#add_button').attr("disabled", true);
            },
            200: function() {
                $('#error_message').text('');
                $('#add_button').prop("disabled", false);
            }
        }
    });
}
//-----------------------------
