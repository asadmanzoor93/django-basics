$(function() {
    $( "#id_birth_date" ).datepicker({
      changeMonth: true,
      changeYear: true,
      yearRange: "1970:2070"
    });
});

function validate_form() {
    var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/,
    username = $('#id_username').val(),
    email = $('#id_email').val(),
    birth_date = $('#id_birth_date').val();

    $('.error_text').text(' *');

    if(username == ''){
         $('#username_error').text(' * Username is required.');
    }

    if(email == ''){
        $('#email_error').text(' * Email address is required.');
    }else if (reg.test(email) == false){
        $('#email_error').text('Invalid email address.');
    }

    if($('#id_birth_date').val() == ''){
        $('#birth_date_error').text(' * Birth date is required.');
    }

    if(error_html == ''){
        alert('Form validation is successful.');
    }
}
