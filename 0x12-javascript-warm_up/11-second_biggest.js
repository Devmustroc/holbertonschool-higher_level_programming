#!/usr/bin/node

let bigg = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  bigg = args[args.length - 2];
}
console.log(bigg);
