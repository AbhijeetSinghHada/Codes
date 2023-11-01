canvas = document.getElementById("canvas1"); //type : canvas
var ctx = canvas.getContext("2d");

canvas.width = 400;
canvas.height = 600;

ctx.fillStyle = "#" + Math.floor(Math.random() * 0xffffff).toString(16);
ctx.fillRect(10, 30, 100, 100);
ctx.lineWidth = 1;
ctx.strokeRect(10, 150, 100, 100);
ctx.strokeStyle = "#" + Math.floor(Math.random() * 0xffffff).toString(16);
ctx.moveTo(10, 270);
ctx.lineTo(110, 370);
ctx.stroke();
ctx.beginPath();
ctx.arc(60, 430, 50, 0, 2 * Math.PI);
ctx.stroke();
ctx.fillText("Hello World", 120, 450);
