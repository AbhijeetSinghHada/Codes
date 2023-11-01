output = document.getElementById("message");
if (localStorage.getItem("msg")) {
    value = localStorage.getItem("msg");
    count = localStorage.getItem("counter");
    output.innerHTML = value + "<br>" + count + "<br>";
}

let msg = "Hello, Worrrrrrrrrld";
localStorage.setItem("msg", msg);
if (!localStorage.getItem("counter")) {
    localStorage.setItem("counter", 0);
} else {
    let val = localStorage.getItem("counter");
    val = Number(val) + 1;
    localStorage.setItem("counter", val);
}
