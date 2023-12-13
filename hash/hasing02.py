# step 01
# DataItem
# define a data item having some data and key, 
# based on which the search is to
# be conducted in a hash table

# step 02
# Hash method
# define a hashing method to compute the hash code of the key of dataitem

class DataItem:
    def __init__(self,data,key):
        self.data = data 
        self.key = key
    

def hashCode(key,size):
    return key % size

def search(key,hashArray,size):
    # get the hash
    hashIndex = hashCode(key,size)

    # move in array until empty
    while hashArray[hashIndex] is not None:
        if hashArray[hashIndex].key == key:
            return hashArray[hashIndex]
        # go to the next cell
        hashIndex += 1

        hashIndex %= size
    return None

if __name__ == "__main__":
    SIZE = 100
    hashArray =  [None] * SIZE 
    keyToSearch = 42

    result = search(keyToSearch, hashArray, SIZE)

    if result is not None:
        print(f"Found DataItem with key: {result.key}")
        print(f"Data: {result.Data}")
    else:
        print(f"DataItem with key {keyToSearch} not found")