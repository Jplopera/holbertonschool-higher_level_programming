#!/usr/bin/node
const SquareV1 = require('./5-square');

class Square extends SquareV1 {
  charPrint (c = 'X') {
    const char = c;
    for (let i = 0; i < this.width; i++) {
      console.log(char.repeat(this.width));
    }
  }
}
module.exports = Square;
