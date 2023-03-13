#!/usr/bin/node
const process = require('process');
const argvee = process.argv;

if (argvee[2]) {
  console.log(argvee[2]);
} else {
  console.log('No argument');
}
