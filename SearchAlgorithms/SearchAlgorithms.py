"""
SearchAlgorithms
Different search algorithms implemented in Python3
by Dylan Hamer
"""

defaultSearchArray = range(0, 40)
defaultSearchKey = 6

#def displayArray(array):
#    for item in array:
#        print(item)
        
"""Linear Search"""
def linearSearch(searchArray, searchKey):
    index = 0
    found = False

    """Verify that the search key is an integer"""
    if not type(searchKey) == int:
        print("Search key is not an integer!")
        return None, None

    """Iterate through the array to find the search key"""
    while not found or index == len(searchArray):
        if searchArray[index] == searchKey:
            found = True
        index += 1
        
    return found, index

def binarySearch(searchArray, searchKey):
    arrayMin = 0
    arrayMax = len(searchArray) -1

    found = False


    print(len(searchArray))
    
    """Verify that the search key is an integer""" 
    if not type(searchKey) == int:
        print("Search key is not an integer!")
        return None, None

    """Find the search key in the search array"""
    while arrayMin < arrayMax  and not found:
        arrayMid = int( (arrayMax + (arrayMax - arrayMin)) / 2 )
        print(arrayMid)
        if searchArray[arrayMid] == searchKey:
            found = True
        elif searchArray[arrayMid] < searchKey:
            arrayMin = arrayMid + 1
        elif searchArray[arrayMid] > searchKey:
            arrayMax = arrayMid - 1

    return found, arrayMid

def test():
    print("Test array:")
#    displayArray(defaultSearchArray)
    found, position = binarySearch(defaultSearchArray, defaultSearchKey)
    if found:
        print("Found at position {0}".format(position))
    else:
        print("Not found!")
    

if __name__ == "__main__":
    test()
            
    
