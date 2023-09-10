# Sudoku Solver

## Playing the Board

As a user, you may enter numbers on the sudoku board. The red square highlights which square you are changing or adding the number to. Correct numbers will be confirmed with a black integer:

![default](./images/default.png)

And incorrect numbers will add an X to the bottom of the interface:

![incorrect](./images/incorrect.png)

Another core feature is that there is also a timer keeping track of the total time spent in the bottom right hand corner.

## Solving the Board

In regards to solving, the entire sudoku board can be solved efficiently within a minute. The following picture is taken during the solving process:

![solving](./images/solving.png)

The solver uses a backtracking algorithm where red 0’s denotes that it is currently backtracking. So, we have the fully solved board:

![complete](./images/complete.png)

In conclusion, it follows that any valid sudoku board can be solved.
