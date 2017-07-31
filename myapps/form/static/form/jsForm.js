$(document).ready(function () {

    $.validator.addMethod("alphanumeric", function(value, element) {
        return this.optional(element) || value == value.match(/^[a-zA-Z0-9]+$/);
    });


    $('#loginForm').validate({ // initialize the plugin
    
        errorClass: "my-error-class",
        validClass: "my-valid-class",
        rules: {
            username: {
                required: true,
                minlength: 5,
                alphanumeric : true
            },
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
            username: {
                required: "Please enter user name",
                alphanumeric: "username must be alphanumeric"
            },
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
    
    
   
    
});