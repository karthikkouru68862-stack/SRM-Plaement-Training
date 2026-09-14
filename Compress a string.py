word =input()
l=len(word)
result=""
count=1
for i in range(l-1):
    if word[i]==word[i+1]:
        count=count+1
    else:
        result=result+word[i]+str(count)
        count=1
i=i+1
result=result+word[i]+str(count) 
print(result)
