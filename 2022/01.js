/**
 * Advent Of Code Day 1
 * Javascript implementation
 * Sum and sort integers lists
 */
const test_data = `
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
`;

fs = require('fs');

/**
 * Solve Day 1 challenge. Solution is sent to stdlog
 * @param {string} data The challenge's input data
 */
function solve(data) {
  let elements = data.trim().split('\n\n');  // Split group of values
  elements = elements.map(e => e.split("\n").map(x => parseInt(x)));  // For each group, convert to integer
  elements = elements.map(x => x.reduce((acc, a) => acc + a, 0));  // Sum over each group
  elements = elements.sort((a, b) => b - a);  // Sort each group

  // Part 1 needs to get the maximum, so first index of the list
  console.log("Part 1: maximum is: ", elements[0])
  // Part 2 needs to sum all top 3
  console.log("Part 2: sum of top 3: ", elements.slice(0, 3).reduce((acc, a) => acc + a, 0))
}

fs.readFile('1.in', 'utf8', function (err, data) {
  if (err) {
    console.log(`Error ${err}: fallback using test data`)
    solve(test_data);
  } else {
    solve(data);
  }
});
