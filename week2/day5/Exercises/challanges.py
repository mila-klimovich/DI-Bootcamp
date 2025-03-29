#1
def insert_item(lst, item, index):
    lst.insert(index, item)
    return lst

my_list = [1, 2, 3, 4]
print(insert_item(my_list, 'a', 2)) 

#2
def count_spaces(s):
    return s.count(' ')

sentence = "Hello world, how are you?"
print(count_spaces(sentence)) 

#3
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

text = "Hello World"
print(count_case(text))

#4
def my_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

numbers = [1, 5, 4, 2]
print(my_sum(numbers))

#5
def find_max(lst):
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num

numbers = [0, 1, 3, 50]
print(find_max(numbers))

#6
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(4))

#7
def list_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

letters = ['a', 'a', 't', 'o']
print(list_count(letters, 'a'))

#8
import math

def norm(lst):
    return math.sqrt(sum(x ** 2 for x in lst))

print(norm([1, 2, 2]))

#9
def is_mono(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

print(is_mono([7, 6, 5, 5, 2, 0])) 
print(is_mono([2, 3, 3, 3])) 
print(is_mono([1, 2, 0, 4]))

#10
def longest_word(lst):
    return max(lst, key=len)

words = ["cat", "elephant", "dog", "giraffe"]
print(longest_word(words))

#11
def separate_lists(lst):
    integers = [item for item in lst if isinstance(item, int)]
    strings = [item for item in lst if isinstance(item, str)]
    return integers, strings

mixed_list = [1, "apple", 2, "banana", 3]
print(separate_lists(mixed_list))

#12
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar")) 
print(is_palindrome("John"))

#13
def sum_over_k(sentence, k):
    words = sentence.split()
    return sum(1 for word in words if len(word) > k)

sentence = "Do or do not there is no try"
k = 2
print(sum_over_k(sentence, k))

#14
def dict_avg(d):
    return sum(d.values()) / len(d)

print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))

#15
def common_div(a, b):
    divisors = [i for i in range(1, min(a, b) + 1) if a % i == 0 and b % i == 0]
    return divisors

print(common_div(10, 20)) 

#16
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(11))

#17
def weird_print(lst):
    return [lst[i] for i in range(len(lst)) if lst[i] % 2 == 0 and i % 2 == 0]

print(weird_print([1, 2, 2, 3, 4, 5]))

#18
def type_count(**kwargs):
    counts = {}
    for value in kwargs.values():
        type_name = type(value).__name__
        counts[type_name] = counts.get(type_name, 0) + 1
    return counts

print(type_count(a=1, b='string', c=1.0, d=True, e=False))  

#19
def my_split(s, delimiter=' '):
    return s.split(delimiter)

print(my_split("Hello world", ' '))

#20
def to_password_format(s):
    return '*' * len(s)

print(to_password_format("mypassword"))