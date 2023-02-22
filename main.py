import heapq

prev_value = 0
count = 1

def greedy_best_first_search(maze, start, goal):
    # initialize frontier and visited set
    global prev_value, count
    frontier = []
    visited = set()

    # add start node to the frontier with a heuristic priority value of 0
    heapq.heappush(frontier, (0, [start]))

    while frontier:
        # get the node with the lowest heuristic priority value
        _, path = heapq.heappop(frontier)
        current = path[-1]

        # check if the current node is the goal node
        if current == goal:
            return path, visited

        # add the current node to the visited set
        visited.add(current)
        print(current)
        count+=1
        prev_value = heuristic(current,goal)

        # explore the neighbors of the current node
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                # calculate the heuristic priority value for the neighbor node
                priority = heuristic(neighbor, goal)
                # add the neighbor node to the frontier with the priority value
                heapq.heappush(frontier, (priority, path + [neighbor]))




    # if the frontier is empty and the goal node has not been found, return None
    return None, visited

def get_neighbors(maze, node):
    # get the row and column of the current node
    row, col = node

    # define the possible moves from the current node
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # check each possible move and add valid neighbors to the list
    neighbors = []
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] == 0:
            neighbors.append((new_row, new_col))

    return neighbors

def heuristic(node, goal):
    # need to change the heuristic calc, this is just manhattan distance, good for small mazes but very bad for bigger mazes
    return prev_value+abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def read_maze():
    with open('mazes/maze8x8.txt', 'r') as f:
        maze_size = int(f.readline())
        squares = [[0 for j in range(maze_size)] for i in range(maze_size)]
        for i in range(maze_size):
            string = f.readline()
            for j in range(maze_size):
                if string[j] == ".":
                    squares[i][j] = 0
                elif string[j] == "#":
                    squares[i][j] = 1
                else:
                    squares[i][j] = string[j]

    return squares


# actual main
def main():
    # Use a breakpoint in the code line below to debug your script.

    # TODO:
    maze = read_maze()
    print(maze)
    print(len(maze))
    for l in maze:
        for item in l:
            print(item, end='')
        print()
    #get start index
    start_index = [(i,j) for i, row in enumerate(maze) for j, val in enumerate(row) if val == 'S']
    # get end index
    end_index = [(i,j) for i, row in enumerate(maze) for j, val in enumerate(row) if val == 'G']
    # replace the characters with 0 after getting indexes
    maze[start_index[0][0]][start_index[0][1]] = 0
    maze[end_index[0][0]][end_index[0][1]] = 0
    #print out the path traveled
    print(greedy_best_first_search(maze, start_index[0], end_index[0]), count)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

