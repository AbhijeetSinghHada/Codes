output = document.getElementById("output");
var str1 =
    "wgvbrsdtds wfe wafew g JavaScript qwfe esfa JavaScripteg gJavaScript";

function validate() {
    var emailPattern = /([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z.]+)/g;
    var email = document.getElementById("email").value;
    if (emailPattern.test(email)) {
        output.innerText = "True";
        x = email.match(emailPattern);
        console.log(x);
    } else {
        output.innerText = "False";
    }
}
