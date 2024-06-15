from typing import Dict, List

def fact(n: int) -> int:
    """
    Returns n factorial i.e., n!
    Assume n >= 0.

    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(5)
    120
    """
    if n <= 1:
        return 1
    return n*fact(n-1)    



def fib(n: int) -> int:
    """
    Returns nth Fibonacci number.
    Assume n >= 0.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(5)
    5
    >>> fib(10)
    55
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)



def get_length(s: str) -> int:
    """
    Returns the length of s. Do not use len or a loop.
    """
    if s == '':
        return 0
    return 1 + get_length(s[1:])



def count_char(s: str, char: str) -> int:
    """
    Returns the number of times char appears in s.
    Do not use len or a loop.
    """
    if s == '':
        return 0
    if s[0] == char:
        return 1 + count_char(s[1:], char)
    return count_char(s[1:], char)



def is_palindrome(s: str) -> bool:
    """
    Returns True iff s is a palindrome.
    Do not use rev or a loop.
    """
    if len(s) < 2:
        return True
    if s[0] != s[1]:
        return False
    return is_palindrome(s[1:-1])



def reverse(s: str) -> str:
    """
    Returns the reverse of s.
    """
    if len(s) < 2:
        return s
    return reverse(s[1:]) + s[0]



def remove_first(s: str, char: str) -> str:
    """
    Returns a version of s with the first occurence of char removed.
    """
    if s == '':
        return s
    if s[0] == char:
        return s[1:]
    return remove_first(s[1:])
    
    
    
def is_near_palindrome(s: str) -> bool:
    """
    Returns True iff s can be turned into a palindrome by removing
    up to 1 character.

    >>> is_near_palindrome("tacocamt")
    True
    >>> is_near_palindrome("11111101111")
    True
    >>> is_near_palindrome("1111011111110")
    False
    """
    if len(s) < 3:
        return True
    if s[0] != s[-1]:
        return is_palindrome(s[1:]) or is_palindrome(s[:-1])
    return is_near_palindrome(s[1:-1])



def is_k_near_palindrome(s: str, k) -> bool:
    """
    Returns True iff s can be turned into a palindrome by removing
    up to k characters.
    """
    if len(s) <= k + 1:
        return True
    if k == 0:
        is_palindrome(s)
    if s[0] == s[-1]:
        return is_k_near_palindrome(s[1:-1], k)
    return is_k_near_palindrome(s[:-1], k - 1) or is_k_near_palindrome(s[1:], k - 1)



def my_sum(L: List[int]) -> int:
    """
    Returns the sum of all the numbers in L.
    """
    if L == []:
        return 0
    return L[0] + my_sum(L[1:])



def count(L: List[int], num: int) -> int:
    """
    Returns the number of time num appears in L.
    """
    if L == []:
        return 0
    if L[0] == num:
        return 1 + count(L[1:], num)
    return count(L[1:], num)



def index_of(L: List[int], num: int) -> int:
    """
    Returns the index of the first occurence of num.
    Assume num appears at least once in L.

    >>> index_of([1,2,3], 1)
        0
    >>> index_of([1,2,3], 2)
        1
    >>> index_of([1,2,3,3,1], 3)
        2
    """
    if L == []:
        return None
    if num == L[0]:
        return 0
    return 1 + index_of(L[1:], num)



def remove_first(L: List[int], num: int) -> List[int]:
    """
    Returns a version of L with the first occurence of num removed.
    """
    if L == []:
        return L
    if L[0] == num:
        return L[1:]
    return [L[0]] + remove_first(L[1:], num)



def remove_all(L: List[int], num: int) -> List[int]:
    """
    Returns a version of L with all occurences of num removed.
    """
    if L == []:
        return L
    if L[0] == num:
        return remove_all(L[1:], num)
    return [L[0]] + remove_all(L[1:], num)



def remove_first_k(L: List[int], num: int, k: int) -> List[int]:
    """
    returns a version of L with the first k occurences of num removed.

    >>> L = [1,2,1,2,3]
    >>> remove_first_k(L, 1, 2)
        [2,2,3]

    >>> L = [1,2,1,2,3]
    >>> remove_first_k(L, 1, 1)
        [2,1,2,3]
    """
    if L == []:
        return []
    if k == 0:
        return L
    if L[0] == num:
        return remove_first_k(L[1:], num, k - 1)
    return [L[0]] + remove_first_k(L[1:], num, k)
    

    
def power_set(L: List[int]) -> List[List[int]]:
    """
    Returns the powerset of L.
    """
    if L == []:
        return [[]]
    head = L[0]
    tail = L[1:]
    return power_set(tail) + add_to_each(power_set(tail), head)



def add_to_each(L: List[List[int]], num: int) -> List[List[int]]:
    new = []
    for sub_list in L:
        new.append(sub_list + [num])
    return new



def sort(L: List[int]) -> List[int]:
    """
    Returns a sorted version of L.
    """
    if len(L) < 2:
        return L
    left = []
    right = []
    pivot = L[1:]
    head = L[0]
    for num in pivot:
        if num < head:
            left.append(num)
        else:
            right.append(num)
    return sort(left) + [pivot] + sort(right)



def hanoi(n, source, spare, target):
    if n == 1:
        print("Move from peg " + source + " to peg " + target)
    else:
        hanoi (n-1, source, target, spare)
        print("Move from peg " + source + " to peg " + target)
        hanoi (n-1, spare, source, target)
    
