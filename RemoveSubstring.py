# program for REmoving Substring from List

mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
index=0
while index <len(mainStr):
    if subStr in mainStr :
        mainStr = mainStr.replace(subStr,'')
    index+=1
print(mainStr)