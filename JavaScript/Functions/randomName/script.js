function displayName() {
    object = document.getElementById('object1');
    response = prompt("Please Enter Your Name : ");
    arr = ["Good", "Bad", "Ok"];
    random_adjective = arr[Math.floor(Math.random() * arr.length)];
    object.innerHTML += "<br>" + random_adjective + "    " + response + "<br>"
}