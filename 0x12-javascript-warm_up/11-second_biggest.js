#!/usr/bin/node
const process = require('process');
const argvee = process.argv;
size = argvee.length;
if (size <= 3) {
  console.log('0');
} else {
  let toppa = argvee[2];
  let secs = argvee[2];
  for (let i = 3; i < size; i++) {
    if (argvee[i] > toppa) {
      secs = toppa;
      toppa = argvee[i];
    } else if (argvee[i] > secs && argvee[i] != toppa) {
      secs = argvee[i];
    }
  }
  console.log(secs);
}
