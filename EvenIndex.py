list=[12,23,24,56,3,5,6,7,82]
index=0
sum=0
while index<len(list):
    if index%2 == 0:
        print(index)
        sum+=list[index]
    index+=1
print(sum)
    