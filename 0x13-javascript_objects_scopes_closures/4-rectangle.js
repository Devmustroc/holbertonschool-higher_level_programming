#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const myvar = this.width;
    this.width = this.height;
    this.height = myvar;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
