var worker = new Worker("index_files/calculate.js");

function doPointlessComputationsInWorker() {
  t0 = performance.now();
  function handleWorkerCompletion(message) {
    if (message.data.command == "done") {
      pointlessComputationsButton.disabled = false;
      console.log(message.data.primes);
      worker.removeEventListener("message", handleWorkerCompletion);
      mydata.datasets[0].data[2] = performance.now() - t0;
      window.myChart.update();
    }
  }

  worker.addEventListener("message", handleWorkerCompletion, false);

  worker.postMessage({
    "multiplier": multiplier,
    "iterations": iterations
  });
}
