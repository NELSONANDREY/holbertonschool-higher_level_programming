#!/usr/bin/node

const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', function (err, contents) {
  if (!err) {
    console.log(contents);
  } else {
    console.log(err);
  }
});
