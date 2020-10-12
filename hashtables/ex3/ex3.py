def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in arrays:
        for j in i:
            if j in cache:
                cache[j] += 1
            else:
                cache[j] = 1

    return [j for (j, count) in cache.items() if count == len(arrays)]
    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

'''
    Return the duplicate ints only in a dict
    - need 2 hts for seen & results?
    - index() to easily sort the arrays
    - slice the arrays? index() should work here

    first pass solution: 
    dups = {}
    seen = {}
    
    for i in arrays:
        if i not in arrays:
            seen[i] = 1
        else:
            if seen[i] == 1:
                dups.update(i)
            seen[i] +=1
        return dups


    
'''
