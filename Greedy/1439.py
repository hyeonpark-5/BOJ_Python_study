S = input()
res = ''
o = 0
z = 0
for s in S:
    if not res or res[-1] == s:
        res += s
    else:
        if res[-1] == '1':
            o += 1
        else:
            z += 1
        res = s
    
if len(res) != 0:
    if res[-1] == '1':
        o += 1
    else:
        z += 1
        
answer = min(o, z)
print(answer)