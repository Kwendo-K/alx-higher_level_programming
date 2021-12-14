#!/usr/bin/node
const y = Math.floor(Number(process.argv[2]));
if (isNaN(y)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < y; i++) {
    console.log('C is fun');
  }
}
