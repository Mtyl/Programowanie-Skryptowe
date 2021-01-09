#!/usr/bin/node
// No use of any template system
const express = require('express');
const logger = require('morgan');

const app = express();
const { vars } = require('./app3.js');

let x = 1;
let y = 2;
x = vars.x;
y = vars.y;

// Determining the contents of the middleware stack
app.use(logger('dev')); // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
app.use(express.static(`${__dirname}/public`)); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', (req, res) => { // The first route
  res.send(`<h1>Hello World!</h1><br><h3>${x} + ${y} = ${x + y}</h3>`);
  res.send(); // Send a response to the browser
});

app.get('/add/:x/:y', (req, res) => {
  const xs = Number(req.params.x);
  const ys = Number(req.params.y);
  res.send(`<h1>Hello World!</h1><br><h3>${xs} + ${ys} = ${xs + ys}</h3>`);
  // res.send(); // Send a response to the browser
});
// The application is to listen on port number 3000
app.listen(3000, () => {
  console.log('The application is available on port 3000');
});
