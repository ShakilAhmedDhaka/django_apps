$(document).ready(function () {

    $.validator.addMethod("alphanumeric", function(value, element) {
        return this.optional(element) || value == value.match(/^[a-zA-Z0-9]+$/);
    });


    $('#loginForm').validate({ // initialize the plugin
    
        errorClass: "my-error-class",
        validClass: "my-valid-class",
        rules: {
            user: {
                required: true,
                minlength: 5,
                alphanumeric : true
            },
            email: {
                required: true,
                email: true
            },
            passwd: {
                required: true,
                minlength: 5,
            },
            conf_passwd: {
                required: true,
                equalTo: '#id_passwd',
            },
            terms_cond: {
                required: true,
            },
        },
        
        // Specify the validation error messages
        messages: {
            user: {
                required: "Please enter user name",
                alphanumeric: "username must be alphanumeric"
            },
            email: "Please enter a valid email address",
            passwd: {
                required: "Please provide a password",
                minlength: "Your password must be at least 5 characters long",
            },
            conf_passwd: {
                required: "Please confirm your password",
                equalTo: "Password mismatch",
            },
            terms_cond: "Must agree to terms and conditions.  ",
        }
        
        
    });
    
});