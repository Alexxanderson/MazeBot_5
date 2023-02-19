# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def read_maze():
    with open('maze.txt', 'r') as f:
        maze_size = f.readline()
        contents = f.read()

    return contents


# actual main
def main():
    # Use a breakpoint in the code line below to debug your script.

    # TODO:
    maze = read_maze()

    print(maze)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
