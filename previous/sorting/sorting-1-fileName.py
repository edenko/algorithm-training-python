# 파일명 정렬

# 문자열로 된 파일명이 주어진다.
# 각 파일명은 다음 3부분으로 이루어진다.

# HEAD + NUMBER + TAIL

# HEAD: 문자로 이루어짐 (대소문자 구분 ❌)
# NUMBER: 숫자 (1~5자리)
# TAIL: 나머지 (정렬에 영향 없음)

# 👉 정렬 기준은 다음과 같다.

# 1️⃣ HEAD 기준 사전순 (대소문자 구분 없이)
# 2️⃣ HEAD가 같으면 NUMBER 기준 숫자 오름차순
# 3️⃣ HEAD, NUMBER가 모두 같으면 입력 순서 유지 (stable)

def solution(files):
    def head(file):
        string = ''

        for x in file:
            if x.isdigit():
                break
            else:
                string += x

        return string.lower()

    def number(file):
        num = ''
        is_str = False

        for x in file:
            if x.isdigit():
                num += x
                is_str = True
            elif is_str:
                break

            if len(num) == 5:
                break
        
        return int(num)

    files.sort(key=lambda x: (head(x), number(x)))
    return files

sol = solution(
    files = [
        "img12.png", "img10.png", "img02.png",
        "img1.png", "IMG01.GIF", "img2.JPG"
    ]
)
print(sol) # ['img1.png', 'IMG01.GIF', 'img02.png', 'img2.JPG', 'img10.png', 'img12.png']
