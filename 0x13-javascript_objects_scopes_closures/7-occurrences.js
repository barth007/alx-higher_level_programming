#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter((lists) => lists === searchElement).length;
};
