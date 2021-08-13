# Replace the String with another one...

mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on" 
index=0
while index <len(mainStr):
    if subStr in mainStr :
        mainStr = mainStr.replace(subStr,replacementStr)
    index+=1
print(mainStr)