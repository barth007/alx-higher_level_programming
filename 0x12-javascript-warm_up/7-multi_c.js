#!/usr/bin/node

const args = process.argv;
if (args[2]) {
  const num = parseInt(args[2]);
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
