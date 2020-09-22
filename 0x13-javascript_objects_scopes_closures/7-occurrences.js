#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let help = 0;
  list.forEach(num => {
    if (num === searchElement) {
      help++;
    }
  });
  return help;
};
