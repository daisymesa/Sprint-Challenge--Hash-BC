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

    route = []
    # hash table insert for all tickets
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    destination = hash_table_retrieve(hashtable, 'NONE')

    while destination is not 'NONE':
        # append destination to route
        route.append(destination)
        # destination retrieves hastable, destination before repeating loop
        destination = hash_table_retrieve(hashtable, destination)

    return route
