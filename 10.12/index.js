const op = require('./module');

const args = process.argv.slice(2);
/** Converting strings to numbers */
const x = new op.Operation(Number(args[0]), Number(args[1]));
/** Printing sum of arguments */
console.log(x.sum());
