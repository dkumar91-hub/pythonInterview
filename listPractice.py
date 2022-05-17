subject = ["eng","hindi","maths","sci","sst"]
sports = ["football","boxing","hockey"]
sportskit=["bat","ball","gloves"]
capital = ["patna","bhopal","chennai"]
'''interview questions'''

'''1:-print elements of list'''
'''2:-adding elements to a list'''
'''3:-finding index of element in a list'''
'''4:-adding elements to i'th location in a list'''
'''5:-removing element from a list'''
'''6:-to insert elements from list to other list'''
'''7:-size of list'''

'''1:-print elements of list'''
print(sports)
subject.append("sanskrit")
'''2:-adding elements to a list'''
print(subject)
'''3:-finding index of element in a list'''
print(subject[3])
'''4:-adding elements to i'th location in a list'''
sports.insert(2,"cricket")
print(sports)
'''5:-removing element from a list'''
capital.remove("bhopal")
print(capital)
'''6:-to insert elements from list to other list'''
sports.extend(sportskit)
print(sports)
'''7:-size of list'''
len(capital)
print(len(capital))