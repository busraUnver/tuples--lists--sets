friends  = {"ann", "sophie", "jo"}
abroad = {"sophie", "jo"}
local = friends.difference(abroad)
print(local)

friends.add("beth")
print(local)
print(friends.difference(abroad))

#empty set
#set()
print(abroad.difference(friends))

local = {"beth", "ann"}

#union
total = abroad.union(local)
print(total)