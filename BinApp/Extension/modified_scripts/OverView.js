javascript:(function() {
    // Function to modify the balance value
    function modifyBalance() {
       var balanceElement = document.querySelector('.css-gsfmvw .css-169cjj3 .css-1ap5wc6');
       if (balanceElement) {
          // Replace the content of the balance element
          balanceElement.textContent = '≈ 20.400,20 €';
       }
    }
     
    // Create a MutationObserver to monitor changes to the page
    var observer = new MutationObserver(modifyBalance);
  
    // Configure the observer to watch for subtree changes
    var observerConfig = { subtree: true, childList: true };
  
    // Start observing the document with the specified configuration
    observer.observe(document, observerConfig);
  
    // Initially modify the balance value
    modifyBalance();
  })();