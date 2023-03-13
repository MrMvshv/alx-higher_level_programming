#!/usr/bin/node
const process = require('process');
const argvee = process.argv;
const number = parseInt(argvee[2]);
if (number) {
  console.log(factoria(number));
} else {
  console.log('1');
}
function factoria (a) {
  if (a === 1) {
    return (1);
  } else {
    return (a * factoria(a - 1));
  }
}
