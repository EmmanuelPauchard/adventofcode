// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

int main () {
  string line;
  ifstream myfile ("1/input.txt");
//   vector<vector<int>> elements;
  vector<int> elements;

  if (myfile.is_open())
  {
    // vector<int> current_line;
    int current_sum = 0;
    while ( getline (myfile,line) )
    {
        if (line.length() == 0) {
            // elements.push_back(current_line);
            elements.push_back(current_sum);
            current_sum = 0;
        }
        else {
            // // Store each number individually
            // current_line.push_back(stoi(line));
            // accumulate all lines
            current_sum += stoi(line);
        }
    }
    // if (current_line.size())
    //     elements.push_back(current_line);
    if (current_sum)
        elements.push_back(current_sum);

    myfile.close();
  }
  else cout << "Unable to open file";

// for (auto & w: elements) {
//     for (auto & c: w) {
//         cout << c << "\r\n";
//     }
//     cout <<"\r\n";
// }
  cout << "Found " << elements.size() << "\r\n";

  std::sort (elements.begin(), elements.end());

  cout << "Top 3: " << endl;
  for_each (elements.rbegin(), elements.rbegin()+3, [](const int n){cout << n << endl;});

  return 0;
}