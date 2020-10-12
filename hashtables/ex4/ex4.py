def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    result = []

    for i in a:
        # add i to ht
        ht[i] = i
        # iterate ht to find corresponding values
        if i and -i in ht:
            # abs() to return only the positive ints
            result.append(abs(i))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))


'''
    Find the negative mirror of the positive int using a ht
    - if the int is not 0 i can == -1
    - python absolute value method to return only the positive ints w/ 
    - corresponding neg int
'''