console.dir(window)
object = document.getElementById("output")
for(let i in window){
    object.innerHTML += i + " : " + window[i] + "<br>";
}

var w = window.open("index copy.html")
w.onbeforeunload = function (){
    this.alert("Dont go.....")
}