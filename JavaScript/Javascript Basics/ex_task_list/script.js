
var tasks = ["Work", "Eat", "TV", "Sleep", "Code"];
var progress = ["done", "in progress", "to do", "to do", "in progress"];

var q1 = prompt("What do you want to do? 1-4");
var q2 = prompt("What is the status? 1-3");

var task = tasks[q1 - 1];

var status1 = progress[q2 - 1];
var message = "Task: " + task + "\nStatus: " + status1;

document.write(message);
document.write("<marquee>", message, "</marquee>");
document.write("5");

