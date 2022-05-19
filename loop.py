'''for loop'''
l1=[2,8,6,4,5,7,9]
le=[]
lo=[]
for y in l1:
    if y % 2 == 0:
        le.append(y)
    else:
         lo.append(y)
print("lo=",lo)
print("le=",le)

