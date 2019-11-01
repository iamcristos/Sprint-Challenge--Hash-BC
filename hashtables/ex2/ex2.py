#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Insert locations on hash table
    for location in range(len(tickets)):
        hash_table_insert(hashtable, tickets[location].source, tickets[location].destination)

    # set start point in route array to NONE
    route[0] = hash_table_retrieve(hashtable, 'NONE')

    for location in range(1, len(route)):
        route[location] = hash_table_retrieve(hashtable, route[location - 1])


    return route