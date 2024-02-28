
def f(nums):
    n = len(nums)
    ignore = set()
    answer = set()
    for i in nums:
        if i not in ignore:
            if nums.count(i) > n/3 and i not in answer:
                answer.add(i)
            else:
                ignore.add(i)
    print(answer, ignore)


# nums = list(map(int, input().split()))
# nums = [ 3, 3, 3, 2, 2, 2, 2, 3 ]
# nums = [ 3, 3, 3, 2, 2, 2, 2, 3, 4, 6, 9, 2 ,2,2,2,2,2,2]
nums = [ 1, 1, -1, -2, 3, 3, 3, 2, 2, 2, 2, 3 ]
f(nums)
