#!/usr/bin/node

// class Rectangle that defines a rectangle:
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // instance method that prints the rectangle using the character X
  print () {
    for (let idx = 0; idx < this.height; idx++) {
      console.log('X'.repeat(this.width));
    }
  }

  // instance method that exchanges the width and height of the rectangle
  rotate () {
    const Exchange = this.width;
    this.width = this.height;
    this.height = Exchange;
  }

  // instance method that multiples the width and height of the rectangle * 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};