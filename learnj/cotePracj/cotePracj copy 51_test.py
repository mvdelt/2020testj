# mx = max([7,500,900],[7.1,1,2,3,4,5])
# print(mx)


def searchRange(nums, target):
    def search(n):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            print(f'mid:{mid}')
            if nums[mid] >= n:
                hi = mid
            else:
                lo = mid + 1
        print(f'lo:{lo}, hi:{hi}')
        return lo
    lo = search(target)
    print(f'search(target+1):{search(target+1)}')
    return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]


nums_ex, target_ex = [1,2,3,4,5,6,7,8,9,10], 10
ret=searchRange(nums_ex, target_ex)
print(ret)