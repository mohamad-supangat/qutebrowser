// ==UserScript==
// @name            Auto visit Faucet pay pay to click
// @description     Auto visit Faucet pay pay to click
// @match           https://faucetpay.io/ptc
// @require         https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.1/jquery.min.js
// ==/UserScript==

$(function () {
  const buttons = $("button.btn-primary");
  for (let button of buttons) {
    button = $(button);
    const button_text = button.html();
    if (button_text.includes("VISIT AD")) {
      button.click();
    }
  }
});
