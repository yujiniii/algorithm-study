def p197_ver01():
    # 7-2 부품찾기
    # 이진탐색으로 풀기
    def binary_search(arr, target, start, end):
        while start <= end:
            mid = (start+end)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid-1  # 타겟이 현재보다 작으니까 왼쪽 확인== end 떙기기
            else:
                start = mid+1  # 타겟이 현재보다 크니까 오른쪽 확인 == start 밀기

        return None

    n = int(input())  # 가게의 부품 개수
    arr = list(map(int, input().split()))  # 가게에서 보유한 부품 번호
    arr.sort()

    m = int(input())  # 손님의 부품 개수
    x = list(map(int, input().split()))  # 확인 요청한 부품 번호

    for i in x:
        result = binary_search(arr, i, 0, n-1)
        if result != None:
            print("yes", end=' ')
        else:
            print("no", end=' ')


def p197_ver02():
    # 7-2 부품 찾기
    # 계수 정렬로 풀기
    n = int(input())
    arr = [0] * 1000001  # 비교할 m(손님 부품의 개수) 최대값 크기의 배열

    for i in input().split():
        arr[int(i)] = 1  # 가게에서 보유한 부품 번호 인덱스에 1

    m = int(input())
    x = list(map(int, input().split()))

    for i in x:
        if arr[i] == 1:
            print("yes", end=' ')
        else:
            print("no", end=' ')


def p197_ver03():
    # 7-2 부품 찾기
    # set()으로 중복 제거하여 확인하기
    n = int(input())
    array = set(map(int, input().split()))  # set() 자료형으로 중복 제거

    m = int(input())
    x = list(map(int, input().split()))

    for i in x:
        if i in array:
            print("yes", end=' ')
        else:
            print("no", end=" ")


def p201():
    # 7-3 떡볶이 떡 만들기
    # 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제 :  파라메트릭 서치
