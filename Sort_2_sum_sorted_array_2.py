def pair_sum_sorted(numbers, target):
    i = 0
    j = len(numbers) -1
    
    while i < j:
        total = numbers[i] + numbers[j]
        if total == target:
            return ([i,j])
        elif total < target:
            i += 1
        else:
            j -= 1
    return ([-1,-1])



def test():
    result = pair_sum_sorted([1, 2, 3, 5, 10], 7)
    print("Two Sum target is: " + str(result))
    
test()

