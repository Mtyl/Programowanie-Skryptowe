const http = require('http');
const url = require('url');
const { stat, readFile } = require('fs');

http.createServer((request, response) => {
  /*
      ,,request'' - input stream - contains data received from the browser,
      e.g. encoded contents of HTML form fields

      ,,response'' - output stream - put in it data that you want to send back to the browser.
         The answer sent by this stream must consist of two parts: the header and the body.
         The header contains, among others, information about the type
         (MIME) of data contained in the body.
         The body contains the correct data, e.g. a form definition.

    */
  console.log('--------------------------------------');
  console.log(`The relative URL of the current request: ${request.url}\n`);
  // eslint-disable-next-line camelcase
  const url_parts = url.parse(request.url, true); // parsing (relative) URL

  if (url_parts.pathname === '/submit') { // Processing the form content, if the relative URL is '/ submit'
    const { path } = url_parts.query; // Read the contents of the field (form) named 'name'
    console.log('Creating a response header');
    response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' }); // Creating an answer header - we inform the browser that the body of the answer will be plain text
    console.log('Creating the body of the response');
    response.write(`Path: ${path}`); // Place given data (here: 'Hello' text) in the body of the answer
    response.write('\n\n');
    stat(path, (err, stats) => {
      if (err) {
        response.write('No such file or directory!');
        response.end();
      } else if (stats.isDirectory()) {
        response.write('It is a directory!');
        response.end();
      } else if (stats.isFile()) {
        response.write('It is a file!\n\n');
        readFile(path, 'utf-8', (error, data) => {
          if (error) {
            response.write('File not readable!');
            response.end();
          } else {
            response.write(data);
            response.end();
          }
        });
      } else {
        response.write('Unexpected error!');
        response.end();
      }
    });

    // The end of the response - send it to the browser
    console.log('Sending a response');
  } else { // Generating the form
    console.log('Creating a response header');
    response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); // Creating a repsonse header - we inform the browser that the body of the response will be HTML text
    // and now we put an HTML form in the body of the answer
    console.log('Creating a response body');
    response.write('<form method="GET" action="/submit">');
    response.write('<label for="path">Give path</label>');
    response.write('<input name="path">');
    response.write('<br>');
    response.write('<input type="submit">');
    response.write('<input type="reset">');
    response.write('</form>');
    response.end(); // The end of the response - send it to the browser
    console.log('Sending a response');
  }
}).listen(8080);
console.log('The server was started on port 8080');
console.log("To end the server, press 'CTRL + C'");
