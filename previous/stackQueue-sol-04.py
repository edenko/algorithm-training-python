# 스택/큐 - 주식가격
def solution(prices = [3, 5, 2, 6, 7, 8, 1, 10, 9]):
    arr = [0 for i in prices]

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            arr[i] += 1
            if prices[i] > prices[j]:
                break

    return arr

solution()
