#!/usr/bin/node

exports.converter = function (base) {
  return function (NumberConvert) {
    return NumberConvert.toString(base);
  };
};
