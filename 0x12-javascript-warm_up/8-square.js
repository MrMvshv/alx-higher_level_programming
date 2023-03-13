#!/usr/bin/node
const process = require('process');
const argvee = process.argv;
const number = parseInt(argvee[2]);
if (number) {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
