#!/usr/bin/node
// comments check
exports.esrever = function (list) {
  const rev_help = [];
  list.forEach(elem => {
    rev_help.unshift(elem);
  });
  return rev_help;
};
