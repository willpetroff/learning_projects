"""
This script creates a "Mario" pyramid with the user setting the number of rows
"""


def create_pyramids(rows):
    spaces = rows - 1  # Sets number of spaces equal to the length of the bottom row less one
    bricks = 1
    while bricks <= rows:
        print(" " * spaces + "#" * bricks + " " + "#" * bricks)
        spaces -= 1  # Decrements number of spaces needed
        bricks += 1  # Increments number of bricks used


def main():
    number_rows = int(input('Please enter pyramid height: '))
    create_pyramids(number_rows)


if __name__ == '__main__':
    main()
