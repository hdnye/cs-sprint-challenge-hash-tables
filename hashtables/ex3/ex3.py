def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    return result


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
        if i is not in arrays:
            seen[i] = 1
        else:
            if seen[i] == 1:
                dups.update(i)
            seen[i] +=1
    
    return dups


    for i in arrays:    
'''