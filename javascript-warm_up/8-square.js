#!/usr/bin/node
if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
} else {
  for (let X = 0; X < process.argv[2]; X++) {
    console.log('X'.repeat(process.argv[2]));
  }
}
