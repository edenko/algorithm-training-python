# 완전탐색 - 최소직사각형

# 1. 내부 배열을 정렬. 
# 2. 배열내부 인덱스끼리 비교해서 큰 수를 리턴.
# 3. 큰 수 두개를 x

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
mw, mh = 0, 0
for item in sizes:
    w, h = sorted(item)
    mw = max(mw, w)
    mh = max(mh, h)

print(mw * mh)