l=[2,"abc",7,4,8,"xyz"]
l3=[4,9,6,"pqr"]
l.append(l3)
print(l)
l.remove("xyz")
print(l)
l.insert(2,"xyz")
print(l)
l.extend(l3)
print(l)
print(len(l3))
print(l[3])

'''condition'''
a=7
b=4
if a>b:
    print("true")
else:
    print("false")

'''tuple'''
l={1,2,4,7,5,7,2,8,7}
print(l)

'''set'''
l2=(1,3,9,5,4,6,3,7,1)
print(l2)

'''dictionary'''
l={"name":("akanksha","diksha"),"address":("gaya","pune")}
print(l)
l["age"]=25
print(l)
l["age"]=30
print(l)

'''LIST COMPREHENSION'''
L=[8,8,5,4,6,6,4,3,2]
L1=[x for x in L if x>5 ]
print(L1)
l2=[x for x in L if x<5]
print(l2)
l3=[x*2 for x in L ]
print(l3)
l4=[x*x for x in L]
print(l4)



