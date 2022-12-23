#!/usr/bin/node
if (isNaN(process.argv[2]) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let y = 0; y < parseInt(process.argv[2]); y++) {
    console.log('C is fun');
  }
}
