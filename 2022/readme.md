# Advent Of Code 2022

This is the first year I will try to complete the Advent Of Code challenges and publish my solutions.

# Repo Organization
- Days 1 to 8 were really straightforward so they are grouped (except for Day 7) in a [common](https://github.com/EmmanuelPauchard/adventofcode/blob/master/2022/01_2_3_4_5_6_8.ipynb) Jupyter notebook
- Day 7 is relatively simple but I wanted to test some new techniques so I kept it apart
- Some challenges have different implementations (Python, C++, Javascript) but the majority of them is written in Python

# Tools
At the beginning of the month, when challenges are quite easy, I played with some new languages and tools:
- ipython notebook: as a quick and efficient way to code, comment and debug
- javascript and C++, just as a refresher

Then from Day 12 when things start to get more difficult I switched back to Emacs, which I had left for vscode for a few years. This kind of game is perfect to re-learn all emacs keybindings, and using emacs is also convenient for the challenges because it allows real fast editing. Also, I find it quicker to perform code/test loops in emacs than in vscode.

# Help
My goal was to complete all challenges by myself but I have to admit that after Day 12, I realized the time it took me to solve each challenge was becoming incompatible with my other activities! So I allowed myself to look at other's solutions when I was blocked. In particular, here are the challenges on which I was stuck and looked for some help, while always providing my own implementation of the solution:
- [Day 11, part 2](https://github.com/EmmanuelPauchard/adventofcode/blob/master/2022/11.ipynb)
- [Day 15, part 2](https://github.com/EmmanuelPauchard/adventofcode/blob/master/2022/15_p2.py)

# Notes

The following is a list of what I've learned or improved thanks to AoC this year:
- **Javascript**: run with node.js for Day [1](https://github.com/EmmanuelPauchard/adventofcode/blob/master/2022/01.js) and [4](https://github.com/EmmanuelPauchard/adventofcode/blob/master/2022/04.js) challenges
- **Python list handling**. I was already used to it but this is the one tool I use the most for these challenges
- **Functional Programming Basics**: [Day 2, Day 3](https://github.com/EmmanuelPauchard/adventofcode/blob/master/2022/01_2_3_4_5_6_8.ipynb) I had fun with Python's `zip`, `map`, `starmap` with a clean separation between data and functions. This gives a very short and, I think, elegant solution although it is harder to read and to debug.
- The [visitor](https://en.wikipedia.org/wiki/Visitor_pattern) design pattern for [Day 7](https://github.com/EmmanuelPauchard/adventofcode/blob/master/2022/07.ipynb), for which I went a bit over the top: I tried to implement a whole filesystem hierarchy, which was a very interesting exercise and where this pattern proved useful.
- **numpy**: I only had the basics of numpy, and from Day 8 I started using it as the base data structure. Since then, I've improved my indexing skills which really makes working with numpy so fun and efficient. For instance, have a look at [Day 15, Part 2](https://github.com/EmmanuelPauchard/adventofcode/blob/master/2022/15_p2.py) for an example of working with vectors.