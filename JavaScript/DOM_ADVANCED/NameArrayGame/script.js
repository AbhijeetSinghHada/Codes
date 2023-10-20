var myArray = [];
var people = [
    "Laurence",
    "Mike",
    "John",
    "Larry",
    "Kim",
    "Joanne",
    "Lisa",
    "Janet",
    "Jane",
];
var key;

function start() {
    myArray = people.slice();
    myArray.sort(function (a, b) {
        return 0.5 - Math.random();
    });
    console.log(myArray);
    build();
    findPerson();
}

function findPerson() {
    key = myArray[Math.floor(Math.random() * myArray.length)];
    message1("Find this name " + key);
}

function build() {
    var html = "<h1>Name Game</h1>";
    for (var x = 0; x < myArray.length; x++) {
        var str = myArray[x];
        var shuffled = str
            .split("")
            .sort(function () {
                return 0.5 - Math.random();
            })
            .join("");
        html +=
            '<div class="box" onmouseover="uText(this,\'' +
            shuffled +
            "')\" onmouseout=\"uText(this,'Hidden " +
            (x + 1) +
            "')\" onclick=\"eEle(this,'" +
            str +
            "')\" >Hidden " +
            (x + 1) +
            "</div>";
    }
    document.getElementById("output").innerHTML = html;
}

function uText(t, mes) {
    t.innerHTML = mes;
}

function eEle(t, s) {
    if (s == key) {
        var n = myArray.indexOf(s);
        message2("correct");
        t.parentNode.removeChild(t);
        myArray.splice(n, 1);
        findPerson();
    } else {
        message2("wrong");
    }
    if (myArray.length <= 0) {
        message1("GAME OVER");
    }
}

function message1(message) {
    document.getElementById("message1").innerHTML = message;
}

function message2(message) {
    document.getElementById("message2").innerHTML = message;
}
