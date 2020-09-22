#!/usr/bin/node
exports.converter = function (base) {
  function helper (nums) {
    return nums.toString(base);
  }
  return helper;
};
