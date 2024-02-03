#!/usr/bin/node
const fs = require('fs');
function writeFile (filePath) {
  fs.writeFile(filePath,contentt, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}
if (process.argv.length < 3) {
  console.log('please provide the file path as an argument');
} else {
  const filePath = process.argv[2];
  writeFile(filePath);
}
