#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

// Function to count completed tasks by user ID
const countCompletedTasksByUserId = (todos) => {
  const completedTasksByUserId = {};

  // Count completed tasks for each user
  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId;
      completedTasksByUserId[userId] = completedTasksByUserId[userId] + 1 || 1;
    }
  });

  return completedTasksByUserId;
};

// Make a GET request to the API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksByUserId = countCompletedTasksByUserId(todos);

    // Print users with completed tasks
    Object.keys(completedTasksByUserId).forEach((userId) => {
      console.log(`User ${userId} completed ${completedTasksByUserId[userId]} task(s).`);
    });
  }
});
