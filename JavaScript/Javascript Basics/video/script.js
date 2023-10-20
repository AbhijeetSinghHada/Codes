// var Question = "What is your name?"
// document.write(Question)

// var ans = prompt(Question);
// console.log(ans);
// document.write("Welcome to my page " + ans + " !")

// alert("Helllloooooo " + ans + " !")

// ***********************************

// var num1 = prompt("Enter number 1 : ");
// var num2 = prompt("Enter number 2 : ");

// num1 = Number(num1)
// num2 = parseInt(num2)
// document.write("The sum of " + num1 + " and " + num2 + " is " + (num1 + num2) + "<br>");

// *********************************************

// var myVar1 = ["string", 12, "Abhi", false, "Horse"]

// myVar2 = myVar1.splice(2,)
// myVar1[myVar1.length + myVar2.length + 6] = myVar2
// myVar1.fill("Hellooo", 2, 11)
// // myVar1.sort()
// // console.log(myVar1)
// // x = myVar1.pop() // removes last element
// // console.log(x)
// // x = myVar1.splice(3, 100) // removes from index 3 to 100
// // console.log(x)

// // myVar1.shift() // removes first element

// // myVar1.unshift("FDSEWFSGFD") // adds element to the beginning of the array


// console.log(myVar1)


// *********************************************

// var newArray = ["Horse", "Dog", "Cat", "Rabbit", "Tiger", "Lion", "Elephant", "Monkey", "Donkey", "Zebra"]
// var response = prompt("What you want to see ? ")
// var index = Number(response)

// msg = index > -1 && index < newArray.length ? "Found" : "Not Found";
// console.log(msg)


// ***************************************************************
// var newArray = ["Horse", "Dog", "Cat", "Rabbit", "Tiger", "Lion", "Elephant", "Monkey", "Donkey", "Zebra"]

// for (var x in newArray) { // x is index for every element in the array
//     console.log(x) // prints index
//     console.log(newArray[x]) // prints value

// }
// ***************************************************************

// var obj = {
//     color: "RED",
//     brand: "BMW",
//     price: 1000000,
//     isAvailable: true,
// }

// console.log(obj)
// console.log(obj.price)
// prop = "price"
// // console.log(obj["price"])
// console.log(obj[prop])

// console.log(obj)

// ***************************************************************

// var obj = {
//     color: "RED",
//     brand: "BMW",
//     price: 1000000,
//     isAvailable: true,
// }

// for (x in obj) {
//     console.log(x + " " + obj[x])
// }


// ***************************************************************

var obj = {
    color: "RED",
    brand: "BMW",
    price: 1000000,
    isAvailable: true,
}

var newArray = ["Horse", "Dog", "Cat", "Rabbit", "Tiger", "Lion", "Elephant", "Monkey", "Donkey", "Zebra"]


console.log(newArray.find("Horse"))