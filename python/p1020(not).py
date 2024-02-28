missle = list(map(int, input().split()))
run_count = 0
n = len(missle)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        
        if missle[i] <= missle[j]:

            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
while len(missle) != 0:
    n = len(missle)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):

            if missle[i] < missle[j]:

                dp[i] = max(dp[i], dp[j] + 1)
    for i in range(max(dp)):
        missle.remove(missle[(dp[i]-1)-i])
    run_count+=1
print(run_count)