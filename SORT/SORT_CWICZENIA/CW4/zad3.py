from random import randint


def alloc(n):
    return [randint(0, 1000000000) for _ in range(n)]


def check_anagrams(word1, word2):
    counters = alloc(2 ** 16)
    for i in range(len(word1)):
        counters[ord(word1[i])] = 0

    for i in range(len(word1)):
        counters[ord(word1[i])] += 1
        counters[ord(word2[i])] -= 1

    for i in range(len(word1)):
        if counters[ord(word1[i])] != 0:
            return False
    return True