const supertest = require('supertest');
const { readFile } = require('fs');
// This agent refers to PORT where program is runninng.
const server = supertest.agent('http://localhost:3000');
const files = ['1.json', '2.json'];
// UNIT test begin
describe('GET /', () => {
  files.forEach((path) => {
    it(`Test file: ${path}`, (done) => {
      const opHtml = [];
      readFile(`operations/${path}`, 'utf-8', (error, json) => {
        if (error) return;
        const { operations } = JSON.parse(json);
        let end = 0;
        operations.forEach((op) => {
          switch (op.op) {
            case '*':
              opHtml.push([`<p>${op.x} * ${op.y} = ${op.x * op.y}</p>`]);
              break;
            case '+':
              opHtml.push([`<p>${op.x} + ${op.y} = ${op.x + op.y}</p>`]);
              break;
            case '-':
              opHtml.push([`<p>${op.x} - ${op.y} = ${op.x - op.y}</p>`]);
              break;
            case '/':
              opHtml.push([`<p>${op.x} / ${op.y} = ${op.x / op.y}</p>`]);
              break;
            default:
              opHtml.push(['ERROR']);
          }
          end += 1;
          if (end == operations.length) {
            server
              .get(`/${path}`)
              .expect((res) => {
                const trHtml = res.text.split('<br>');
                for (let i; i < opHtml.length; i += 1) {
                  if (!trHtml.includes(opHtml[i])
                  ) throw new Error('Incorrect body');
                }
              })
              .expect(200, done);
          }
        });
      });
    });
  });
});
