#!/usr/bin/node

module.exports = class Rectangle {};

const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);
