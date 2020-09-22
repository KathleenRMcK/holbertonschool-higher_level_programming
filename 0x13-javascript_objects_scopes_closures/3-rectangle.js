#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w = null, h = null) {
    if (w <= 0 || h <= 0) {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let help = 0;
    for (help; help < this.height; help++) {
        console.log('X'.repeat(this.width));
    }
  }
};
