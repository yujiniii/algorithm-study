def p217():
    # 8-2 1로 만들기
    # d : 각 인덱스가 1이 되기 위한 연산 횟수가 들어 있음
    # 따라서 d[i]에서 -1,/2,/3,/5 를 했을때 d에 저장된 연산 횟수가 가장 작은걸 구하는 거
    # 근데 d[i]에서 -1,/2,/3,/5 로 찾아가는거 자체가 연산이기 때문에 +1 해줘야함
    # min(d[i-1], d[i/2], d[i/3], d[i/5]) + 1

    x = int(input())

    d = [0] * 30001  # dp 테이블

    for i in range(2, x+1):
        d[i] = d[i-1]+1
        if i % 2 == 0:
            d[i] = min(d[i], d[i//2]+1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i//5]+1)
    print(d[x])


def p220():
    # 8-3 개미 전사
    # d: 개미 전사가 선택한 번호에서 얻을 수 있는 식량의 최대값
    # i를 털면 i-2를 털 수 있고 i-1을 털면 i-2랑 i를 못 턴다
    # max(arr[i]+d[i-2], d[i-1])
    n = int(input())

    arr = list(map(int, input().split()))

    d = [0] * 100  # DP table
    d[0] = arr[0]
    d[1] = max(arr[0], arr[1])
    for i in range(2, n):
        d[i] = max(d[i-2]+arr[i], d[i-1])
    print(d[n-1])


def p223():
    # 8-4 바닥공사
    # 796796 으로 나눈 나머지를 구할 것 -> 수가 커지는 것을 방지 (DP인거 눈치까기)
    n = int(input())

    d = [0] * 1001

    d[1] = 1
    d[2] = 3
    for i in range(3, n+1):
        d[i] = (d[i-1] + (2 * d[i-2])) % 796796
        # print(i, ' : ', d[i], " = ", d[i-1], "+ 2 *", d[i-2])

    print(d[n])
