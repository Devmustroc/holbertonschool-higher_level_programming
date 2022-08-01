#!/usr/bin/node

const Numbers = process.argv.length;
const numTest = process.argv.slice(2);
if (Numbers < 4) {
  console.log(0);
} else {
  const CheckTest = numTest.sort((a, b) => b - a);
  console.log(CheckTest[1]);
}
