
fs = require('fs');
const regex = /(\d+)-(\d+),(\d+)-(\d+)/g;

function is_superset(a1, a2, b1, b2) {
    return (a1 >= b1 && a2 <= b2) || (a1 <= b1 && a2 >= b2)
}

function does_overlap(a1, a2, b1, b2) {
    return (a1 >= b1 && a1 <= b2) || (a2 >= b1 && a2 <= b2) || is_superset(a1, a2, b1, b2)
}

fs.readFile('4.in', 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    const array_of_matches = [...data.matchAll(regex)];

    let supersets = array_of_matches.filter(x => is_superset(parseInt(x[1]), parseInt(x[2]), parseInt(x[3]), parseInt(x[4])) === true, array_of_matches);
    let overlaps = array_of_matches.filter(x => does_overlap(parseInt(x[1]), parseInt(x[2]), parseInt(x[3]), parseInt(x[4])) === true, array_of_matches);

    console.log(`Number of pairs where one set is included in another: ${supersets.length}`)
    console.log(`Number of pairs where one set overlaps another: ${overlaps.length}`)
  });
