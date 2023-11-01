const cart = ["shoes", "pants", "pyjamas"];

api.createOrder(cart, function () {
    api.proceedToPayment(function () {});
});
// Here we are assuming that createOrder will call the
// callback function at some point in the future.
// We don't know when, but we depend on it to happen.
// That's a huge problem. We should not be depending on someone else's written code
// it might be a case that the code might have been written by some intern and it might be buggy
