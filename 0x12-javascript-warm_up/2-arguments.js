#!/usr/bin/node
const process = require('process');
const argvee = process.argv;

const size = argvee.length;
if (size === 2) {
  console.log('No argument');
} else if (size === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
