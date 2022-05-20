l2=[13,20]
h=l2[0]
for x in l2:
    if x>h:
        h=x
print(h)

'''lowest'''
l2=[13,20]
l=l2[0]
for x in l2:
    if x<l:
        l=x
print(l)
l4=["abc","efg","hij","abc","hij"]
abc=[]
efg=[]
hij=[]
for x in l4:
    if x==("abc"):
        abc.append(x)
    elif x==("efg"):
        efg.append(x)
    else:
        hij.append(x)
print(len(abc))
print(len(efg))
print(len(hij))
