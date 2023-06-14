#!/usr/bin/node

const args = process.argv;
const firstOperand = parseInt(args[2]);
const secondOperand = parseInt(args[3]);

function add (a, b) {
  const result = a + b;
  return result;
}
const result = add(firstOperand, secondOperand);
console.log(result);
