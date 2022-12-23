#!/usr/bin/node
if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
} else {
  for (let x = 0; x < process.argv[2]; x++) {
    console.log('x'.repeat(process.argv[2]));
  }
}
