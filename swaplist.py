import sys

num = raw_input("enter the nums ")

list_1 = num.split()

lnt = len(list_1)

def swaplist(list_1, lnt):
    temp = list_1[0]
    list_1[0] = list_1[lnt-1]
    list_1[lnt-1] = temp

    return list_1


swaplist(list_1, lnt)

print ("the final list is \n")
print list_1
