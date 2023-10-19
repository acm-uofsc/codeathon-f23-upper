# <Problem Name>

## Problem Statement

Treasure hunters have ventured into a mysterious underground labyrinth searching for a fabled relic hidden in the heart of the maze. The labyrinth consists of m x n chambers arranged in a 2D grid. Our intrepid explorer starts from the top-left chamber and must navigate through the labyrinth to retrieve the relic. The heart of the maze that contains the relic is, of course, the bottom-right chamber furthest from the explorer.

The explorer begins the journey with an initial stamina level represented by a positive integer. If, at any point, their stamina drops to 0 or below, they perish in the labyrinth.

Some chambers are guarded by dangerous creatures (represented by negative integers), causing the explorer to lose stamina when entering such chambers. Others are unoccupied (represented as 0) or contain enchanted crystals that boost the explorer's stamina (represented by positive integers).

To retrieve the relic as swiftly as possible, the explorer chooses to move exclusively in rightward or downward directions during each step.

Determine the minimum initial stamina level the explorer needs to successfully recover the relic from the heart of the labyrinth.

Note that any room can contain threats or power-ups, even the first room the hunter enters and the bottom-right room where the princess is imprisoned.

## Input Format

m n
m lines follow with n integers space-delimited

## Constraints

m == number of rows
n == number of columns
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000

## Output Format

A number X representing the minimum health needed for the explorer to make it to the relic

# Instructions for Problem Writers

Replace all filler with your own information. This is what will go in HackerRank.

Modify mkin.py to print the problem input to the console.

Run genSamples.sh to only generate the inputs for the sample cases. You may want special checks on test number if you want to generate a certain number of very large tests. 

Run runSampleInput.sh to generate sample outputs using your **correct** solution (solutions/sol.py). Make sure these are valid.

Run testgen.sh to generate the remaining test cases. Modify this if you need more/fewer test cases. The cases.zip file is what will be uploaded to HackerRank. 

# Acknowledgements

Special thanks to Colter Boudinot (@Goldenlion5648) for putting together this template.