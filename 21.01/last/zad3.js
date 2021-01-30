/* eslint-disable default-case */
const http = require('http');
const https = require('https');
const url = require('url');
const fs = require('fs');
const { parse } = require('querystring');
const path = require('path');

const directoryPath = path.join(__dirname, 'data');
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

    case '/req':
      // eslint-disable-next-line no-case-declarations
      let body = '';
      request.on('data', (chunk) => {
        body += chunk.toString(); // convert Buffer to string
      });
      request.on('end', () => {
        body = parse(decodeURIComponent(body));
        response.writeHead(200, { 'Content-Type': 'application/json' });
        fs.readdir(directoryPath, (err, files) => {
            if(err) return console.log("dir error");
            let counter = files.length;
            let fileData = {};
            files.forEach((file) => {
                let chunk = []
                fs.readFile(`${directoryPath}/${file}`, 'utf-8', (err, content) => {
                    if(err) return console.log(err);
                    if(`${file}`.search(body.filename) >= 0){
                        
                    let c = `${content}`.split('\n');
                    for(line of c){
                        console.log(line.search(body.data));
                        if(line.search(body.data) >= 0){
                        chunk.push(line);}
                    }
                    fileData[file] = chunk;
                    }counter--;
                    if(counter == 0){
                        console.log(fileData);
                        response.end(JSON.stringify(fileData));
                    }
                });
            })
        })
      });

    // Other cases
  } // switch
}).listen(8003);
console.log('The server was started on port 8003');
console.log("To end the server, press 'CTRL + C'");
