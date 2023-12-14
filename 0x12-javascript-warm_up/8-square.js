#!/usr/bin/node
const args = process.argv.slice(2);
const size = args[0];

let index = 0;
let index1 = 0;
let row;
if (Number.isInteger(parseInt(size))) {
  for (index = 0; index < size; index++) {
    row = '';
    for (index1 = 0; index1 < size; index1++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
