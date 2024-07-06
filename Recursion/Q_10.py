# Reverse a String using recursion

st = "Saurabh"
 
def reverseString(st,length):
    
    if length == 0:
        return st[length]
    else:
        return  st[length] + reverseString(st,length-1)
        
        
print(reverseString(st,len(st)-1))