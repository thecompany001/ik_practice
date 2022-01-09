def generate_all_subsets(s):
    res = ['']
    
    for num in s:
        for j in res:
            temp.append(num)