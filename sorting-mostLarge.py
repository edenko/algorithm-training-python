from functools import cmp_to_key

def sol(numbers = [6, 10, 2]):
    strs = list(map(str, numbers))

    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        return 0
    
    strs.sort(key=cmp_to_key(compare))
    return ''.join(strs)
