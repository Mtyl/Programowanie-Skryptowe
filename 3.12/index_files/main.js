const iterations = 100;
const multiplier = 1000000000;

var worker = new Worker("index_files/calculate.js");

/**
 * Doing the pointless computations. 
 */
var pointlessComputationsButton = document.getElementById("pointless-computations");
pointlessComputationsButton.disabled = false;
pointlessComputationsButton.addEventListener("click", doPointlessComputations, false);

function doPointlessComputations() {
  pointlessComputationsButton.disabled = true;

  var useWorkerButton = document.getElementById("use-worker");
  var useBlockingJsButton = document.getElementById("use-blocking-js");
  var useRequestAnimationFrame = document.getElementById("use-request-animation-frame");
  var useInterval = document.getElementById("use-interval");
  var useTimeout = document.getElementById("use-timeout");

  if (useBlockingJsButton.checked) {
    doPointlessComputationsWithBlocking();
  }
  if (useRequestAnimationFrame.checked) {
    doPointlessComputationsWithRequestAnimationFrame();
  }
  if (useWorkerButton.checked) {
    doPointlessComputationsInWorker();
  }
  if (useInterval.checked){
    doPointlessComputationsWithInterval();
  }
  if (useTimeout.checked){
    doPointlessComputationsWithTimeout();
  }
}

/**
 * Start/stop animation
 */
var started = false;
var startStopButton = document.getElementById("start-stop");

startStopButton.addEventListener("click", startStop, false);

function startStop() {
  started = !started;
  if (started) {
    container.classList.add("started");
    startStopButton.value = "Stop animations";
  }
  else {
   container.classList.remove("started");
   startStopButton.value = "Start animations";
  }
}
