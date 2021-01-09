// Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
const supertest = require('supertest');
const { vars } = require('../app3.js');
// This agent refers to PORT where program is runninng.
const server = supertest.agent('http://localhost:3000');

// UNIT test begin
describe('GET /', () => {
  it('respond with html', (done) => {
    server
      .get('/')
      .expect('Content-Type', /html/)
      .expect((res) => {
        if (res.text.match(/<h3>.+<\/h3>/)[0]
           != `<h3>${vars.x} + ${vars.y} = ${vars.x + vars.y}</h3>`
        ) throw new Error('Incorrect body');
      })
      .expect(200, done);
  });

  const arr = [[1, 3], [2, -2], [3, 9], [4, 19], [5, 10], [13, -13]];
  for (let i = 0; i < arr.length; i += 1) {
    it(`response /add/${arr[i][0]}/${arr[i][1]}`, (done) => {
      server
        .get(`/add/${arr[i][0]}/${arr[i][1]}`)
        .expect((res) => {
          if (res.text.match(/<h3>.+<\/h3>/)[0]
           != `<h3>${arr[i][0]} + ${arr[i][1]} = ${arr[i][0] + arr[i][1]}</h3>`
          ) throw new Error('Incorrect body');
        })
        .expect(200, done);
    });
  }
});
