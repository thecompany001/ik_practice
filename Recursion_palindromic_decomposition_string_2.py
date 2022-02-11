def generate_palindromic_decompositions(s):
    def is_palindrome(start, end):
        if s[start] != s[end]:
            return False
        if start >= end:
            return True
        return is_palindrome(start+1, end-1)
        
    result ={}
    for start in range(len(s), -1, -1):
        inter = []
        for i in range(start, len(s)):
            if is_palindrome(start,i):
                if i == len(s)-1:
                    inter.append(s[start:])
                else:
                    prefix = s[start:i+1]
                    for p in result[i+1]:
                        inter.append(prefix+ '|' + p)
            result[start]= inter
    return result[0]


XXXXXXXXXXXXXXXX


def generate_palindromic_decompositions(s):

    resultMap = {}

    def is_palindrome(start, end):
        if s[start] != s[end]:
            return False
        if start >= end:
            return True
        return is_palindrome(start+1, end-1)
    
    for startIndex in range(len(s), -1 ,-1):
        inter = []
        for i in range(startIndex, len(s)):
            if is_palindrome(startIndex, i):
                if i ==len(s) - 1:
                    inter.append(s[startIndex:])
                else:
                    prefix = s[startIndex:i + 1]
                    for p in resultMap[i+1]:
                        inter.append(prefix + "|" + p)
            resultMap[startIndex] = inter
    return resultMap[0]


XXXXXXXXXXXXXXXX


from functools import lru_cache

def isPalin(string):
    return string == string[::-1] 


def generate_palindromic_decompositions(s):
    if not s:
        return []
    results = palinRecurse(s)
    return results
    

@lru_cache(maxsize = None)
def palinRecurse(s):
    s_len = len(s)
    
    if s_len==1:
        return [s]
    
    results = []
    for i in range(s_len):
        sub_string = s[:i+1]
        if isPalin(sub_string):
            if (i == s_len - 1):
                results.append(sub_string)
            else:
                valid_palins = palinRecurse(s[i+1:])
                for each_palin in valid_palins:
                    results.append(sub_string + '|' + each_palin)
    
    return results

XXXXXXXXXXXXXXXX


def generate_palindromic_decompositions(string):
    if not string or len(string) == 1:
        return [string]

    output = []
    n = len(string)

    def _palindromic_decomposition(so_far, start):
        # base case
        if start == n:
            output.append('|'.join(so_far))
            return

        # take every possible string from the current position and 
        # if it's palndromic go forward, and if it's not prune
        for i in range(start+1, n+1):
            curr = string[start:i]
            if is_palindrome(curr):
                so_far.append(curr)
                _palindromic_decomposition(so_far, i)
                # at the end of dfs remove what was appended to
                so_far.pop()

    _palindromic_decomposition([], 0)
    return output


def is_palindrome(string):
    if not string or len(string) == 1:
        return True

    low, high = 0, len(string) - 1
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1

    return True


def is_palindrome_rec(string):
    if len(string) == 0:
        return True
    return _is_palindrome(string, 0, len(string)-1)


def _is_palindrome(string, start, end):
    # empty string or string of 1 character
    if start == end or start > end:
        return True

    return string[start] == string[end] and _is_palindrome(string, start+1, end-1)



XXXXXXX



from functools import lru_cache

def generate_palindromic_decompositions(s):
    if not s:
        return []
    results = palinRecurse(s)
    return results

def isPalin(string):
    return string == string[::-1]

@lru_cache(maxsize = None)
def palinRecurse(s):
    s_len = len(s)

    if s_len==1:
        return [s]

    results = []
    for i in range(s_len):
        sub_string = s[:i+1]
        if isPalin(sub_string):
            if (i == s_len - 1):
                results.append(sub_string)
            else:
                valid_palins = palinRecurse(s[i+1:])
                for each_palin in valid_palins:
                    results.append(sub_string + '|' + each_palin)

    return results


XXXXX


def generate_palindromic_decompositions(s):

    def is_palindrome(start, end):
        if s[start] != s[end]:
            return False
        elif start >= end:
            return True
        else:

            return is_palindrome(start+1, end-1)

    results = {}
    for start in range(len(s), -1, -1):
        inter = []
        for i in range(start, len(s)):

            if is_palindrome(start, i):

                if i == len(s) - 1:
                    inter.append(s[start:i+1])
                else:

                    prefix = s[start:i+1]
                    for suffix in results[i+1]:
                        tmp = prefix + "|" + suffix
                        inter.append(tmp)
                results[start] = inter
    return results[0]