#!/usr/bin/node
const args = process.argv.slice(2);

const x = args[0];

const le = 'C is fun';

let index = 0;
if (Number.isInteger(parseInt(x))) {
  while (index < x.length) {
    console.log(le[index]);
    index++;
  }
} else {
  console.log("Missing number of occurrences");
}
