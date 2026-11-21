# 알고리즘 풀이 모음

파이썬으로 푼 프로그래머스·백준 위주 문제들을 유형별로 정리했습니다. 모든 스크립트는 표준 입력을 그대로 사용하므로, 예제 입력을 터미널에 붙여 넣거나 파일 리다이렉션(`python foo.py < input.txt`)으로 실행하면 됩니다.

## 디렉터리/파일 구조
- `exsearch-*.py` : 브루트포스 / 완전탐색 연습
- `greedy-*.py` : 탐욕법 패턴 정리
- `hash-*.py` : 해시·딕셔너리를 활용한 문제
- `sorting-*.py` : 정렬 및 우선순위 큐
- `stackQueue-*.py` : 스택/큐 및 데크 활용
- `test.py` : 즉석 실험용 스크립트
- `README.me` : 현재 문서

## 실행 방법
```bash
python exsearch-sol-03.py      # 원하는 스크립트를 지정해서 실행
python greedy-atm.py
```
필요 시 `pyenv`·`venv` 등을 사용해 Python 3.10 이상 환경을 맞춰 주세요.

## 풀이 요약
| 유형 | 파일 | 핵심 아이디어 |
| --- | --- | --- |
| 완전탐색 | `exsearch-arithmeticSequence.py` · `exsearch-blackjack.py` · `exsearch-combination.py` 등 | 모든 조합을 순회하면서 제약을 통과하는지 검사. 일부 스크립트는 DFS/백트래킹을 함께 사용. |
| 완전탐색(심화) | `exsearch-sol-01.py` ~ `exsearch-sol-07.py` | 브루트포스에 메모이제이션·가지치기를 더해 시간 복잡도를 낮춤. |
| 해시 | `hash-clothes.py`, `hash-defaultdict.py` | `dict`/`defaultdict`로 출현 빈도나 카테고리 조합을 빠르게 계산. |
| 정렬 | `sorting-h.py`, `sorting-k.py`, `sorting-mostLarge.py` | 커스텀 키 정렬, 파라메트릭 서치, 부분 배열 최대값 찾기 등의 패턴을 연습. |
| 그리디 | `greedy-atm.py`, `greedy-meeting.py` | 정렬 후 누적합/회의실 배정 같은 전형적인 탐욕 전략 구현. |
| 스택·큐 | `stackQueue-sol-01.py` ~ `stackQueue-sol-04.py` | 스택으로 괄호 검증, 큐/데크로 슬라이딩 윈도우·다중 프로세스 시뮬레이션 처리. |

## 앞으로 추가하고 싶은 것
1. 각 문제에 대한 링크/설명 주석 보강
2. `pytest` 기반 간단한 입출력 테스트 스위트
3. 카테고리별 README 서브섹션 + 난이도/태그 메타데이터

필요한 내용이 더 있다면 언제든지 업데이트할 예정입니다.
