# Find length of string recursion

st = "Saurabh"

a = list(st)


lengt=0
def length(a, lengt):
  if a == []:
    return lengt
  a.pop()
  return length(a,lengt+1)



print(length(a,0))