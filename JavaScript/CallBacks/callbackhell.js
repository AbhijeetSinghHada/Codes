// Working on a shoping website
// What are callbacks?
// Callbacks are functions that are passed as arguments to other functions
// Callbacks are used to make sure that certain code doesn't execute until other code has already finished execution

const cart = ["shoes", "pants", "pyjamas"];

api.createOrder(cart, function (orderId) {
    // now this requires paymentAuthorization once we create order after this
    api.proceedToPayment(function (orderId) {
        api.showOrderDetails(function () {
            // after payment orderdetails should be visible
            api.updateWallet(); //the wallet should be updated after order details are visible
        });
    });
});

// This grows the code horizontally instead of vertically.
// So whole of this made a callback hell which is not good for code readability and maintainability
// So we will use promises to avoid this callback hell

// Promises
// Promises are a way to organize callbacks, they are a way to deal with asynchronous code
// Promises are objects that represent the eventual completion or failure of an asynchronous operation
