#!/usr/bin/node

const fs = require('fs');
const wr = process.argv[3];
fs.writeFile(process.argv[2], wr, 'utf-8', function (err, wr) {
  if (err) {
    console.log(err);
  }
});
