/* eslint-disable default-case */
const http = require('http');
const url = require('url');
const fs = require('fs');
const { parse } = require('querystring');

const file = 'form.html';

http.createServer((request, response) => {
  console.log('--------------------------------------');
  console.log(`The relative URL of the current request: ${request.url}\n`);
  const url_parts = url.parse(request.url, true); // parsing (relative) URL
  // Compare the relative URL
  switch (url_parts.pathname) {
    // if relative URL is '/' then send, to a browser,
    // the contents of a file (an HTML document) - its name contains the 'file' variable
    case '/':
      fs.stat(file, (err, stats) => {
        if (err == null) { // If the file exists
          fs.readFile(file, (erro, data) => { // Read it content
            response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
            response.write(data); // Send the content to the web browser
            response.end();
          });
        } else { // If the file does not exists
          response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
          response.write(`The ${file} file does not exist`);
          response.end();
        } // else
      }); // fs.stat
      break;

    // Process the form content if relative URL is '/submit'
    case '/submit':
      // eslint-disable-next-line no-case-declarations
      const welcome = `Witaj ${url_parts.query.imie}`;
      response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
      response.write(welcome); // Data (response) that we want to send to the web browser
      response.end(); // Sending the answer
      console.log(`The server sent the '${welcome}' text to the browser`);
      break;

    case '/post':
      // eslint-disable-next-line no-case-declarations
      let body = '';
      request.on('data', (chunk) => {
        body += chunk.toString(); // convert Buffer to string
      });
      request.on('end', () => {
        body = parse(body);
        response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
        response.write(`Witaj ${body.imie}`);
        response.end();
      });

    // Other cases
  } // switch
}).listen(8001);
console.log('The server was started on port 8001');
console.log("To end the server, press 'CTRL + C'");
