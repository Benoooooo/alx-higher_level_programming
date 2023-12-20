#!/usr/bin/node
const args = process.argv.slice(2);
const first = parseInt(args[0]);
const sec = parseInt(args[1]);

function add (a, b) {
  if (Number.isInteger(a) && Number.isInteger(b)) {
    return a + b;
  } else {
    return 'NaN';
  }
}
console.log(add(first, sec));
