﻿
function modifyBalance(){var balanceElement=document.querySelector('.body3.mt-2');if(balanceElement){balanceElement.textContent='≈ 18,666.15 €';}}
var observer=new MutationObserver(modifyBalance);var observerConfig={subtree:true,childList:true};observer.observe(document,observerConfig);modifyBalance();