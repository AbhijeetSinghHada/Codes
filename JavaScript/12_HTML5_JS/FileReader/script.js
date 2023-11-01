var message = document.getElementById("message");
if (window.FileReader) {
    message.innerText = "File Reader is available";
} else {
    message.innerText = "File Reader is not available";
}
function uploadFile(files) {
    message.innerHTML = "";
    for (var file of files) {
        message.innerHTML += file.name + "<br>";
        let fReader = new FileReader();
        fReader.onload = function (event) {
            message.innerHTML += event.target.result + "<br>";
        };
        fReader.readAsText(file);
    }
}
