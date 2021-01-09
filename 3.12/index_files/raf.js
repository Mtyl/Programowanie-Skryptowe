function doPointlessComputationsWithRequestAnimationFrame() {
  var t0 = performance.now();
  function testCandidate(index) {
    // finishing condition
    if (index == iterations) {
      console.log(primes);
      pointlessComputationsButton.disabled = false;
      mydata.datasets[0].data[1] = performance.now() - t0;
      window.myChart.update();
      return;
    }
    // test this number
    var candidate = index * (multiplier * Math.random());
    var isPrime = true;
    for (var c = 2; c <= Math.sqrt(candidate); ++c) {
      if (candidate % c === 0) {
          // not prime
          isPrime = false;
          break;
       }
    }
    if (isPrime) {
      primes.push(candidate);
    }
    // schedule the next
    var testFunction = testCandidate.bind(this, index + 1);
    window.requestAnimationFrame(testFunction);
  }

  var primes = [];
  var testFunction = testCandidate.bind(this, 0);
  window.requestAnimationFrame(testFunction);
}


function doPointlessComputationsWithInterval() {
  index = 0;
  var t0 = performance.now();
  function testCandidate() {
    // finishing condition
    if (index == iterations) {
      console.log(primes);
      pointlessComputationsButton.disabled = false;
      clearInterval(intervalId);
      mydata.datasets[0].data[3] = performance.now() - t0;
      window.myChart.update();
      return;
    }
    // test this number
    var candidate = index * (multiplier * Math.random());
    var isPrime = true;
    for (var c = 2; c <= Math.sqrt(candidate); ++c) {
      if (candidate % c === 0) {
          // not prime
          isPrime = false;
          break;
       }
    }
    if (isPrime) {
      primes.push(candidate);
    }
    index++;
  }

  var primes = [];
  var intervalId = setInterval(testCandidate, 10);
}


function doPointlessComputationsWithTimeout() {
  index = 0;
  t0 = performance.now();
  function testCandidate() {
    // finishing condition
    if (index == iterations) {
      console.log(primes);
      pointlessComputationsButton.disabled = false;
      mydata.datasets[0].data[4] = performance.now() - t0;
      window.myChart.update();
      return;
    }
    // test this number
    var candidate = index * (multiplier * Math.random());
    var isPrime = true;
    for (var c = 2; c <= Math.sqrt(candidate); ++c) {
      if (candidate % c === 0) {
          // not prime
          isPrime = false;
          break;
       }
    }
    if (isPrime) {
      primes.push(candidate);
    }
    index++;
    setTimeout(testCandidate, 10);
  }

  var primes = [];
  testCandidate();
}