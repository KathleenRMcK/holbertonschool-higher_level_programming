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
};
