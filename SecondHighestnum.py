list1=[50,40,23,70,56,12,5,10,7]       
mx=list1[0]
secondmax=list1[1]
i=0
while i<len(list1):
    if list1[i]>mx: 
        secondmax=mx
        mx=list1[i] 
    elif list1[i]>secondmax : 
        secondmax=list1[i]
    i=i+1
print("Second highest number is :", secondmax)