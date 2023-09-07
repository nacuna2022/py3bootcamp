#!/usr/bin/python3

# sequences can be lists, strings and tuples
# have generic operators/functions that can be used on all sequences.

# indexing          [] : access element of sequence
# concatenation      + : combine sequences together
# repetition         * : concatenate a repeated number of times
# membership        in : test if in sequence
# length           len : count of items
# slicing          [:] : extract part of sequence


#indexing
mylist = [0, 1,2,3,4,5,6,7,8,9]
print(mylist[3])

#concatenation
mylist = mylist + [10,11,12,13,14,15,16,17,18,19]
print(mylist[15])

#repetition 
mylist2 = [0] * 6
print(mylist2)

mylist3 = [5, 7] * 8
print(mylist3)

#membership
mylist4 = ['a', 'b', 'c']
print('a' in mylist4)
print('x' in mylist4)
print(1024 in mylist4)

#length
print(len(mylist))
print(len(mylist2))
print(len(mylist3))


#slicing
mylist5 = [0,1,2,3,4,5,6,7,8,9]
print(mylist5[0:10])
print(mylist5[:5])
print(mylist[5:])
