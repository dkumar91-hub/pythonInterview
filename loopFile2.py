ball=["blue","blue","green","white","green","green","blue","blue","white","blue","blue","green","blue"]
blue=[]
green=[]
white=[]
for x in ball:
    if x==("blue"):
      blue.append(x)
    elif x==("green"):
      green.append(x)
    else:
      white.append(x)
print(len(blue))
print(len(white))
print(len(green))