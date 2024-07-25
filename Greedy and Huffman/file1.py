# x = "字"
# print(ord(x))


# u= "漢"
# print(ord(u))
# v= "ल"
# print(ord(v))

# s1 = "chocolate"

from collections import defaultdict,Counter
## frequency map for a string.......

string1 = input("Enter a string: ")

def freqTable(string1:str)->dict:
    # table = dict()
    # for i in string1:
    #     if i not in table:
    #         table[i] = 1
    #     else:
    #         table[i] += 1
    # return table
    
    
    
    ### default dict...
    # table = defaultdict(int)
    # for i in string1:
    #     table[i] += 1
        
    # return table



    ### using counter
    table = Counter(string1)
    return table


print(freqTable(string1))



class Node:
    c:str
    f:int
    left:int
    right:int

