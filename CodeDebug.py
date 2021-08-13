# name = ["Savitri", "Phule", "26"]
# print (name[0] + name[1] + name[2])
# Code mei dekhiye naam theek se print kyu nahi ho raha 

# marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
marks = [10, 32, 42, 65, 67, 89, 76, 38, 67]
total_marks = 0
counter = 0
while counter < len(marks):
    total_marks = total_marks + marks[counter]
    counter = counter + 1 
print(total_marks)