var output = document.getElementById("output");
var myObj = {
    name: "John",
    age: 30,
    cars: ["Ford", "BMW", "Fiat"],
};
var myString = JSON.stringify(myObj);
console.log(myObj);
console.log(myString);
myStringToJson = JSON.parse(myString);
console.log(myStringToJson.cars);
