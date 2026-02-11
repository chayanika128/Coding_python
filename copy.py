a =[1,10,2]
b = a      # refrence to the same object
c = a.copy()  #shallow copy
b.append(3)
c.append(5)
print(a)
print(b)
print(c)




import copy
a=[[1,2],[3,4]]
b=copy.deepcopy(a)
# b=a.copy()
b[0].append(10)
print(a)
print(b)
