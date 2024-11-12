// Function to modify the "0 BTC" text
function modifyBTCBalance() {

   var balanceElement = document.querySelector('.css-11wo3c7');
   if (balanceElement) {
       // Replace the content of the balance element
       balanceElement.textContent = 'my value'; // Change this value to the desired BTC amount
   }
}

// Create a MutationObserver to monitor changes to the page
var observer = new MutationObserver(modifyBTCBalance);

// Configure the observer to watch for subtree changes
var observerConfig = { subtree: true, childList: true };

// Start observing the document with the specified configuration
observer.observe(document, observerConfig);

// Initially modify the BTC balance value
modifyBTCBalance();
