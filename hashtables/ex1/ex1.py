#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # loop through the weights
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
        first_weight = hash_table_retrieve(ht, weights[i])
        weight_diff = limit - weights[i]

        second_weight = hash_table_retrieve(ht, weight_diff)
        if second_weight:
            if  first_weight == second_weight:
                return (1, 0)
            if first_weight > second_weight:
                return (first_weight, second_weight)
            else:
                return (second_weight, first_weight)   
    """
    YOUR CODE HERE
    """

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
