#!/usr/bin/node

const arSearch = process.argv.length;

if (arSearch === 2) {
  console.log('No argument');
} else if (arSearch === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
