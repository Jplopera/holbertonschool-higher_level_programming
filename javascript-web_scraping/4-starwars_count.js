#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  let results;
  if (error) {
    console.log(error);
  } else {
    results = JSON.parse(body).results;
  }
  let chid = 0;
  for (let x = 0; x < results.length; x++) {
    for (let y = 0; y < results[x].characters.length; y++) {
      if (results[x].characters[y].includes('18')) {
        chid++;
      }
    }
  }
  console.log(chid);
});
