i, n = map(str, input().split())
char_offset = ord(i) + int(n)
print(chr(char_offset))
#ну, и опять же, если сплит нельзя было юзать:
"""s = input()
n = ""
j = ""
for i in range(len(s)):
    if s[i] != ",":
        n = n + s[i]
    else:
        j = n
        n = ""
char_offset = ord(j) + int(n)
print(chr(char_offset))"""