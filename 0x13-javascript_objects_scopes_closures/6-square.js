#!/usr/bin/node
const Rectangle = require('./5-square.js');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c == null) {
      super.print();
    } else {
      let help = 0;
      for (help; help < this.height; help++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
