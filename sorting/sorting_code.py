def p178():
    # 6-2 위에서 아래로
    n = int(input())

    array = []
    for i in range(n):
        array.append(int(input()))

    array = sorted(array, reverse=True)

    for i in array:
        print(i, end=' ')


def p180():
    # 6-4 성적이 낮은 순서로 학생 출력하기
    # (이름, 점수) 으로 묶은 후 점수에 대해 sort 수행
    n = int(input())

    array = []
    for i in range(n):
        input_data = input().split()
        array.append((input_data[0], int(input_data[1])))  # (이름, 점수)

    array = sorted(array, key=lambda stu: stu[1])

    for s in array:
        print(s[0], end=' ')


def p182():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break
    print(sum(a))
