l = []
lis = [1,56,"x",34,2.34,["s","t","t","o","k","a"]]
print(lis)

a=[a+b for a in 'assl' if a != "list" for b in 'soap' if b !='']
print(a)

l.append(23)
l.append(34)
b = [24,67]
l.extend(b)
l.insert(1,56)
l.append(34)
l.remove(34)
l.pop(0)
print(l.index(56))
print(l.count(34))
l.sort()
l.reverse()
l.clear()
print(l)