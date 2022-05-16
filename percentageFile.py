'''average of marks'''

maths=85
hindi=70
english=80
sci=70
sst=90
marks_obtained=maths+hindi+english+sci+sst
total_marks=500
percentage=(marks_obtained/total_marks)*100
print("percentage:",percentage)

if percentage >=80:
    print("grade a")
if (percentage >=60) and (percentage<80):
     print("grade b")
elif (percentage >=30) and (percentage<60):
     print("grade c")
else:
    print("fail")
