var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");
var imgLoader = document.getElementById("imgLoader");
imgLoader.addEventListener("change", upImage, false);

function upImage() {
    var r = new FileReader();
    r.readAsDataURL(event.target.files[0]);
    r.onload = function (event) {
        var img = new Image();
        img.src = event.target.result;
        img.width = canvas.width;
        img.height = canvas.height;
        img.onload = function () {
            ctx.drawImage(img, 0, 0);
            ctx.font = "30px Arial";
            ctx.fillText("JavaScript Course", 10, 100);
        };
        console.log(r);
    };
}
