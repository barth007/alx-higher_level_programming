#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c = 'X') {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double (num = 2) {
    this.width *= num;
    this.height *= num;
  }
};
