// for the main page (dashboard page)

(function() {
    const selector = ".oxd-topbar-header-title";

    const element = document.querySelector(selector);

    if(element){
        console.log(`test_element_presence: Test passed - Element with selector "${selector}" is present.`);
    }
    else{
        console.error(`test_element_presence: Test failed - Element with selector "${selector}" is not found.`);
    }
})();
