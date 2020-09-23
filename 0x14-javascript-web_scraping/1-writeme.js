#!/usr/bin/node
let filesystems = require('fs');

filesystems.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) console.log(err);
});
