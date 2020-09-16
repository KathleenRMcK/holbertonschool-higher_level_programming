#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  const total = parseInt(process.argv[2])
  for (let helper = 0; helper < total; helper++) {
    console.log('X'.repeat(total));
  }
}
