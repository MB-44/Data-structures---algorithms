# hash table is a ds which stores data in associative manner, in a hash 
# table, data is stored in an array format, where each data value has its own 
# unique index value. Access of data becomes very fact 
# if we know the index of the desired data

# Hashing
# hashing is a technique to convert a range of key values into a range of
# index of an array. We are going to use modulo operator to get a range of
# key value.

# example
# (1, 20) --> key --> 1 --> hash --> 1 % 20 = 1 ---> array index --> 1
# (14, 20) --> key --> 14 --> hash --> 14 % 20 = 14 ---> array index --> 14


# linear probing
# it may happen that hashing technique is used to create and already used index
# of the array. In such a case, we can search the next empty location in the array
# by looking into the next cell until we find an empty cell.
# this technique called linera probing

# it's almost like that
