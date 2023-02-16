#a list
l = ["hi", "hii", "hiii"]

#a tuple
#you can't modify a tuple, it's final
t = ("anne", "baba", "cocuk")

#a set
#you can't have duplicate elements
#while lists and tuples keep the order of elements +
#set doesn't necessarily keep the order
s = {"*", "**", "***"}

#with tuples and lists
print(l[0])
print(t[0])
#but with lists this doesn't make sense bc they don't have order

#you can modify list but not tuples
l[0] = "i"
print(l)

#to add element at the end of lists
l.append("hiiii")
l.remove("i")
print(l)

#with sets
s.add("****")
print(s)