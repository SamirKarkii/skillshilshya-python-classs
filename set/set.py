a ={9 ,2,3,4,5}   #homo
# b = {1,2,True, "helloworld"}  #hetero
# empty_set = set()
# dup_set = {1,1,2,2,3,3,4,4}

# print(type(a))
# print(type(b))
# print(type(empty_set))
# print(dup_set)                              

# # a[0]=1        #set is unordered
# # print(a)
# # empty_set.add(4)
# # print(empty_set)

# empty_set.update([1,2,3])
# print(empty_set)

# a.remove(2)  #may through error if not found 
# print(a)

# a.discard(7)   #wont through even the element is not found 
# print(a)

# removed =a.pop()        #will remove randomly ; in list it removes from back
# print("Removed:", removed)
# print(a)



A = {1,2,3,4}
B = {3,4,5,6}   
print("Union:", A.union(B))       # |        
print("INTERSECTION:", A.intersection(B)) #&
print("Difference:",A.difference(B)) #-
print("difference b-a", B.difference(A)) #-
print("Symmetric Difference:",A.symmetric_difference(B)) #^

print(A.issubset(B))
print(B.issuperset(A))
print(A.isdisjoint({5,6}))

#frozen set is immutable versiion of sets , likely don't have a real life usecase
fd = frozenset([1,2,3])
print(fd)
print(fd.add(4))