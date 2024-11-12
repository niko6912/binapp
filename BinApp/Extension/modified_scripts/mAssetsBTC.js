javascript:(function() {
    // Function to modify the balance value
    function modifyBalance() {
       var balanceElement = document.querySelector('.css-35z0bk');
       if (balanceElement) {
          // Replace the content of the balance element
          balanceElement.textContent = '1.2';
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