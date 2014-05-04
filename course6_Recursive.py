from functools import reduce
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)


def jc(n):
    return reduce(operator.mul, range(1,10)) 


print(factorial(0))
print(factorial(5))


def is_palindromes(s):
    return s==s[::-1]

print(is_palindromes('abba'))
print(is_palindromes('abba'))
print(is_palindromes('abca'))


def rabbits(n):
    if n==1 or n==2:
        return 1
    else:
        if n<=5:
            return rabbits(n-1)+rabbits(n-2)
        else:
            return rabbits(n-1)+rabbits(n-2)-rabbits(n-5)
print(rabbits(10))


def hexes_to_udaciousness(n, spread, target):
    if target < n:
        return 0
    else:
        if target>n*(1+spread):
            return hexes_to_udaciousness(n*(1+spread), spread, target)+1
        else:
            return 1    
print(hexes_to_udaciousness(100000, 2, 36230) )
print (hexes_to_udaciousness(50000, 2, 150001))
print (hexes_to_udaciousness(20000, 2, 7 * 10 ** 9) )
print(hexes_to_udaciousness(15000, 3, 7 * 10 ** 9))


def is_list(p):
    return isinstance(p, list)
def deep_count(p):
    for entry in p:
        if is_list(entry)==True:
            return len(p)+deep_count(entry)
    return len(p)
print(deep_count([1, 2, 3]))
print(deep_count([1, [], 3])) 
print(deep_count([1, [1, 2, [3, 4]]]))
print(deep_count([[[[[[[[1, 2, 3]]]]]]]]))
