#!/usr/bin/node
exports.logMe = function (item) {
  if (!exports.logMe.counter) {
    exports.logMe.counter = 0;
  }
  exports.logMe.counter++;
  console.log(exports.logMe.counter - 1 + ':', item);
};
