#!/usr/bin/node
const args = process.argv.slice(2);
const first = parseInt(args[0]);

function factorial (a) {
  if (a === 0) {
    return 1;
  } else if (isNAN) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(first));
