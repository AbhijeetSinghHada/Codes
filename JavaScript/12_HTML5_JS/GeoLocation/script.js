window.onload = init;

function init() {
    navigator.geolocation.getCurrentPosition(placeMap);
}
function placeMap(data, a, b, c) {
    console.dir(data);
    console.log(a);
    console.log(b);
    console.log(c);
}
