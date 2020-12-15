clrlist = [    'black',    'brown',    'red',    'orange',    'yellow',    'green',    'blue',    'violet',    'grey',    'white']
om = dict()
cnt = 0
for i in clrlist:
    om[i]=clrlist[cnt]
    om[i] = dict()
    om[i]["value"] = cnt
    om[i]["mul"] = 10**cnt
    cnt=cnt+1

result = int(str(om[input()]["value"]) + str(om[input()]["value"]))
print(result*om[input()]["mul"])