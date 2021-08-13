#/ Write a Program to create a pattern like 1,10,100,1000..
#/ After that add sum of these and output should be 11111...

a=int(input("Enter the number"))
b=int(input("Enter the numberwhich want to add"))
sum=0
c=1
index=0
while index < b:
    sum=sum+(a*c)
    a=a*10
    index+=1
print(sum)
