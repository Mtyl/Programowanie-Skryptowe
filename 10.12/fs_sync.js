const fs = require('fs');

exports.check = (name) => {
  let stats;
  try {
    stats = fs.statSync(name);
  } catch (e) {
    return 'n';
  }
  if (stats.isFile()) {
    return 'f';
  } if (stats.isDirectory()) {
    return 'd';
  }
  return 'e';
};

exports.simpleRead = (name) => fs.readFileSync(name, { encoding: 'utf8', flag: 'r' });
