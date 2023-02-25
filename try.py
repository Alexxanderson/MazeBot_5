def print_explored(maze,result):
    print("Optimal Path: ")
    optimal = result[0]
    traversed = result[1]
    # for x in traversed:
    #     if maze[x[0]][x[1]] != 'S' and maze[x[0]][x[1]] != 'G':
    #         maze[x[0]][x[1]] = 'x'

    for x in optimal:
        if maze[x[0]][x[1]] != 'S' and maze[x[0]][x[1]] != 'G':
            maze[x[0]][x[1]] = '*'

    for l in maze:
        for item in l:
            print(item, end='')
        print()

def read_maze():
    with open('maze.txt', 'r') as f:
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

def main():
    print('it works')
    result = ([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)], {(0, 1), (1, 3), (4, 0), (1, 2), (2, 1), (0, 0), (4, 3), (0, 3), (2, 0), (4, 2), (3, 0), (1, 4), (2, 2), (1, 0), (4, 1)})
    print(result)
    print("optimal path ", result[0])
    print("explored path ", result[1])

    maze = read_maze()


    #prints the maze in ln
    print()
    print(maze)
    print(len(maze))
    print()

    # for actual printing of maze
    for l in maze:
        for item in l:
            print(item, end='')
        print()

    print()

    print_explored(maze,result)





main()
