import copy
import heapq
import math
import time
import pygame
from collections import OrderedDict

def draw_maze(screen, maze, block_size):
    # define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255,255,0)
    ORANGE = (255,165,0)

    # draw maze as a grid
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            if maze[i][j] == 1:  # wall
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
            elif maze[i][j] == 'S':  # start
                pygame.draw.rect(screen, YELLOW, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
            elif maze[i][j] == 'G':  # goal
                pygame.draw.rect(screen, GREEN, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
            elif maze[i][j] == 'x':  # traversed
                pygame.draw.rect(screen, GRAY, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
            elif maze[i][j] == '*':  # optimal path
                pygame.draw.rect(screen, ORANGE, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)
            else:  # unexplored
                pygame.draw.rect(screen, BLACK, rect)
                pygame.draw.rect(screen, BLACK, rect, 2)


def print_explored_gui(maze, result):
    # initialize Pygame
    pygame.init()

    # set up screen
    block_size = 40
    width = len(maze[0]) * block_size
    height = len(maze) * block_size
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Solver")

    # initialize clock
    clock = pygame.time.Clock()

    # draw initial maze
    draw_maze(screen, maze, block_size)

    # draw search path
    optimal = result[0]
    traversed = result[1]
    for x in traversed:
        if maze[x[0]][x[1]] != 'S' and maze[x[0]][x[1]] != 'G':
            maze[x[0]][x[1]] = 'x'

        draw_maze(screen, maze, block_size)
        pygame.display.update()
        time.sleep(0.2)

    # draw optimal path
    for x in optimal:
        if maze[x[0]][x[1]] != 'S' and maze[x[0]][x[1]] != 'G':
            maze[x[0]][x[1]] = '*'

        draw_maze(screen, maze, block_size)
        pygame.display.update()
        time.sleep(0.2)

    # wait for user to quit
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

def search(maze, start, goal):
    # initialize frontier, visited set, and cost dictionary
    frontier = []
    visited = OrderedDict()
    cost = {}

    # add start node to the frontier with a priority value of 0
    heapq.heappush(frontier, (0, start))
    cost[start] = (0, None)

    for i in range(len(maze)):
        for j in range(len(maze)):
            if (i, j) != start:
                cost[(i, j)] = (math.inf, None)

    while frontier:
        # get the node with the lowest priority value
        _, current = heapq.heappop(frontier)

        # check if the current node is the goal node
        if current == goal:
            # return the path and visited set
            path = []
            while current in cost:
                path.append(current)
                current = cost[current][1]
            return list(reversed(path)), list(visited)

        # add the current node to the visited set
        visited[current] = None

        # explore the neighbors of the current node
        for neighbor in get_neighbors(maze, current):
            # calculate the tentative actual cost to reach the neighbor node
            tentative_cost = cost[current][0] + 1  # assuming each move has a cost of 1

            if tentative_cost < cost[neighbor][0]:
                # update the actual cost and parent node for the neighbor node
                cost[neighbor] = (tentative_cost, current)
                priority = tentative_cost + heuristic(neighbor, goal)
                # add the neighbor node to the frontier with the priority value
                heapq.heappush(frontier, (priority, neighbor))

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
    # need to change the heuristic calc, this is just manhattan distance, good for small mazes but very bad for
    # bigger mazes
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def read_maze():
    with open('mazes/maze19x19.txt', 'r') as f:
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
    # TODO:
    maze = read_maze()
    copied_maze = copy.deepcopy(maze)  # suboptimal, nawawala kasi yung G at S so bandaid solution
    print(maze)
    print(len(maze))
    for l in maze:
        for item in l:
            print(item, end='')
        print()
    # get start index
    start_index = [(i, j) for i, row in enumerate(maze) for j, val in enumerate(row) if val == 'S']
    # get end index
    end_index = [(i, j) for i, row in enumerate(maze) for j, val in enumerate(row) if val == 'G']
    # replace the characters with 0 after getting indexes
    maze[start_index[0][0]][start_index[0][1]] = 0
    maze[end_index[0][0]][end_index[0][1]] = 0
    # print out the path traveled
    result = search(maze, start_index[0], end_index[0])

    # printing the actual result
    print_explored_gui(copied_maze, result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/