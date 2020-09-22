#!/usr/bin/node
exports.esrever = function (list) {
  const rev_help = [];
  list.forEach(elem => {
    rev_help.unshift(elem);
  });
  return rev_help;
};
