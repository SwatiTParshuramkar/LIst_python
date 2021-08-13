# # # # polindrome or not
# # # # List=input("Enter the name to check polindrome")
# # # List=['R','A','C','E','C','A','R']
# # # List1=[]
# # # index=0
# # # rev_len=len(List)-1
# # # while index < len(List):
# # #     First_value = List[index]
# # #     Last_value = List[rev_len]
# # #     if First_value == Last_value:
# # #         List1.append(List[rev_len])
# # #         rev_len=rev_len-1
# # #     index+=1
# # # if List == List1:
# # #     print("Given List is Polindrome")
# # # else:
# # #     print("Given List is not Polindrome")

# List=["k","o","m","o","k"]
# List1=[]
# index=0
# rev_len=len(List)-1
# while index < len(List)//2:
#     First_value = List[index]
#     Last_value = List[rev_len]
#     if First_value == Last_value:
#         List1.append(List[rev_len])
#         rev_len=rev_len-1
#     index+=1
# if First_value==Last_value:
#     print("P")
# else:
#     print("NP")
    

# # # List=input("Enter the name to check polindrome")
# # List=['R','A','C','E','C','A','R']
# # List1=[]
# # index=0
# # rev_len=len(List)-1
# # while index < len(List):
# #     if List[index] == List[rev_len]:
# #         List1.append(List[rev_len])
# #         rev_len=rev_len-1
# #     index+=1
# # if List == List1:
# #     print("Given List is Polindrome")
# # else:
# #     print("Given List is not Polindrome")
    

# List1 = ['R','C','S','E','C','A','R']
# flag=True
# i = 0
# revIndex = len(List1)-1
# while i < len(List1):
#     if (List1[i] != List1[revIndex]):
#         flag = False
#         break
#     elif (i==revIndex):
#         break
#     i=i+1
#     revIndex -=1
# if (flag):
#     print("Given list is palindrome")
# else:
#     print("Given list is not palindrome")
    
