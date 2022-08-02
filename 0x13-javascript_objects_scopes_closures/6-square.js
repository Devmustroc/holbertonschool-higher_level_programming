#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    c = 'X';
    for (let idx = 0; idx < this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
};