#!/usr/bin/node
/**
 * This script reads and prints content of a file
 * File path is the first argument
 * If error occurs, print error object
 */
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
