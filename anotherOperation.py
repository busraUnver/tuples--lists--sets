art = {"bob", "jen", "rolf", "charlie"}
science = {"bob", "jen", "adan", "ann"}

#intersection
both =art.intersection(science)

print(both)

#also with signs
set1 = {"1", "2", "3"}
set2 = {"2", "3", "4"}
set3 = {"3", "4", "5"}

#union
print(set1 | set2 | set3)

#intersection
print(set1 & set2)

#difference
print(set1 - set2)
print(set2 - set1)