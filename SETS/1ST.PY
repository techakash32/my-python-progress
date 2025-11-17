#sets overview

set={"10" ,"20","30"}
set1={}
print(type(set1))
print(type(set))

#add element to sets

set.add("80")
print("insert: ",set)

#add list to set

set.update([1,2,3,4,5])
print("insert 2: ",set)

#union

sec={10,20,30,40}
sec2={40,50,70,80,90}
print(sec.union(sec2))

#intersection

print(sec.intersection(sec2))

#update

print(sec2.intersection_update(sec))

#semmtric difference
SECTION={10,20,30,40,50}
SECTION2={10,70,80,90}

print(SECTION.difference_update(SECTION2))

#SYMMETIC DIFFERENCE

print(SECTION.symmetric_difference(SECTION2))

#symmetric difference update

print(SECTION.symmetric_difference_update(SECTION2))

#Is subset

print(SECTION.issubset(SECTION2))

#is disjoint

print(SECTION.isdisjoint(SECTION2))


#

