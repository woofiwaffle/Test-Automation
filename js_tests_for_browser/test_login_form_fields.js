//for the login page

(function() {
    const usernameSelector = "input[name='username']";
    const passwordSelector = "input[name='password']";

    const usernameField = document.querySelector(usernameSelector);
    const passwordField = document.querySelector(passwordSelector);

    if(usernameField && passwordField){
        console.log("test_login_form_fields: Test passed - Login form fields are present.");
    }
    else{
        console.error("test_login_form_fields: Test failed - One or more login form fields are missing.");
    }
})();
