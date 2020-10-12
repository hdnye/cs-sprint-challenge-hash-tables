# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here  
    # list comprehension with any()
    return [i for i in files if any(sub in i for sub in queries)]


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

'''
    - To find the path from the queries, need to search to the end of the path to find
    - the matching name
    - if querie in files, return files

    first pass solution:
    
    cache = {}
    for i in files:
        queries[i] = i
        if i in files:
            cache[i] += 1
        else: 
            return None

    
'''