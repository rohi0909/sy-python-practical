list=[1,2,3,4,5,6]
print(list)

list.append(3)
print(list)

list.insert(2,4)
print(list)

list[2]=10
print(list)

list.extend(["a,b"])
print(list)

print(list[1])
list.remove(2)
print(list)

list.pop(3)
print(list)

list.pop()
print(list)

del list[1]
print (list)
print(len(list)) 



if 2 in list:
    print("element is present")
else:
    print("element is not present")



for i in list:
  print(i)    

print(list.count(3))  

print(list.index(1))
list1=[4,6,1,9,2]
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list.clear()
print(list)
newlist=[1,2,3]
print(newlist)

list3=newlist.copy()
print(list3)



