const { readFile } = require('fs');
const express = require('express');
const logger = require('morgan');

const app = express();

// Determining the contents of the middleware stack
app.use(logger('dev')); // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
app.use(express.static(`${__dirname}/public`)); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

app.get('/:path', (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  readFile(`operations/${req.params.path}`, 'utf-8', (error, json) => {
    if (error) return;
    const { operations } = JSON.parse(json);
    let end = 0;
    operations.forEach((op) => {
      switch (op.op) {
        case '*':
          res.write(`<p>${op.x} * ${op.y} = ${op.x * op.y}</p><br>`);
          break;
        case '+':
          res.write(`<p>${op.x} + ${op.y} = ${op.x + op.y}</p><br>`);
          break;
        case '-':
          res.write(`<p>${op.x} - ${op.y} = ${op.x - op.y}</p><br>`);
          break;
        case '/':
          res.write(`<p>${op.x} / ${op.y} = ${op.x / op.y}</p><br>`);
          break;
        default:
          res.write('ERROR');
      }
      end += 1;
      if (end == operations.length) res.end();
    });
  });
});

app.listen(3000, () => {
  console.log('The application is available on port 3000');
});
