students=['Rishabh','Madhurima','Rahul','Abhishek','Faizal','Muskan']
marks=[10,20,56,45,36,20]
print(len(students))
print(len(marks))
length=len(students)
counter=0
while counter<length:
    print(students[counter] + str(marks[counter]))
    counter=counter+1