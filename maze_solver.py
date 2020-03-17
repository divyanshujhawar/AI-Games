#!/usr/local/bin/python3

import sys
import json
import numpy as np

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]


# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
	return 0 <= pos[0] < n  and 0 <= pos[1] < m


# Find the possible moves from position (row, col)
def moves(map, row, col):
	moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

	# Return only moves that are within the board and legal (i.e. on the sidewalk ".")
	return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]


# Calculate the heuristic between current and goal
def heuristic(curr_move,goal_move):
	man_dist = abs(curr_move[0] - goal_move[0]) + abs(curr_move[1] - goal_move[1])
	return man_dist


# To find the direction of next move
def find_direction(curr_move, next_move):

	direction = ""

	if curr_move[0]>next_move[0]:
		direction = "N"
	elif curr_move[0]<next_move[0]:
		direction = "S"
	elif curr_move[1]>next_move[1]:
		direction = "W"
	elif curr_move[1]<next_move[1]:
		direction = "E"
	return direction


# Perform search on the map
def search1(maze_map,status_map):

	# Find my start position
	you_loc=[(row_i,col_i) for col_i in range(len(maze_map[0])) for row_i in range(len(maze_map)) if maze_map[row_i][col_i]=="#"][0]
	
	# Find the goal position
	goal_loc=[(row_i,col_i) for col_i in range(len(maze_map[0])) for row_i in range(len(maze_map)) if maze_map[row_i][col_i]=="@"][0]

	goal_dist = abs(you_loc[0] - goal_loc[0]) + abs(you_loc[1] - goal_loc[1])

	#Fringe -> {location, distance_travelled, manhattan_dist, direction travelled till now}
	fringe=[(you_loc,0,goal_dist,"")]

	while fringe:
		
		# Calculating the priorities, to be popped out
		min_val = fringe[0][1] + fringe[0][2]
		min_idx = 0

		# Priority queue
		for i in range(len(fringe)):
			if (fringe[i][1] + fringe[i][2]) < min_val:
				min_val = fringe[i][1] + fringe[i][2]
				min_idx = i

		# Popping out item with highest priority
		((curr_move), curr_dist, curr_man, curr_dir)=fringe.pop(min_idx)

		# finding new moves in neighborhood
		for move in moves(maze_map, *curr_move):

			# neighbor is target
			if maze_map[move[0]][move[1]]=="@":
				direction = find_direction(curr_move,move)
				return curr_dist+1,curr_dir+direction
			else:
				h = heuristic(move,goal_loc)
				
				if maze_map[move[0]][move[1]] == '.':

					# Checking if the given state is visited or new
					if status_map[move[0]][move[1]] == 0:
						direction = find_direction(curr_move,move)
						next_direction = curr_dir + direction
						fringe.append((move, curr_dist + 1,h,next_direction))
						status_map[move[0]][move[1]] = 1
					
					# For visited states, we will update the status with minimum cost and resp. direction
					else:
						for i in range(len(fringe)):
							if fringe[i][0] ==  move:
								if (fringe[i][1]+fringe[i][2]) > (curr_dist + curr_man):
									
									fringe[i] = (fringe[i][0],curr_dist,curr_man,curr_dir)
								break
	# If no path found
	return maze_map,"Inf"


# Main Function
if __name__ == "__main__":
	maze_map=parse_map(sys.argv[1])
	
	print("Shhhh... quiet while I navigate!")

	# Conversion to a map that can be run on sice servers
	maze = [[maze_map[i][j] for j in range(len(maze_map[0])-1)] for i in range(len(maze_map))]
	
	status_map = [[0 for j in range(len(maze_map[0])-1)] for i in range(len(maze_map))]

	solution, direction = search1(maze,status_map)
	
	print("Here's the solution I found:")
	if direction == "Inf":
		print(direction)
	else:
		print(solution),
		print(direction)
