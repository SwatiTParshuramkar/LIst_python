# List1 = ['R','C','S','E','C','A','R']
List1 = ['s','w','a','t','t','i','s']
# List1=input("Enter the name")
flag=True
i = 0
revIndex = len(List1)-1
while i < len(List1):
    if (i%2==0) or (revIndex%2 ==0):
        if (List1[i] != List1[revIndex]):
            print(List1[i])
            flag = False
            break
        elif (List1[i]==List1[revIndex]):
            print(List1[i])
            # break
    i=i+1
    revIndex -=1
