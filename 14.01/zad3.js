/* eslint-disable default-case */
const http = require('http');
const https = require('https');
const url = require('url');
const fs = require('fs');
const { parse } = require('querystring');

const file = 'zad3.html';

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

    case '/files':
      // eslint-disable-next-line no-case-declarations
      let body = '';
      request.on('data', (chunk) => {
        body += chunk.toString(); // convert Buffer to string
      });
      request.on('end', () => {
        body = parse(decodeURIComponent(body));
        fs.readdir("data", (err, files) => {
            if(err) return console.log(err);
            files = files.filter(file => file.includes(body.name));
            counter = files.length;
            response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
            response.write("<div id='found'>");
            files.forEach((f) => {
                fs.readFile(`data/${f}`, (erro, data) => {
                    let out = "";
                    data = `${data}`
                    if(erro) return console.log(erro);
                    let fil = data.split("\n");
                    fil = fil.filter(line => line.includes(body.data));
                    out += `<ul>${f}</ul>`;
                    for(lin of fil){
                        out += `<li>${lin}</li>`
                    }
                    response.write(out);
                    counter--;
                    if(counter == 0)
                    response.end("</div>") 
                })
            })
            if(files.length == 0){
                response.end("</div>")
            }
        })
      });

    // Other cases
  } // switch
}).listen(8000);
console.log('The server was started on port 8000');
console.log("To end the server, press 'CTRL + C'");
