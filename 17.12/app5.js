const express = require('express');
const logger = require('morgan');
const http = require('http');

const app = express();

// Configuring the application
app.set('views', `${__dirname}/views`); // Files with views can be found in the 'views' directory
app.set('view engine', 'pug'); // Use the 'Pug' template system

// Determining the contents of the middleware stack
app.use(logger('dev')); // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
app.use(express.static(`${__dirname}/public`)); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', (req, res) => { // The first route
  res.render('table', {
    pretty: true, // x, y, z: x + y,
  });
});

app.get('/*', (req, res) => {
  let par = req.params[0].split('/');
  const date1 = par[0];
  const date2 = par[1];
  par = par.slice(2);
  let reqN = par.length;
  const matrix = {};
  par.forEach((curr) => {
    http.request({
      hostname: 'api.nbp.pl',
      port: 80,
      path: `/api/exchangerates/rates/a/${curr}/${date1}/${date2}/?format=json`,
      method: 'GET',
    }, (resp) => {
      resp.on('data', (d) => {
        const { rates } = JSON.parse(d);
        console.log(rates);
        matrix[curr] = rates;
        console.log(matrix);
        reqN -= 1;
        if (reqN == 0) {
          res.render('table', {
            pretty: true, m: matrix, c: curr, p: par,
          });
        }
      });
    }).end();
  });
});

// The application is to listen on port number 3000
app.listen(3000, () => {
  console.log('The application is available on port 3000');
});
