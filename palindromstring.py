# List1 = ['R','C','S','E','C','A','R']
# List1 = ['R','C','S','E','C','A','R']
List1=input("Enter the name")
flag=True
i = 0
revIndex = len(List1)-1
while i < len(List1):
    if (List1[i] != List1[revIndex]):
        flag = False
        break
    elif (i==revIndex):
        break
    i=i+1
    revIndex -=1
if (flag):
    print("Given string  is palindrome")
else:
    print("Given string is not palindrome")
