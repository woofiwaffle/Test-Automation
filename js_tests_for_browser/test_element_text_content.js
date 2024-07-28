// for the main page (dashboard page)

(function() {
    const selector = ".oxd-main-menu-item";
    const expectedText = "Admin";

    const element = document.querySelector(selector);

    if(element && element.textContent === expectedText){
        console.log(`test_element_text_content: Test passed - Element with selector "${selector}" has correct text.`);
    }
    else{
        console.error(`test_element_text_content: Test failed - Element with selector "${selector}" 
        does not have the expected text "${expectedText}".`);
    }
})();
