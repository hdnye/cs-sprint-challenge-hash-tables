def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    results = {}

    # iterate over weights list & index
    for i, weight in enumerate(weights):
        # if weight in results:
        #     results[weight].update(i)
        # else:
        results[weight] = i

    # loop over weights & find pairs == to limit
    for i in range(len(weights)):
        sum_indeces = limit - weights[i]
        if sum_indeces in results:
            return(max(i, results[sum_indeces]), min(i, results[sum_indeces]))

    return None


"""
- a f() that adds 2 indeces together & compares them to the limit to find the 
- pair that equal it. 
- returns the pairs with the higher value index listed first

first pass solution:

weight = {}
results = {}  
    for i in range(len(weights)):
        for j in range(len(weights)):
            if weights[i] + weights[j] == limit:
                results.append(weights[i][j])
            else: return None
"""
