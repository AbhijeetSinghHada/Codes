var myArray = [
    "Laurence",
    "Mike",
    "John",
    "Larry",
    "Kim",
    "Joanne",
    "Lisa",
    "Janet",
    "Jane",
];
window.onload = build;
document.getElementById("addNew").addEventListener("click", addN, false);

function addN() {
    var a = document.getElementById("addFriend").value;
    myArray.push(a);
    build();
}

function build() {
    var html = "<h1>Table</h1><table>";
    for (var x = 0; x < myArray.length; x++) {
        html +=
            '<tr id="id' +
            x +
            '" data-row="' +
            x +
            '"><td>' +
            myArray[x] +
            '</td><td><a href="#" data-action="delete">Del</a></td><td><a href="#" data-action="edit">Edit</a></td></tr>';
    }
    document.querySelector(".output").innerHTML = html;
    var action_data = document.querySelectorAll('[data-action="delete"]');
    for (var x = 0; x < action_data.length; x++) {
        action_data[x].addEventListener("click", function () {
            event.preventDefault();
            var iValue = this.closest("[data-row]").getAttribute("data-row");
            var r = myArray.splice(iValue, 1);
            build();
            console.log(r);
        });
    }
    var dae = document.querySelectorAll('[data-action="edit"]');
    for (var x = 0; x < dae.length; x++) {
        dae[x].addEventListener("click", function () {
            event.preventDefault();
            var row = this.closest("[data-row]");
            var rid = row.getAttribute("data-row");
            row.style.backgroundColor = "Yellow";
            var td = row.firstElementChild;
            var input = document.createElement("input");
            input.type = "text";
            input.value = td.innerText;
            td.innerHTML = "";
            td.appendChild(input);
            input.focus();
            input.onblur = function () {
                td.removeChild(input);
                td.innerHTML = input.value;
                myArray[rid] = input.value;
                row.style.backgroundColor = "White";
            };
        });
    }
    console.log(action_data);
}
