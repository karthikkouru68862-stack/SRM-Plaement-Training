word = input()
l=len(word)
result= ""
i = 0

while i < l:
    n = int(word[i])
    i += 2
    j = word.index(")", i)
    result+= word[i:j] * n
    i = j + 1

print(result)
