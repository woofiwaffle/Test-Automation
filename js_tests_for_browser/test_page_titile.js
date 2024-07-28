// for the login page

(function() {
    const expectedTitle = "OrangeHRM";

    const actualTitle = document.title;

    if(actualTitle === expectedTitle){
        console.log("Test passed: Page title is correct.");
    }
    else{
        console.error(`Test failed: Expected title "${expectedTitle}" but got "${actualTitle}".`);
    }
})();