s = "a10b2c2"
result = ""
i = 0
while i < len(s):
    ch = s[i]
    i += 1
    num = ""
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    result += ch * int(num)
print(result)
s = "a10b2c2"
result = ""
i = 0
while i < len(s):
    ch = s[i]
    i += 1
    num = ""
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    result += ch * int(num)
print(result)