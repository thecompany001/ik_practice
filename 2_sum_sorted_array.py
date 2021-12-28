def pair_sum_sorted(numbers, target):
    left_point = 0
    right_point = len(numbers) -1
    
    while left_point < right_point:
        current_sum = numbers[left_point] + numbers[right_point]
        if current_sum > target:
            right_point -= 1
        elif current_sum < target:
            left_point += 1
        else:
            current_sum == target
        return [left_point, right_point]
    return [-1, -1]

def test():
    result = pair_sum_sorted([1, 2, 3, 5, 10], 15)
    print("Two Sum with target of 7 is: " + str(result))
    
test()

