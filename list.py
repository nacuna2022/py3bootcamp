#!/usr/bin/python3
#today we learn about python lists


list1 = [1,2,3,4,5]
print(list1)

# python lists are not homogenous like C-arrays
# you can combine any datatype in a list
list2 = [1, 4.5, 'a', "abc"]
print(list2)


# a list is also a sequence. so all sequence operators can work on a list
tmplist = [1,2,3] + [4,5,6]
print(tmplist)

tmplist = [123] * 2
print(tmplist)

print(len(tmplist))

print('a' in tmplist)
print(123 in tmplist)

tmplist = [1,2,3,4,5,6,7]
print(tmplist[1:5])
