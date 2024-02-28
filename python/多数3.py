def n(nums):
    appears = {}
    for i in nums:
        if i not in appears:
            appears[i] = 0        
        appears[i] += 1
    print(appears)


nums = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
n(nums)
