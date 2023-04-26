#!/usr/bin/node
/**
 * This script gets content of a webpage
 * and stores it in a file utf-8 encoded
 * first argument is url to request
 * second argument is file path to store response
 */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
