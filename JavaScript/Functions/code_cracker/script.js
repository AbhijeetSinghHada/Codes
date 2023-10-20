var safeKey = ""
for (let i = 0; i < 3; i++) {
    safeKey += String(Math.floor(Math.random() * 9))
}

output = document.getElementById("output")
// output.innerHTML += safeKey + "<br>"
obj = {}


function checkForSafe() {
    num1 = document.getElementById("value1").value
    num2 = document.getElementById("value2").value
    num3 = document.getElementById("value3").value
    console.log(num1 + num2 + num3)

    afterCheck1 = checkHighLow(num1, safeKey[0])
    afterCheck2 = checkHighLow(num2, safeKey[1])
    afterCheck3 = checkHighLow(num3, safeKey[2])
    numberUser = afterCheck1 + afterCheck2 + afterCheck3
    output.innerHTML += numberUser + "<br>"
    if (numberUser === safeKey) {
        output.innerHTML = "You Guessed It Right......" + "<br>"
    }

}
function checkHighLow(inputNum, SafeKey) {
    if (Number(inputNum) === Number(SafeKey)) {
        return inputNum
    }
    else if (Number(inputNum) > Number(SafeKey)) {
        return "H"
    }
    else {
        return "L"
    }
}