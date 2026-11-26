# 백준 1759 암호 만들기

# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 
# 또한 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 
# 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

# 새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 
# C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

# 첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 
# 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 
# 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

# 4 6
# a t c i s w

# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw

l, c = map(int, input().split())
words = sorted(list(map(str, input().split())))
path = []
vowels = ['a', 'e', 'i', 'o', 'u']

def dfs(x):
  if len(path) == l:
    vow = 0
    cons = 0

    for p in path:
      if p in vowels:
        vow += 1
      else:
        cons += 1

    if vow > 0 and cons > 1:
      print(''.join(path))
    return

  for i in range(x, c):
    path.append(words[i])

    dfs(i + 1)

    path.pop()

dfs(0)
