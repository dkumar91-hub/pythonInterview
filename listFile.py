'''list of flat'''
b402vi = ["satya","nivedita"]
h1702lr = ["dilip","akanksha","diksha"]
h1705lr = ["aditya","ritika","adira"]
print("b402vi=",b402vi)
print("h1702lr=",h1702lr)
print("h1705lr=",h1705lr)
'''add new element to a list'''
b402vi.append("xyz")
print("b402vi=",b402vi)
'''add element of one list in other list'''
b402vi.extend(h1702lr)
print("b402vi=",b402vi)
'''add an element to n'th index'''
b402vi.insert(1,"abc")
print("b402vi=",b402vi)
'''remove a particular name'''
b402vi.remove("dilip")
print("b402vi=",b402vi)
'''lenth of list'''
len(b402vi)
print(len(b402vi))
'''finding n'th element'''
print(b402vi[3])
'''find last element of list'''
print(b402vi[5])
'''tuple'''
b402vi = ("satya","nivedita")
h1702lr = ("dilip","akanksha","diksha")
h1705lr = ("aditya","ritika","adira")
# b402vi.append("xyz")
print("b402vi=",b402vi)

'''set'''
b402vi = {"satya","nivedita"}
h1702lr = {"dilip",2,4,2,1,1,1,"dilip","akanksha","diksha"}
h1705lr = {"aditya","ritika","adira"}
print(h1702lr)
