import bisect

# def searchRange(nums, target):
#     lo = bisect.bisect_left(nums, target)
#     print(f'lo:{lo}')
#     lo = bisect.bisect_left(sorted(nums), target)
#     print(f'sorted nums:{sorted(nums)}')
#     print(f'lo:{lo}')
#     return [lo, bisect.bisect(nums, target)-1] if target in nums[lo:lo+1] else [-1, -1]


# nums_ex, target_ex = [1,15,7,4,5,5,5,6,9,8,2], 7
# ret=searchRange(nums_ex, target_ex)
# print(ret)

i = bisect.bisect_right([1,3,5,7,9], 9)
print(i) # 5 (인덱스 벗어난 값인데도 리턴.)

