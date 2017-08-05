
$(document).ready(function () {

    $.validator.addMethod("alphanumeric", function(value, element) {
        return this.optional(element) || value == value.match(/^[a-zA-Z0-9]+$/);
    });


    $('#loginForm').validate({ // initialize the plugin
    
        errorClass: "my-error-class",
        validClass: "my-valid-class",
        rules: {
            email: {
                required: true,
                email: true
            },
            password1: {
                required: true,
                minlength: 5,
            },
            password2: {
                required: true,
                equalTo: '#id_password1',
            },
            terms_cond: {
                required: true,
            },
        },
        
        // Specify the validation error messages
        messages: {
            email: "Please enter a valid email address",
            password1: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long",
            },
            password2: {
                required: "Please confirm your password",
                equalTo: "Password mismatch",
            },
            terms_cond: "Must agree to terms and conditions.  ",
        }
        
        
    });
    
    //$("form").attr('novalidate', 'novalidate');
    
    $("#id_username").prop("readonly", true);
    
    //$('#id_user_form input[type=password]').remove();
    //$('#id_password_form input[type=text]').remove();
    

    var username = ""
    var email = ""
    username = $("#id_username").val();
    console.log(username);
    $.ajax({
        url: '/form/check_get_user/',
        data: {
          'username':username
          },
        dataType: 'json',
        success: function (data) {
          if (data.valid) {
            email = data.email;
            //$("#id_email").attr("placeholder", data.email).blur();
             $("#id_email").val(data.email);
            // $("#id_email").attr("placeholder", data.email).blur();
            // $("#id_contact").attr("placeholder", data.contact).blur();
            // $("#id_location").attr("placeholder", data.address).blur();
            // $("#id_birth_date").attr("placeholder", data.birth_date).blur();
            
          }
          else{
              alert("Such user does not exit");
          }
        }
      });
      
   
    
    $( ".btn-warning" ).click(function() {
      document.location.href = '/form/profile';
    });
    
    // $("#id_form").submit(function (e) {
    //     //e.preventDefault();
    //     console.log('ok');
    //     $("#id_email").val(email);
        
    //     var form = $(this).closest("form");
        
    //     console.log(form.attr("update_profile_url"));
    //     $.ajax({
    //         url: form.attr("update_profile_url"),
    //         method: 'POST',
    //         data: form.serialize(),
    //         dataType: 'json',
    //         success: function (data) {
    //             console.log(data.status);
    //             document.location.href = '/form/profile';
    //     }
    //   });

    // });
   
   
    
});