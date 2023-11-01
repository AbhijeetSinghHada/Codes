var playLockout = false;
var gamePlay = false;
var tileImages = [],
    tileArray = [],
    tfo = [];
var cardFlipped = -1;
var timer;
var sb = document.getElementById("start");
var message = document.getElementById("message");
var score = document.getElementById("score");
var gameBoard = document.getElementById("gameboard");
sb.addEventListener("click", startGame);

function startGame() {
    // hide start button
    sb.style.display = "none";
    message.innerHTML = "Its working" + gamePlay;
    if (!gamePlay) {
        gamePlay = true;
        buildArray();
        tileArray = tileImages.concat(tileImages);
        shuffleArray(tileArray);
        buildBoard();
    }
}

function buildBoard() {
    var html = "";
    var x = 0;
    tileArray.forEach(function (ele) {
        x++;
        html += '<div class="gameTile">';
        html +=
            '<img id="cardz' +
            x +
            '" src="http://via.placeholder.com/250/000000/ffffff?text=click" onclick="pickCard(' +
            (x - 1) +
            ',this)" class="flipImage"></div>';
    });
    gameBoard.innerHTML = html;
}

function pickCard(i, t) {
    console.log(event.target);
    // not in array of flipped over
    // not locked out
    if (!playLockout && !isinArray(t.id, tfo)) {
        if (cardFlipped >= 0) {
            cardFlip(i, t);
            playLockout = true;
            if (
                checkSrc(tfo[tfo.length - 1]) == checkSrc(tfo[tfo.length - 2])
            ) {
                message.innerHTML = "Match Found";
                cardFlipped = -1;
                playLockout = false;
                if (tfo.length == tileArray.length) {
                    gameover();
                }
            } else {
                message.innerHTML = "No Match";
                timer = setInterval(hideCard, 1000);
            }
            //check to see if its a match
        } else {
            cardFlipped = i;
            cardFlip(i, t);
        }
    } else {
        message.innerHTML = "Locked Out";
    }
}

function gameover() {
    message.innerHTML = "Game Over";
    sb.style.display = "block";
    gamePlay = false;
    tfo = [];
    tileImages = [];
    gameBoard.innerHTML = "";
}

function isinArray(v, array) {
    return array.indexOf(v) > -1;
}

function hideCard() {
    for (var x = 0; x < 2; x++) {
        var vid = tfo.pop();
        document.getElementById(vid).src =
            "http://via.placeholder.com/250/000000/ffffff?text=click";
    }
    clearInterval(timer);
    cardFlipped = -1;
    playLockout = false;
    message.innerHTML = "Select Again";
}

function checkSrc(a) {
    return document.getElementById(a).src;
}

function cardFlip(i, t) {
    t.src = "http://via.placeholder.com/250/ffffff/000000?text=" + tileArray[i];
    tfo.push(t.id);
}

function buildArray() {
    for (var x = 1; x < 7; x++) {
        tileImages.push(x + ".jpg");
    }
}

function shuffleArray(array) {
    for (var x = array.length - 1; x > 0; x--) {
        var holder = Math.floor(Math.random() * (x + 1));
        var itemValue = array[x];
        array[x] = array[holder];
        array[holder] = itemValue;
    }
    return array;
}
