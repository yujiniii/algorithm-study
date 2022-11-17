# 다이나믹 프로그래밍

동적 계획법이라고도 함  
메모리 공간을 조금 더 사용하면서 연산 속도를 비약적으로 올리는 방법  
시간복잡도 O(N)

**조건**

1. 큰 문제를 작은 문제로 나눌 수 있다
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

> #### 퀵 정렬(분할 정복 알고리즘)과의 차이점
>
> 분할 정복 알고리즘은 한번 분할되고 나면 pivot이 바뀌는 등의 일은 일어나지 않지만,
> 다이나믹 프로그래밍은 문제들이 서로 영향을 미치고 있다.

## 종류

### 하향식 / 탑다운(Top-Down)

메모이제이션이 여기 해당됨  
재귀함수를 이용하여 소스코드를 작성하는 방법  
큰 문제를 해결하기 위해 작은 문제를 호출한다는 뜻

### 상향식 / 보텀업(Bottom-Up)

반복문을 이용하여 소스코드를 작성하는 방법  
작은 문제부터 차근차근 답을 도출한다는 뜻  
재귀 함수 스택 크기가 제한돼있을 수도 있으니 보텀업 방식 권장

---

## 피보나치 수열로 동적계획법 이해하기

```python
# DP를 사용하지 않은 피보나치 수열
def fibo(x):
    if x==1 or x==2:
        return 1
    return fibo(x-1)+fibo(x-2)

print(fibo(4))
```

`fibo(n)` 에서 n이 커질수록 반복해서 호출하는 횟수가 많아진다. n=30 이라면 10억 가량의 연산을 수행해야 한다. (개오바)  
따라서 n에 따라 나오는 값이 고정되어 있다면 그것을 메모리에 저장해 필요할 때마다 불러오는 방식을 사용하게 된다.

```python
# DP를 사용한 피보나치 수열(Top-Down)
d = [0] * 100 # 계산된 결과를 저장하는 리스트 / 메모이제이션

def pibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x=2)
    return d[x]

print(pibo(99))
```

```python
# DP를 사용한 피보나치 수열(Bottom-Up)
d = [0] * 100 # 계산된 결과를 저장하는 리스트 / DP 테이블

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])

```