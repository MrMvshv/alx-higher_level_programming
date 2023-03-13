#!/usr/bin/node
const process = require('process');
const argvee = process.argv;
function add (a, b) {
  return (a + b);
}
console.log(add(parseInt(argvee[2]), parseInt(argvee[3])));
