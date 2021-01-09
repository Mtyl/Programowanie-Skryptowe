const { expect } = require('chai');
const { check, simpleRead } = require('../fs_sync');

const path = '/home/balhaim/Dokumenty/skrypty/10.12/cwiczenie4/';
describe('The check() function', () => {
  it('Finds existing files', () => {
    expect(check(`${path}index.js`)).to.equal('f');
    expect(check(`${path}index.mjs`)).to.equal('f');
    expect(check(`${path}test/test.js`)).to.equal('f');
    expect(check(`${path}test/test_sync.js`)).to.equal('f');
  });
  it('Finds existing directories', () => {
    expect(check(`${path}`)).to.equal('d');
    expect(check(`${path}out`)).to.equal('d');
    expect(check(`${path}out/fonts`)).to.equal('d');
    expect(check(`${path}test`)).to.equal('d');
  });
  it('Returns false for non-existing files', () => {
    expect(check(`${path}inex.js`)).to.equal('n');
    expect(check(`${path}idex.mjs`)).to.equal('n');
    expect(check(`${path}test/tst.js`)).to.equal('n');
    expect(check(`${path}tet/test_sync.mjs`)).to.equal('n');
  });
  it('Read file', () => {
    expect(simpleRead(`${path}mocha`)).to.equal('node ./node_modules/mocha/bin/mocha test/$1');
  });
});
