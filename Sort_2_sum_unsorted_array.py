def two_sum(nums, target):
    hashmap = {}
    
    for i in range(len(nums)):
        if target-nums[i] in hashmap:
            return [i, hashmap[target-nums[i]]]
        else:
            hashmap[nums[i]] = i
    return [-1, -1]
        
def test():
    result = two_sum([5, 3, 10, 45, 1], 55)
    print("Two Sum target is: " + str(result))
    
test()