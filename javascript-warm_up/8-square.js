#!/usr/bin/node
if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
} else {
  for (let y = 0; y < process.argv[2]; y++) {
    console.log('y'.repeat(process.argv[2]));
  }
}
