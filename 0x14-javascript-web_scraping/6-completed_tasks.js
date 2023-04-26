#!/usr/bin/node
/**
 * This script prints the number of tasks
 * completed by user id.
 * first argument is API url
 * Only print users with completed task
 */
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const tasks = {};
    const result = JSON.parse(body);

    result.forEach((task) => {
      if (task.completed === true) {
        const uId = task.userId;
        if (uId in tasks) {
          let num = tasks[uId];
          num += 1;
          tasks[uId] = num;
        } else {
          tasks[uId] = 1;
        }
      }
    });
    console.log(tasks);
  }
});
