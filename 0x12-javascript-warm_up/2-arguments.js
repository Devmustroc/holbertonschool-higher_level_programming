#!/usr/bin/node

const Ar_Search = process.argv.length;

if (Ar_Search === 2) {
  console.log('No argument');
} else if (Ar_Search === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
