#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w && h !== 0) && (w && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.width));
    }
  }
};
