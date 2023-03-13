#!/usr/bin/node
const process = require('process');
const argvee = process.argv;
const number = parseInt(argvee[2]);
if (number) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
