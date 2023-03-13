#!/usr/bin/node
const process = require('process');
const argvee = process.argv;

const size = argvee.length;
if (size === 2) {
  console.log('No argument');
} else if (size === 3) {
  console.log('Argument found');
  console.log(argvee[2]);
} else {
  console.log('Arguments found');
  for (let i = 2; i < size; i++) {
    console.log(argvee[i]);
  }
}
