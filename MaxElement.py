numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=numbers[0]
while i<len(numbers):
    m=numbers[i]
    if m>max:
        max=m
    i=i+1
print("Maximum number is", max)
    
        