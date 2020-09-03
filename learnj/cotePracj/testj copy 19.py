# dict1 = {{1,2}:'hi', {1,3}:'bi'} # TypeError: unhashable type: 'set'

# dict2 = {1:{1,2}, 2:{1,3}} # i. 이건 됨.
# print(type(dict2))
# print(type(dict2[1]))

# nums = [3,4,6,7,9]
# for n in nums:
#     a = nums[:]
#     a.remove(n)
#     print(a)

# {[1,2], [3,4]} # TypeError: unhashable type: 'list'

# print({(1,2), (3,4)}) # i. 이건 됨.
# print({(1,2), (3,4), (4,3), (3,4)})
# print({tuple([1,2]), tuple([3,4]), tuple([1,2])})

li = [(1), (2,)]
print(li)
print(type(li[0]))
print(type(li[1]))

nums = [1,2,3,4,5,6,7,8,9,10]
set_ex = {(n,) for n in nums if n%2==0 }
print(set_ex)
print(type(set_ex))