import numpy as np


def compute_kmp_table(pattern):
    table = np.zeros((len(pattern),), dtype="i4")
    k = 0  # number of matched characters
    for i in range(1, len(pattern)):
        while k > 0 and pattern[i] != pattern[k]:
            k = table[k - 1]
        if pattern[i] == pattern[k]:
            k += 1
        table[i] = k
    return table


print(compute_kmp_table("ababaa"))
print(compute_kmp_table("gcagagag"))


def kmp_matcher(string, pattern):
    kmp_table = compute_kmp_table(pattern)
    positions = []
    n = len(string)
    m = len(pattern)
    k = 0  # number of matched characters
    for i in range(0, n):
        while k > 0 and string[i] != pattern[k]:
            k = kmp_table[k - 1]
        if string[i] == pattern[k]:
            k += 1
        if k == m:
            positions.append(i - m + 1)
            k = kmp_table[k - 1]
    return positions


print(compute_kmp_table("bbba"))
print(kmp_matcher("bbbabbbba", "bbba"))
