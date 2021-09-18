def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print('tri_recursion')
tri_recursion(10)

def tri_loop(k):
    result = k
    while k > 0:
        print(result)
        result += k - 1
        k -= 1
    return result

print('tri_loop')
tri_loop(10)
