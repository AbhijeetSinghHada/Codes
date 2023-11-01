// const radius = [3,6,1,5];

// const calculateArea = function (radius) {
//     const output = [];
//     for (let i = 0; i < radius.length; i++) {
//         output.push(Math.PI * radius[i] * radius[i]);
//     }
//     return output;
// };
// const calculateCircumference = function (radius) {
//     const output = [];
//     for (let i = 0; i < radius.length; i++) {
//         output.push(2 * Math.PI * radius[i]);
//     }
//     return output;
// };

// console.log(calculateArea(radius));
// // Output: [ 28.274333882308138, 113.09733552923255, 3.141592653589793, 78.53981633974483 ]

// // Now we will use functional programming to do the same task

// const calculate = function (radius, logic) {
//     const output = [];
//     for (let i = 0; i < radius.length; i++) {
//         output.push(logic(radius[i]));
//     }
//     return output;
// };
// const area = function (radius) {
//     return Math.PI * radius * radius;
// };
// const circumference = function (radius) {
//     return 2 * Math.PI * radius;
// };
// console.log(calculate(radius, area));
// // Output: [ 28.274333882308138, 113.09733552923255, 3.141592653589793, 78.53981633974483 ]
// console.log(calculate(radius, circumference));
// // Output: [ 18.84955592153876, 37.69911184307752, 6.283185307179586, 31.41592653589793 ]

// // ****************************************************************
// // Example using a square function

const side = [3, 6, 1, 5];

const calculateArea = function (side) {
    const output = [];
    for (let i = 0; i < side.length; i++) {
        output.push(side[i] * side[i]);
    }
    return output;
};
const calculatePerimeter = function (side) {
    const output = [];
    for (let i = 0; i < side.length; i++) {
        output.push(4 * side[i]);
    }
    return output;
};

console.log(calculateArea(side));
// Output: [ 9, 36, 1, 25 ]
console.log(calculatePerimeter(side));
// Output: [ 12, 24, 4, 20 ]

// Now we will use functional programming to do the same task

const calculate = function (side, logic) {
    const output = [];
    for (let i = 0; i < side.length; i++) {
        output.push(logic(side[i]));
    }
    return output;
};
const area = function (side) {
    return side * side;
};
const perimeter = function (side) {
    return 4 * side;
};
console.log(calculate(side, area));
// Output: [ 9, 36, 1, 25 ]
console.log(calculate(side, perimeter));
// Output: [ 12, 24, 4, 20 ]
