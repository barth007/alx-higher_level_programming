#!/usr/bin/node

const args = process.argv;
if (args[2]) {
  if (parseInt(args[2])) {
    const square = parseInt(args[2]);
    for (let i = 0; i < square; i++) {
      console.log('X'.repeat(square));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
