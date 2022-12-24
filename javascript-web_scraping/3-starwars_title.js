#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (error, response, body) {
  if (error) return console.log('code:', error);
  console.log(JSON.parse(body).title);
});
