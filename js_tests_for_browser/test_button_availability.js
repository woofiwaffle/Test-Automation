// for the login page

(function() {
    const selector = "button[type='submit']";

    const button = document.querySelector(selector);

    if(button && !button.disabled){
        console.log(`test_button_availability: Test passed - Button with selector "${selector}" is available.`);
    }
    else{
        console.error(`test_button_availability: Test failed - Button with selector "${selector}" is not available or is disabled.`);
    }
})();
