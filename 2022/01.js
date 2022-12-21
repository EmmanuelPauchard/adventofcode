fs = require('fs');
fs.readFile('2022/1.in', 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    let elements = data.split('\n\n');
    elements = elements.map(e => e.split("\n").map(x => parseInt(x)));
    elements = elements.map(x => x.reduce((partialSum, a) => partialSum + a, 0));
    elements = elements.sort((a, b) => b - a);

    console.log(elements.slice(0, 3))
  });
