char_list = ["a", "n", "t", "a", "a", "t",
"n", "n", "a", "x", "u", "g", "a", "x", "a"]
count=0
i=0
new_list=[]
while i < len(char_list):
    count = char_list.count(char_list[i])
    new_list.append([char_list[i],count])
    i+=1

print(new_list)