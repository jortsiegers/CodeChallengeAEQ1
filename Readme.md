
## Introduction

Hey team, welcome to the first sprint coding challenge! In this challenge, you guys, will use your coding skills to fold a virtual piece of paper 8 times over its x and y axis.

Think of this as coding origami, where instead of using your hands, you'll be using your brain and your keyboard to fold the virtual paper. You will be given a starting point, it's a file named input.txt and your job is to fold it in a way that by the end of the 8th fold, the virtual paper will take a specific shape as described in the output file named output.txt.

But be warned, this is not as easy as it seems. You see, when you fold a piece of paper, it gets smaller and smaller each time. And with each fold, the number of potential crease lines increases exponentially. So, by the time you reach the 8th fold, the number of potential crease lines is a whopping 40,320!

But don't worry, that's where your coding skills come in. You will need to write a program that can navigate through all of those crease lines and make the final fold in the right spot. It's like a game of "Where's Waldo", but with paper folding.

## Breakdown
Here's a breakdown of the program:

- You will have to Implement the fold_x and fold_y functions. (These are the only functions you will have to write)
- The read_input function reads the contents of a file named input.txt and stores it in the data attribute of the class.
- The data attribute is then passed to the fold_x function, which is responsible for folding the virtual piece of paper along the x-axis.
- The result of the fold_x function is then passed to the fold_y function, which is responsible for folding the virtual piece of paper along the y-axis.
- This process of alternating between the fold_x and fold_y functions is repeated 8 times in total, with the final result being written to a file named output.txt using the output_data function.
- Develop the logic for the folding process, that takes the input and transform it to the output described by the output file.

## Example

```
Implement the fold_x and fold_y functions. On fold_x if the following list is provided is has to return the following result:
input = [
    [' ', 'x', 'y', ' '],
    [' ', ' ', 'y', ' '],
    ['x', ' ', ' ', ' '],
    [' ', ' ', ' ', 'y'],
]

output = [
    ['x', 'x', 'y', 'y'],
    [' ', ' ', 'y', ' '],
]

```

## GOODLUCK!!!