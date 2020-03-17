#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]


# Count total # of friends on board
def count_friends(board):
    #print(sum([ row.count('F') for row in board ] ))
    return sum([ row.count('F') for row in board ] )


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])


# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
    return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:]


# check if board is a goal state
def is_goal(board):
    
    return count_friends(board) == K 


# To find out the current position available
def row_column_check(board,current_pos):

    board_len = len(board[0])

    return int((current_pos)/board_len),(current_pos)%board_len


# Get list of successors of given board state
def successors(board,current_pos):

    row_check,column_check = row_column_check(board,current_pos)

    while current_pos < map_length:
        #print("Current position: ",current_pos)
        #print("row check: ",row_check)
        #print("column check: ",column_check) 
        #print("\n")

        collision = 0

        if board[row_check][column_check] == '.':

            for r in range(row_check,0,-1):
                if board[r-1][column_check] == '&' or board[r-1][column_check] == '@':
                    break
                if board[r-1][column_check] == 'F':
                    collision += 1
                    break

            for c in range(column_check,0,-1):
                if board[row_check][c-1] == '&' or board[row_check][c-1] == '@':
                    break
                if board[row_check][c-1] == 'F':
                    collision +=1
                    break

            if (collision == 0):
                board[row_check][column_check] = 'F'
                current_pos+=1
                #print(board)
                return board,current_pos

            else:
                current_pos+=1
                row_check,column_check = row_column_check(board,current_pos)
        else:
            current_pos+=1
            row_check,column_check = row_column_check(board,current_pos)

    return board,current_pos
        
    



# Solve n-rooks!
def solve(initial_board):
    current_pos = 0
    fringe = [initial_board]
    map_length = len(maze_map)*len(maze_map[0])

    if current_pos == (map_length):
        return False

    while len(fringe) > 0:
        s,cu_pos = successors(fringe.pop(),current_pos)

        if is_goal(s):
            return(s)
        current_pos = cu_pos
        fringe.append(s)
    return False


# Main Function
if __name__ == "__main__":
    map=parse_map(sys.argv[1])

    maze_map = map[:][:(len(map[0])-1)]

    map_length = len(maze_map)*len(maze_map[0])

    # This is K, the number of friends
    K = int(sys.argv[2])
    
    print ("Starting from initial board:\n" + printable_board(maze_map) + "\n\nLooking for solution...\n")
    solution = solve(maze_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")


