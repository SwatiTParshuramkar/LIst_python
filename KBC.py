question_list = ["How many continents are there?","What is the capital of India?",
    "NG mei kaun se course padhaya jaata hai?"]
options_list = [ ["1) Four", "2) Nine", "3) Seven", "4) Eight"],
["Chandigarh", "Bhopal","Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", 
"Agriculture"]]
index=0

print(question_list[index])
print("Choose your Option")
print(options_list[0][0])
print(options_list[0][1])
print(options_list[0][2])
print(options_list[0][3])
option =input("Tell me the Your Answer")
if option == "1" :
    print("Your answer is Wrong")
elif option == "2":
    print("Your answer is Wrong")
elif option == "3":
    print("Your answer is Right")
elif option == "4":
    print("Your answer is Wrong")
else:
    print("Your answer is Invalid")
