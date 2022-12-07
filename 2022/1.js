console.log("Hello")
fs = require('fs');
fs.readFile('/mnt/c/epauchard/projects/adventofcode/2022/1/input.txt', 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    // console.log(data);
    let elements = data.split('\n\n');
    elements = elements.map(e => e.split("\n").map(x => parseInt(x)));
    elements = elements.map(x => x.reduce((partialSum, a) => partialSum + a, 0));
    elements = elements.sort((a, b) => b - a);

    console.log(elements.slice(0, 3))
  });
