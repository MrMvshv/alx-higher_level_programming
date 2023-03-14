#!/usr/bin/node

exports.esrever = function (list) {
  const esre = [];

  for (let i = list.length - 1; i >= 0; i--) {
    esre.push(list[i]);
  }
  return esre;
};
