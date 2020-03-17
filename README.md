# AI-Games

This repo collects my work on Artificial Intelligent games, it includes various different search, extraction and ML algorithms. All the codes are written in Python3.

1. Maze Solver: This part represents application to A-Star algorithm to solve the maze.

2. Hide n Seek: Similar to maze solver with a little change. Also, A-star implementation.

3. Tile Sliding: This is problem is same as https://en.wikipedia.org/wiki/15_puzzle, where the task to sort the letter by sliding tile. 
  This part represents the implmentation of A* and IDA* search algorithm. Here, we had to solve it with 3 different challenges: Simply each problem had it's own move type.
  * (a) Original move: which the standard problem have, that it can move {up,down,left,right}
  * (b) Circular move: in addition to moves of original move, it can also move circular. Like from top row it can directly move to the alst   row.
  * (c) L move: this is similar to "knight move" in chess and no other moves are allowed.
  
4. 2048 AI tile game: This part is very much similar to 2048 game https://en.wikipedia.org/wiki/2048_(video_game), just that it wass converted to 2 player game. So, there are 3 possibility Human-Human, Human-AI and AI-AI. Mini-Max algorithm with alpha-beta pruning was used. And we have tested it with 7 different heuristic functions.

5. Code Breaking: This part the idea is to decrypt a code without any key. I have used Metropolis Hastings algorithm for this part, and using that the code was clearly decrypting the given encoded string. Different patterns in determining keys were used, with multiple run to get the accurate result.
