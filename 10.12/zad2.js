const { check, simpleRead } = require('./fs_sync');

const type = check(process.argv[2]);
switch (type) {
  case 'n':
    console.log('No such file or directory!');
    break;
  case 'f':
    console.log('File exists!\n');
    console.log(simpleRead(process.argv[2]));
    break;
  case 'd':
    console.log('Directory exists!');
    break;
  default:
    console.log('Unexpected error!');
    break;
}
