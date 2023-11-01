setTimeout(function () {
    console.log("I waited 2 seconds");
}, 2000); // Here this function is a callback function
// Callbacks are very important in asynchronous programming in javascript and they are used everywhere
// Example 2
let counter = 0;
function timeout(updateCounter) {
    updateCounter();
    console.log("Inside Timeout and Called a Callback function");
}

timeout(function () {
    counter++;
    console.log("Counter is incremented");
}); // not this anonymous function is a callback function which we don't know when called but it will be called somewhere by timeout function

function main(callBackFunction) {
    // Doing some Task
    callBackFunction();
}

main(function () {
    // I am being passed as a param to x
});
