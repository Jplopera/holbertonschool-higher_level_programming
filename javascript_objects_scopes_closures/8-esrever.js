#!/usr/bin/node
exports.esrever = function (list) {
  let c = list.length - 1;
  const array = [];
  while (c >= 0) {
    array.push(list[c]);
    c--;
  }
  return (array);
};
