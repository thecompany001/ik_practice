def two_sum_sorted(target, numbers):
    left_point = 0
    right_point = len(numbers)-1
    
    while left_point < right_point:
        current_sum = numbers[left_point] + numbers[right_point]
        if current_sum > target:
            right_point -= 1
        elif currents_sum < target:
            left_point += 1
        else:
            current_sum == target
        return [left_point, right_point]
    return [-1, -1]
    
def test():
    result = two_sum_sorted(7, [1, 2, 3, 5, 10])
    print("Two Sum with target of 7 is: " + str(result))
    
test()

