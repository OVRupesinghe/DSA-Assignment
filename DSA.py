# Implementation of Boyer Moore algorithm

from _collections import defaultdict


def shift_table(p):
    m = len(p)
    st = defaultdict(lambda: m)  # creates an empty dictionary which could be modified dynamically
    for k in range(m - 1):
        st[ord(p[k])] = m - k - 1  # ord : gets the unicode value of the given string
    return st


def horspool_algo(pattern, text):
    m = len(pattern)
    n = len(text)

    if m > n:
        return "Invalid entry"

    shiftTable = shift_table(pattern)
    k = m - 1

    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return 1

        k += shiftTable[ord(text[k])]




p = input("Enter a search string:")
file1 = open('modules.txt', 'r')
Lines = file1.readlines()
count = 0
for line in Lines:
    a = horspool_algo(p.casefold(),line.casefold())
    if a == 1:
        print(line)
        count += 1
print("Number of matches: ", count)
