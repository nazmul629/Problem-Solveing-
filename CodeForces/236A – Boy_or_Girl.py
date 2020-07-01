name = input()
sort_name = sorted(name)
count = 1
for i in range(0,len(name)-1,1):
    if sort_name[i] != sort_name[i+1]:
        count+=1
if count%2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
