word =input()

l=len(word)

result=""

i=0

while(i<l):
    result=result+(word[i]*int(word[i+1]))
    i=i+2

print(result)

