var items = [
    { name: "iPhone", details: "Apple iPhone 12", price: 1000, quantity: 1 },
    { name: "Samsung", details: "Samsung Galaxy S21", price: 900, quantity: 1 },
    { name: "Google", details: "Google Pixel 5", price: 800, quantity: 1 },
    { name: "Huawei", details: "Huawei P40 Pro", price: 700, quantity: 1 },
    { name: "OnePlus", details: "OnePlus 9 Pro", price: 600, quantity: 1 },
    { name: "Xiaomi", details: "Xiaomi Mi 11", price: 500, quantity: 1 },
    { name: "Oppo", details: "Oppo Find X3 Pro", price: 400, quantity: 1 },
    { name: "Vivo", details: "Vivo X60 Pro", price: 300, quantity: 1 },
    { name: "Realme", details: "Realme GT", price: 200, quantity: 1 },
    { name: "Motorola", details: "Motorola Edge", price: 100, quantity: 1 },
    { name: "Nokia", details: "Nokia 8.3", price: 50, quantity: 1 },
    { name: "Asus", details: "Asus Zenfone 8", price: 25, quantity: 1 },
    { name: "Sony", details: "Sony Xperia 1 III", price: 10, quantity: 1 },
    { name: "LG", details: "LG Wing", price: 5, quantity: 1 },
    { name: "HTC", details: "HTC U12+", price: 1, quantity: 1 },
];
var html = "<br>";
window.onload = init;
var html = "<br>";
var shopcart = [];
window.onload = init;

function init() {
    buildItems();
    var q = document.querySelectorAll(".productItem");
    for (var x = 0; x < q.length; x++) {
        q[x].addEventListener("click", function (e) {
            e.preventDefault();
            addToCart();
        });
    }
    outputCart();
}

function addToCart() {
    var iteminfo = event.target.dataset;
    var itemincart = false;
    iteminfo.qty = 1;
    shopcart.forEach(function (v) {
        if (v.id == iteminfo.id) {
            v.qty = parseInt(v.qty) + parseInt(iteminfo.qty);
            itemincart = true;
        }
    });
    if (!itemincart) {
        shopcart.push(iteminfo);
    }
    localStorage.setItem("scart", JSON.stringify(shopcart));
    outputCart();
}

function outputCart() {
    if (localStorage.getItem("scart") != null) {
        shopcart = JSON.parse(localStorage.getItem("scart"));
    }
    var html =
        "<table><tr><th>Item</th><th>Quantity</th><th>cost</th><th>id</th><th>subtotal</th><th>Options</th></tr>";
    var total = 0;
    shopcart.forEach(function (v) {
        var stotal = v.qty * v.price;
        total += stotal;
        html +=
            "<tr><td>" +
            v.name +
            "(" +
            v.s +
            ")</td><td>" +
            v.qty +
            "</td><td>" +
            v.price +
            "</td><td>" +
            v.id +
            "</td><td>" +
            fMoney(stotal) +
            '</td><td><span class="remove btn" onclick="remove(' +
            v.id +
            ')">x</span></td></tr>';
    });
    html += "<tr><td colspan=6>Total " + fMoney(total) + "</td></tr></table>";
    document.getElementById("output2").innerHTML = html;
}

function buildItems() {
    var x = 0;
    items.forEach(function (v) {
        html +=
            '<div class="item"><h3>' +
            v.name +
            '</h3><img src="http://placehold.it/350x150" class="img-fluid"><div>' +
            v.details +
            ' <br><a href="#" class="productItem" data-name="' +
            v.name +
            '" data-s="' +
            v.details +
            '"  data-price="' +
            v.price +
            '" data-id="' +
            x +
            '" >Add to Cart</a></div>' +
            fMoney(v.price) +
            "</div>";
        x++;
    });
    document.getElementById("output").innerHTML += html;
}

function remove(id) {
    for (var x = 0; x < shopcart.length; x++) {
        if (shopcart[x].id == id) {
            var rem = shopcart.splice(x, 1);
            console.log(rem);
        }
    }
    localStorage.setItem("scart", JSON.stringify(shopcart));
    outputCart();
}

function fMoney(n) {
    return "$" + (n / 100).toFixed(2);
}
