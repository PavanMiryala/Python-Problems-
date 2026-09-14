class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        for x in s:
            count[x]=count.get(x,0)+1
        for x in t:
            count[x]=count.get(x,0)-1
        for x in count:
            if count[x]!=0:
                return False 
        return True

    
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
