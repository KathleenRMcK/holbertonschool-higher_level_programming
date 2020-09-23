#!/usr/bin/node
const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], (err, res, body) => {
  if (err) { return console.log(err); }
  let char_check = JSON.parse(body).characters;
  chars.forEach(url => {
    request(url, (err, res, body) => {
      console.log(JSON.parse(body).title);
    });
  });
});
