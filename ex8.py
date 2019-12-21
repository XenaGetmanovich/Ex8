from ex8_helper import *


def get_row_variations(row, blocks):
    options = list()
    for i in range(len(row)):  # check if block + index > len
        if i == 0 or row[i-1] != 1:
            # if the previous block is filled,
            # if we run the function it will give wrong variation, because the
            #  variation will have extra filled block.
            #  but it also means we already checked that variation during the
            # previous as we increase the index in the recursion
            row_variations_helper(row, i, blocks, 0, blocks[0], options)
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
    if num_of_block >= len(blocks) - 1:
        # means we successfully checked the last block and we could fit it
        # in the row, so the current variation is valid
        variations.append(row[:])  # send a shallow copy of the row because we
        # return the old values to continue checking
    elif not index >= len(row):
        if row[index] == -1:
            row[index] = 0
        row_variations_helper(row, index + 1, blocks, num_of_block + 1,
                              blocks[num_of_block + 1], variations)
        # run the helper again but with the current row, which is a valid
        # variation of the previous block, with index +1 because we can't
        # color blocks one after another and with num of block +1 to find
        # a variation with the next one.
    return


def complete_variations(variations):
    if variations:
        for variation in variations:
            for i in range(len(variation)):
                if variation[i] == -1:
                    variation[i] = 0
    return variations


rw = [0,0,1,1,0]
blcks = [2]
print_board([[-1, -1, -1, -1], [-1, -1, -1, -1]])
print(get_row_variations(rw, blcks))
# complete_variations(rw)
