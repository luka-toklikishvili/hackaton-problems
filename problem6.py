word="goa is best academy"
vowels="aeiou"
res=""

for i in word:
    if vowels in word:
        res += i
print(res)
