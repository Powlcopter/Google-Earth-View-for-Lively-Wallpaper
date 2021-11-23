var r = document.querySelector(':root');
var rs = getComputedStyle(r);

var imageIDjson;
var imageID;
var nextImageID;

var leanBackDelay = 5000;
var leanBackLoop;
startup();


async function startup() {
  await getIDJson();
  //console.log(imageIDjson);
  chooseNextImage(imageIDjson);
  switchToNextImage();
  chooseNextImage(imageIDjson);
}


function testButton() {

}

function playButton() {
  //console.log("Starting leanback mode with interval " + leanBackDelay + "ms");
  setVar("--play-state", "hidden")
  setVar("--pause-state", "visible")
  window.leanBackLoop = window.setInterval(nextImageButton, leanBackDelay);
}

function pauseButton() {
  //console.log("Pausing leanback mode");
  setVar("--play-state", "visible")
  setVar("--pause-state", "hidden")
  window.clearInterval(window.leanBackLoop);
}

function favButton() {
  //console.log("Adding to favorites...");
  setVar("--next-bg-image", "url(https://www.gstatic.com/prettyearth/assets/full/2406.jpg)")
  //console.log("Added to favorites");
}

function nextImageButton() {
  switchToNextImage();
  chooseNextImage(imageIDjson);
}


async function getIDJson() {
  await fetch("./imageIDs.json")
  .then(response => response.json())
  .then(data => imageIDjson = data);
}

function switchToNextImage() {
  //console.log("Switching to next image...");
  var currentImageURL = getVar("--next-bg-image");
  //console.log("Current image URL: " + currentImageURL);
  setVar("--bg-image", currentImageURL);
  //console.log("Switched to next image");
}

async function loadNextImage() {
  //console.log("Loading next image...");
  await fetch("./imageIDs.json")
  .then(response => response.json())
  .then(data => chooseNextImage(data));
  //console.log("Loaded next image");
}


function chooseNextImage(imageIDs) {
  //console.log("Choosing new Image...");
  var randomID = getRndInt(imageIDs.numOfIDs);
  //console.log("Next image ID: "+ imageIDs.IDs[randomID]);
  setVar("--next-bg-image", addURL(imageIDs.IDs[randomID]));
}

function getRndInt(max) {
    return Math.floor(Math.random() * max);
}

function addURL(ID) {
  return "url(https://www.gstatic.com/prettyearth/assets/full/" + ID + ".jpg)";
}

function getVar(varName) {
  // Get the styles (properties and values) for the root

  value = rs.getPropertyValue(varName)
  //console.log("The value of " + varName + " is: " + value);
  return value;
}

function setVar(varName, value) {
  r.style.setProperty(varName, value);
}