#!/usr/bin/node
const args = process.argv;
if (args.length === 2) {
  console.log('Not a number');
} else if (parseInt(args[2])) {
  console.log('My number:' + ' ' + parseInt(args[2]));
} else {
  console.log('Not a number');
}
