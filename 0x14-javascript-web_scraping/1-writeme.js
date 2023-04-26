#!/usr/bin/node
/**
 * This script writes a string to a file
 * File path is the first argument
 * String to write is second argument
 * If error occurs, print error object
 */
const fs = require('fs');
const fileName = process.argv[2];
const str = process.argv[3];

fs.writeFile(fileName, str, { encoding: 'utf-8' }, (err) => {
  if (err) {
    console.error(err);
  }
});
