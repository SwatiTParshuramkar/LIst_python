n = [ 19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
duplicate_n=[]
index=0
number=[]
while index<len(n):
    if n[index] not in duplicate_n :
        duplicate_n.append(n[index])
    else :
        number.append(n[index])
    index+=1
print(duplicate_n)
print(number)