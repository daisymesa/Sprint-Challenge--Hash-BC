#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    for i in range(length):

        diff = limit - weights[i]

        # check for None
        if hash_table_retrieve(ht, diff) is None:
            # return hash table insert
            hash_table_insert(ht, weights[i], i)
        else:
            # return i, and hash table retrieve diff
            return (i, hash_table_retrieve(ht, diff))


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
