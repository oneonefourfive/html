nums = list(map(int, input().split()))
n = len(nums)
for i in nums:
    if nums.count(i) > n/2:
        print(i)
        break
