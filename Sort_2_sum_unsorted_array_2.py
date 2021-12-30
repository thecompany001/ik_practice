def two_sum(numbers, target):
    hmap = {}
    for i in range(len(numbers)):
        if target - numbers[i] in hmap:
            return [i, hmap[target-numbers[i]]]
        else:
            hmap[numbers[i]] = i
    return [-1, -1]




def two_sum(numbers, target):
    if len(numbers) <=1:
        return
    hashmap= {}
    for index, value in enumerate(numbers):
        diff = target - value
        if diff in hashmap:
            return [index,hashmap[diff]]
        else: 
            hashmap[value] = index
    
    return [-1,-1]


def two_sum(numbers, target):
    seen={}
    for i,num in enumerate(numbers):
        if target-num in seen:
            return(i,seen[target-num])
        else:
            seen[num]=i
            
    return(-1,-1)