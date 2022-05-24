def area(lenght,breadth):
    area=lenght*breadth
    print(area)
def perimeter(length,breadth):
    perimeter=2*(length+breadth)
    print(perimeter)
def area_of_triangle(base,height):
    area_of_triangle=.5*(base*height)
    print(area_of_triangle)
lenght=10
breadth=20
base=10
height=20
area(lenght,breadth)
perimeter(lenght,breadth)
area_of_triangle(base,height)

'''function'''
def xyz(L1):
    for i in L1:
        print(i)
list1 = [3,7,9,8]
xyz(list1)
def abc(l2):
    for x in l2:
        print(l2[3])
list2 = [5,6,7,3]
abc(list2)
def pqr(l3):
    for i in l3:
        list2.append(list3)
        list2.insert(2,5)
        list2.extend(list3)
        list2.remove(4)
        print(len(list3))
        print(list2)
list3 = [9,1,3,8,5,4,2]
list2 = [5,6,7,3]
abc(list2)
pqr(list3)
