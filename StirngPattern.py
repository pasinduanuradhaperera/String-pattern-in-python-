s = input("Enter a word : ")
for x in range(len(s)):
    print(str((x+1))+ ". " + (s[x]*(x+1)))
