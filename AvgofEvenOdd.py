# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
a=0
sum=0
sum1=0
while a<len(elements):
    if elements[a]%2==0:
        sum+=elements[a]
    else:
        sum1+=elements[a]
    a+=1
print(sum/(len(elements)),"Average of even number")
print(sum1/(len(elements)),"Avaerage of odd number")