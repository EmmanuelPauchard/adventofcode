/**
 * Challenge Day 4: overlapping sets of integers
 */

const test_data = `
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
`;

fs = require('fs');

/**
 * Check if range [a1,a2] is a superset (ie: a set that totally includes) range [b1,b2]
 * @param {int} a1 Lower bound of the first range
 * @param {int} a2 Upper bound of the first range
 * @param {int} b1 Lower bound of the second range
 * @param {int} b2 Upper bound of the second range
 * @returns {boolean} True if interval a is a superset of interval b
 */
function is_superset(a1, a2, b1, b2) {
  // Return true
  return (a1 >= b1 && a2 <= b2) || (a1 <= b1 && a2 >= b2)
}

/**
 * Check if range [a1,a2] overlaps (ie: has a non empty intersection with) range [b1,b2]
 * @param {int} a1 Lower bound of the first range
 * @param {int} a2 Upper bound of the first range
 * @param {int} b1 Lower bound of the second range
 * @param {int} b2 Upper bound of the second range
 * @returns {boolean} True if interval a overlaps interval b
 */
function does_overlap(a1, a2, b1, b2) {
  return (a1 >= b1 && a1 <= b2) || (a2 >= b1 && a2 <= b2) || is_superset(a1, a2, b1, b2)
}

/**
 * Solve Day 4 challenge. Solution is sent to stdlog
 * @param {string} data The challenge's input data
 */
function solve(data) {
  const regex = /(\d+)-(\d+),(\d+)-(\d+)/g;
  const array_of_matches = [...data.matchAll(regex)];

  let supersets = array_of_matches.filter(x => is_superset(parseInt(x[1]), parseInt(x[2]), parseInt(x[3]), parseInt(x[4])) === true, array_of_matches);
  let overlaps = array_of_matches.filter(x => does_overlap(parseInt(x[1]), parseInt(x[2]), parseInt(x[3]), parseInt(x[4])) === true, array_of_matches);

  console.log(`Number of pairs where one set is included in another: ${supersets.length}`)
  console.log(`Number of pairs where one set overlaps another: ${overlaps.length}`)
}

fs.readFile('4.in', 'utf8', function (err, data) {
  if (err) {
    console.log(`Error ${err}: fallback using test data`)
    solve(test_data);
  } else {
    solve(data);
  }
});
