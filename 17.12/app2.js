#!/usr/bin/node
// Application using the 'Pug' template system
const express = require('express');
const logger = require('morgan');

const app = express();
const { vars } = require('./app3.js');

let x = 1;
let y = 2;
x = vars.x;
y = vars.y;

// Configuring the application
app.set('views', `${__dirname}/views`); // Files with views can be found in the 'views' directory
app.set('view engine', 'pug'); // Use the 'Pug' template system

// Determining the contents of the middleware stack
app.use(logger('dev')); // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
app.use(express.static(`${__dirname}/public`)); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', (req, res) => { // The first route
  res.render('index', {
    pretty: true, x, y, z: x + y,
  });
});

app.get('/add/:x/:y', (req, res) => {
  const sum = Number(req.params.x) + Number(req.params.y);
  res.render('index', {
    pretty: true, x: req.params.x, y: req.params.y, z: sum,
  });
});

// The application is to listen on port number 3000
app.listen(3000, () => {
  console.log('The application is available on port 3000');
});
