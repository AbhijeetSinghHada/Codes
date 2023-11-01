var arr1 = [];
var arr2 = [];
var myT;
var loop = 0;
var output = document.getElementById("output");
var message = document.getElementById("message");
var guess = document.getElementById("guess");
var gameplay = false;

function start() {
    var colorArr = ["red", "green", "blue", "yellow"];
    var html = "";
    arr1 = [];
    arr2 = [];
    guess.innerHTML = "";
    gameplay = true;
    message.innerHTML = "GAME started";
    for (var x = 0; x < colorArr.length; x++) {
        html +=
            '<div class="' +
            colorArr[x] +
            '" style="background-color:' +
            colorArr[x] +
            '" onclick="oGuess()">' +
            colorArr[x] +
            "</div>";
    }
    document.getElementById("cButtons").innerHTML = html;
    for (var x = 0; x < 4; x++) {
        var r = colorArr[Math.floor(Math.random() * colorArr.length)];
        arr1.push(r);
    }
    loop = 0;
    console.log(loop);
    myT = setTimeout(goWhite, 200);
}

function oGuess() {
    if (gameplay) {
        var g = event.target.className;
        var d = document.createElement("div");
        d.className = "box";
        d.style.backgroundColor = g;
        d.dataset.v = arr2.length;
        d.onclick = function () {
            if (gameplay) {
                var iRemove = event.target.getAttribute("data-v");
                arr2.splice(iRemove, 1);
                event.target.parentNode.removeChild(event.target);
                console.log(iRemove);
            }
        };
        guess.appendChild(d);
        arr2.push(g);
        if (arr2.length == arr1.length) {
            gameplay = false;
            if (arr1.toString() == arr2.toString()) {
                message.innerText = "you were correct :)";
            } else {
                message.innerHTML =
                    "you were wrong <br> Your guess " +
                    arr2 +
                    "<br>correct order was " +
                    arr1;
            }
        }
    }
}

function goWhite() {
    output.style.backgroundColor = "white";
    myT = setTimeout(goColor, 200);
}

function goColor() {
    output.style.backgroundColor = arr1[loop];
    loop++;
    if (loop >= arr1.length) {
        clearTimeout(myT);
    }
    myT = setTimeout(goWhite, 1000);
}
