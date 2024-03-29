#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tem = this.width;
    this.width = this.height;
    this.height = tem;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
