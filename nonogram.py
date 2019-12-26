from ex8_helper import *


def get_row_variations(row, blocks):
    options = list()
    colored_squares = 0
    final_coloured_squares = 0
    copy_of_row = row[:]  # creating a copy of the row so that the original
    # won't be changed
# if all the blocks that need to be filled are filled, then we have nothing
# to do but to return the row as the only option (with 0 instead of 1)'
    if not blocks and not row:
        return [[]]
    if not blocks:
        for num in row:
            options.append(0)
    for square in row:
        if square == 1:
            colored_squares += square
    for block in blocks:
        final_coloured_squares += block
    if colored_squares == final_coloured_squares:
        return complete_variations([copy_of_row]) # the function changes the input
    # so I

    for i in range(len(row)):  # check if block + index > len

        if i == 0 or row[i-1] != 1:
            # if the previous block is filled,
            # if we run the function it will give wrong variation, because the
            #  variation will have extra filled block.
            #  but it also means we already checked that variation during the
            # previous as we increase the index in the recursion
            row_variations_helper(copy_of_row, i, blocks, 0, blocks[0], options)
    return complete_variations(options)


def row_variations_helper(row, index, blocks, num_of_block, block_size
                          , variations):
    if block_size == 0:
        if index >= len(row) or row[index] != 1:
            # if the index is out of range then we got to the end of the row,
            # and this is a good option *for this current block*
            # or in a case when the block fits the row fully,but the next
            # square is full as well means we can't color the squares this way
            # now we need to check if the next block fits as well so
            # we run the function again but with the next block
            row_variations_next_block(row, index, blocks, num_of_block,
                                      variations)
        return
    elif index >= len(row):
        return  # the index is out of range and the block could not be inserted
    # means it's an invalid variation
    # the recursion step:
    elif row[index] == -1:  # if
        row[index] = 1
        row_variations_helper(row, index + 1, blocks, num_of_block,
                              block_size - 1, variations)
        row[index] = -1  # at this point after the previous line of code
        # was executed, the option was either entered or not, in both cases the
        # function continues searching for the next variation
    elif row[index] == 1:
        # if the block is filled we continues as if we filled it
        row_variations_helper(row, index + 1, blocks,
                              num_of_block, block_size - 1, variations)
    elif row[index] == 0:
        return
    return variations


def row_variations_next_block(row, index, blocks, num_of_block, variations):
    filled = 0
    supposed_to_be_filled = 0
    for num in row:
        if num == 1:
            filled += 1
    for block in blocks:
        supposed_to_be_filled += block
    if num_of_block >= len(blocks) - 1:
        # means we successfully checked the last block and we could fit it
        # in the row, so the current variation is valid
        if not filled > supposed_to_be_filled:
            variations.append(row[:])
        # send a shallow copy of the row because we
        # return the old values to continue checking
    elif not index >= len(row):
        for i in range(len(row) - index):
            index += 1
            row_variations_helper(row, index, blocks, num_of_block + 1,
                                  blocks[num_of_block + 1], variations)
        # run the helper again but with the current row, which is a valid
        # variation of the previous block, with index +1 because we can't
        # color blocks one after another and with num of block +1 to find
        # a variation with the next one.
    return


def complete_variations(variations):
    new_variations = []
    if variations and type(variations[0]) == list:
        for variation in variations:
            updated_variation = []
            for i in range(len(variation)):
                if variation[i] == -1:
                    updated_variation.append(0)
                else:
                    updated_variation.append(variation[i])
            new_variations.append(updated_variation)
    elif len(variations):

        for i in range(len(variations)):
            if variations[i] == -1:
                new_variations.append(0)
            else:
                new_variations.append(variations[i])
    else:
        return []

    return new_variations


def get_intersection_row(rows):
    if len(rows) == 0 or len([rows[0]]) == 0:
        return []
    return get_intersection_row_helper(rows, 0)


def get_intersection_row_helper(rows, index):
    if index + 1 >= len(rows):
        # if we got to the last list in the rows we return the list
        return rows[index].copy()
    ultimate_list = get_intersection_row_helper(rows, index + 1)
    for i in range(len(rows[index])):  # goes over the lists and if the the elements
        # are not the same replace with -1
        if ultimate_list[i] != rows[index][i]:
            ultimate_list[i] = - 1
    return ultimate_list


def conclude_from_constraints(board, constraints):
    if len(board) == 0:
        board = [board]  # otherwise the function sends an int to the
        # other functions
    if not constraints or not constraints[0]:
        return
    for i in range(len(board)):  # going over the rows in the board
        options = get_row_variations(board[i], constraints[0][i])
        board[i] = get_intersection_row(options)


def solve_easy_nonogram():
    pass


row = [[-1, -1, 1, -1, -1], [-1, -1, -1, -1, -1], [-1, -1, -1, -1, -1]]


blocks = [[[1, 2], [1, 2], [2]], [[4], [1], [1], [1, 3], [2]]]





# options = get_row_variations(row[0], blocks[0])
# print(options)
# print(get_intersection_row(options))
conclude_from_constraints(row, blocks)
print(row)
# print(get_intersection_row([[]]))




