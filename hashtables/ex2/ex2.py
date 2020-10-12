#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # assign k:v pair to tickets list
    start = {ticket.source : ticket.destination for ticket in tickets}
    # set search start at None
    lookup = "NONE"
    next_stop = start[lookup]
    route = []

    # while loop to find route
    while lookup != "NONE":
        next_stop = start[lookup]
        route.append(next_stop)
        lookup = next_stop
    return route


'''
    Return ht of k:v's that = source: destination
    - sort to find original source tkt, append ht with corresponding dest value
    - make the prev value the new key & add the corresponding dest as the new value
    - lookup table for solution 

    first pass solution: 
    ht = {}
    key  = (source, destination)
    for i, ticket in enumerate(tickets):
        return ht[ticket] = i
    for key in ht:
        if key in ht:
            ht[destination] = [key]
        else:
            ht[key].update[destination]
'''