# 완전탐색 - 모음사전
from itertools import product

words = ['A', 'E', 'I', 'O', 'U']
word = "AAAAE"
dic = set()

for idx in range(len(words)):
    for comb in product(words, repeat = idx + 1):
        dic.add(''.join(comb))

dic = sorted(dic)
print(dic.index(word) + 1)