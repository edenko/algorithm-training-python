# 프로그래머스 - 완주하지 못한 선수

# 마라톤에 참여한 선수들의 이름이 담긴 participant와 완주한 선수들의 이름이 담긴 completion이 주어져.
# 단 한 명의 선수만 완주하지 못했어. 그 선수의 이름을 반환해.
# dict 또는 Counter를 사용해서 평균 O(N)에 해결해 봐. 정렬은 사용하지 말자.

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# 정답: "leo"

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]

# 정답: "mislav"

def solution(participant, completion):
    dic = {}
    
    for part in participant:
        dic[part] = dic.get(part, 0) + 1
        
    for com in completion:
        dic[com] -= 1 # 참가자가 모두 등록했다는 조건이 있어서
    
    for k, v in dic.items():
        if v > 0:
            return k

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))