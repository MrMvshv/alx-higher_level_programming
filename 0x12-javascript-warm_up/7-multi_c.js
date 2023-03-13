#!/usr/bin/node
const process = require('process');
const argvee = process.argv;
const number = parseInt(argvee[2]);
if (number) {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
