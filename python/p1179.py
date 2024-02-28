list= list(map(int,input().split()))
count=0
for i in range(list[0],list[1]+1):
    count+=str(i).count("2")
print(count)