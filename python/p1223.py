def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
n = int(input())
ds = list(map(int, input().split()))
a = 1
time =0 
dy={}
time2=0
finallist=[]
already_in=[]
at=0

for i in ds:
    if i not in dy:
        dy[i]=a
    else:
        while True:
            if str(i)+":"+str(time2) not in dy:
                dy[str(i)+":"+str(time2)]=a
                break
            time2+=1

    a+=1
fn=bubble_sort(ds)

time=0
for i in fn:
    if i not in already_in:
        finallist.append(dy[i])
        already_in.append(i)
    else:
        while True:
            if str(i)+":"+str(time)not in already_in:
                finallist.append(dy[str(i)+":"+str(time)])
                already_in.append(str(i)+":"+str(time))
                break
            time+=1

time2=0
a=0
finallist = map(str,finallist)
for i in range(1,len(fn)):
    at+=fn[i-1]*(n-i)
print(" ".join(finallist))

formatted_number = "%.2f" % round(at/n,2)

print(formatted_number)






























































































