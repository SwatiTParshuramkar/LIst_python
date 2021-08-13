# list=['A','B','C','D','E','F','G','H','I']
# flag=True
# index=0
# revIndex=len(list)-1
# while index <len(list):
#         if index%2==0 or revIndex%2==0:
#             if list[index]==list[revIndex]:
#                 print(list[index])
#                 break
#             elif list[index] != list[revIndex]:
#                 flag=False
#                 break
#         index+=1
#         revIndex-=1
        
# List1 = ['R','C','S','E','C','A','R']
List1 = ['A','A','A','A','A','A','A']
# List1=input("Enter the name")
flag=True
i = 0
revIndex = len(List1)-1
while i < len(List1):
    if (i%2==0) == (revIndex%2 ==0):
        if (List1[i] != List1[revIndex]):
            flag = False
            break
        elif (i==revIndex):
            print(List1[i])
            break
    i=i+1
    revIndex -=1
