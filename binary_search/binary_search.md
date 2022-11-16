## 순차탐색(Sequential Search)

리스트 안의 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
시간복잡도 O( _N_ )

```python
def sequential_search(n,target,array):
    for i in range(n):
        if array[i] == target:
            return i+1

input_data = input().spilt()
n=int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n,target,array))
```

# 이진 탐색

내부의 데이터가 정렬돼있어야 사용 가능  
시간복잡도 O(logN)  
시작점/끝점/중간점 이 존재한다

```python
# 재귀함수로 구현한 이진탐색 소스코드
def binary_seaarch(arr, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if arr[mid] == target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, mid-1, end)

n = # 원소의 개수
target = # 찾고자 하는 문자열
arr = # 전체 원소 / 정렬 필수

result = binary_search(arr, target, 0, n-1)
if result = None:
    print("원소가 존재하지 않습니다")
else:
    print(result)
```

```python
# 반복문으로 구현한 이진탐색 소스코드
def binary_seaarch(arr, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            return mid-1
        else:
            return mid+1
    return None

n = # 원소의 개수
target = # 찾고자 하는 문자열
arr = # 전체 원소 / 정렬 필수

result = binary_search(arr, target, 0, n-1)
if result = None:
    print("원소가 존재하지 않습니다")
else:
    print(result)
```

## 트리 자료구조

- 트리는 부모 노드와 자식 노드의 관계로 표현된다
- 트리의 최상단 노드를 루트 노드라고 한다
- 트리의 최하단 노드를 단말 노드라고 한다
- 트리에서 일부를 떼어내도 트리 구조이며, 이를 서브트리라 한다
- 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다

### 이진탐색트리

트리 자료구조 중 가장 간단한 형태

- 왼쪽 자식 노드 < 부모노드
- 부모 노드 < 오른쪽 자식 노드
