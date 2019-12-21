from ex8_helper import *


def get_row_variations(row, blocks):
    options = list()
    for i in range(len(row)):  # check if block +index > len
        row_variations_helper(row, i, blocks[0], options)
    return options


def row_variations_helper(row, index, block, options):
    if block == 0:
        options.append(row[:])
        return
    elif index >= len(row):
        return
    elif row[index] == -1:
        row[index] = 1
        row_variations_helper(row, index + 1, block-1, options)
        row[index] = -1
    elif row[index] == 0 or row[index] == 1:
        return
    return options


rw = [-1, -1, -1, -1]
blcks = [1]
print_board([[-1, -1, -1, -1], [-1, -1, -1, -1]])
print(get_row_variations(rw, blcks))

