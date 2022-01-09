def generate_all_subsets(s):
    all_sets = ['']
    for c in s:
        temp = all_sets.copy()
        temp = [s+c for s in temp]
        all_sets += temp
    return all_sets


XXXXXXXXXXXXXXXXXXXXXXXX


def generate_all_subsets(s):

    answer = ['']
    
    for character in s:
        answer += [cur_string + character for cur_string in answer]
        
    return answer


XXXXXXXXXXXXXXXXXXXXXXXX


def generate_all_subsets(s):
    
    result = [""]
    
    for num in s:
        
        tmp = [st + num for st in result]
        # for j in result:
        #     tmp.appemd(num+j)    
            
        result += tmp
    
    return result
        
    
    # sets = ['']
    # for c in s:
    #     sets += [st + c for st in sets]
    # return sets


XXXXXXXXXXXXXXXXXXXXXXXX


def generate_all_subsets(s):
    res = ['']
    for i in s:
        res += [c+i for c in res]
    return res


XXXXXXXXXXXXXXXXXXXXXXXX


def generate_all_subsets(s):
    
    sets = ['']
    for c in s:
        sets += [st + c for st in sets]
    return sets


XXXXXXXXXXXXXXXXXXXXXXXX





XXXXXXXXXXXXXXXXXXXXXXXX