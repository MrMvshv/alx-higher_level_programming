#!/usr/bin/node
/**
 * This script displays status code of a request
 * URL is the first argument
 * printed like this: code: <status code>
 * sends a GET request
 */
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
