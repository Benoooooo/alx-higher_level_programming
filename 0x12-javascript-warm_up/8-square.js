#!/usr/bin/node
const args = process.argv.slice(2);
const size = args[0];

let index = 0;
let index1 = 0;
if (Number.isInteger(parseInt(size))) {
  while (index < size) {
    while (index1 < size) {
      console.log('X');
      index1++;
    }
    index++;
  }
} else {
  console.log('Missing size');
}
