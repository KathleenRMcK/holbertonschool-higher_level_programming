#!/usr/bin/node
const request = require('request');

request(process.argv[2], (err, res, body) => {
  if (err) { return console.log(err); }
  let holder = {};
  JSON.parse(body).forEach(item => {
    if (item.completed) {
        holder[item.userId] ? holder[item.userId] += 1 : holder[item.userId] = 1;
    }
  });
  console.log(holder);
});
