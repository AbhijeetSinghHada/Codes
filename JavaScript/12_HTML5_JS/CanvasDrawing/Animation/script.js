window.onload = init;
canvas = document.getElementById("canvas1"); //type : canvas
var ctx = canvas.getContext("2d");

canvas.width = 400;
canvas.height = 600;

pos1 = {
    x: 25,
    y: 50,
};
pos2 = {
    x: 0,
    y: 50,
};
function init() {
    draw();
}
var offset1 = 1;
var offset2 = 1;
var radius = 50;
function draw() {
    pos1.x += (5 + Math.floor(Math.random() * 5)) * offset1;
    pos1.y += (5 + Math.floor(Math.random() * 5)) * offset2;
    if (pos1.x > canvas.width - radius) {
        offset1 = -1;
        ctx.fillStyle = "#" + Math.floor(Math.random() * 0xffffff).toString(16);
    }
    if (pos1.y > canvas.height - radius) {
        offset2 = -1;
        ctx.fillStyle = "#" + Math.floor(Math.random() * 0xffffff).toString(16);
    }
    if (pos1.x <= radius) {
        offset1 = 1;
        ctx.fillStyle = "#" + Math.floor(Math.random() * 0xffffff).toString(16);
    }
    if (pos1.y <= radius) {
        offset2 = 1;
        ctx.fillStyle = "#" + Math.floor(Math.random() * 0xffffff).toString(16);
    }

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();
    ctx.arc(pos1.x, pos1.y, radius, 0, 2 * Math.PI);
    ctx.fill();

    timeout_ = window.setTimeout(draw, 3);
}
// function draw() {
//     pos1.x += 4;
//     pos2.y += 6;
//     if (pos1.x > canvas.width) {
//         pos1.x = 0;
//     }
//     if (pos2.y > canvas.height) {
//         pos2.y = 0;
//     }

//     ctx.clearRect(0, 0, canvas.width, canvas.height);

//     ctx.beginPath();
//     ctx.fillStyle = "red";
//     ctx.arc(pos1.x + 50, pos1.y, 50, 0, 2 * Math.PI);
//     ctx.fill();

//     ctx.beginPath();
//     ctx.fillStyle = "blue";
//     ctx.arc(pos2.x + 50, pos2.y, 50, 0, 2 * Math.PI);
//     ctx.fill();

//     timeout_ = window.setTimeout(draw, 10);
// }
