# 1
def root(number):
    return number**2
x = int(input())
print(root(x))

# 2
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
x = int(input())
print(is_even(x))

# 3
def factorial(n):
    if n >=0:
        total = 1
        for i in range(1, n + 1):
            total = total * i
        return total
    else:
        return -1
x = int(input())
print(factorial(x))

# 4
def reverse(s):
    return s[::-1]
stroka = input()
print(reverse(stroka))

# 5
def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a
x = int(input())
print(fibonacci(x))

# 6
def count_vowels(s):
    count = 0
    for i in s:
        if i in 'уеыаоэяиюУЕЫАОЭЯИЮ':
            count+=1
    return count
stroka = input()
print(count_vowels(stroka))

# 7
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
stroka = input()
print(is_palindrome(stroka))

# 8
def power(x, n):
    return x**n
a = int(input())
b = int(input())
print(power(a, b))

# 9
def is_anagram(s1, s2):
    if (sorted(s1) == sorted(s2)):
        return True
    else:
        return False
st1 = input()
2 = input()
print(is_anagram(st1, st2))

# 10

def is_pangram(s):
    if not set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') - set(s.lower()):
        return True
    else:
        return False
st = input()
print(is_pangram(st))