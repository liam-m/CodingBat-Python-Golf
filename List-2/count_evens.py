def count_evens(nums):
    res = 0
    for n in nums:
        if n % 2 == 0:
            res += 1
    return res
