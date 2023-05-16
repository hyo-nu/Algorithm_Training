word = input()
sset = set()
for num in range(1,len(word)+1):
    for i in range(len(word) - num + 1):
        sset.add(word[i:i+num])
print(len(sset))