# 정렬

데이터를 특정한 기준에 따라서 순서대로 나열하는 것

`arr.sort(key=)` `sorted(arr)` : O(nlogn) 보장하는 머지정렬

## 선택 정렬(Selection Sort)

가장 작은 것을 선택하는 정렬  
시간복잡도 O(n^2)

1. 정렬되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞으로 보낸다.
2. `1`의 과정을 반복한다.

```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #swap

print(array)
```

## 삽입정렬(Insertion Sort)

데이터를 하나씩 확인하며 각 데이터를 적절한 위치에 삽입하는 정렬 방식  
데이터가 "거의" 정렬 돼 있을 때 효율적이다.  
정렬이 이루어진 원소는 항상 오름차순을 유지한다는 특징이 있다.
시간복잡도 O(n^2) , 최선의 경우 O(n)

1. 첫 번째 데이터는 그 자체로 정렬돼있다고 판단, 두번째 데이터를 첫번째 데이터와 비교해 올바른 위치에 삽입한다.
2. 그 다음 데이터를 가져와 정렬된 부분에서 올바른 위치를 찾아 삽입한다.
3. `2`의 과정을 반복한다.

```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)
```

## 퀵정렬(Quick Sort)

기준 데이터(pivot)을 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면서 진행하는 정렬 방식  
이미 데이터가 정렬되어있는 경우에는 느리게 동작한다.  
시간복잡도 O(nlogn) 최악의 경우 O(n^2)

> ### pivot 선택 및 분할 방식
>
> **호어 분할(Hoare Patition)**  
>  : 아래 설명과 같다. 평균적으로 swap을 3배이상 덜 발생시켜 유리하다.  
> **로무토 분할(Lomuto Patition)**  
>  : `i(index-1)` 와 `j(index)` 가 모두 증가하는 방식
> [참조](https://ldgeao99.tistory.com/376)

1. 리스트에서 첫 번째 데이터를 피벗으로 정한다
2. ㅤ  
   2-1. 왼쪽에서부터 피벗보다 큰 데이터를 찾는다.  
   2-2. 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
   2-3. 큰 데이터와 작은 데이터의 위치를 서로 교환해준다.
3. `2`의 과정이 끝나면 처음 정한 피벗을 기준으로 왼쪽엔 작은수, 오른쪽엔 큰 수가 위치하게 된다.( == 분할/파티션 )
4. 왼쪽 리스트와 오른쪽 리스트 각각에 대해 `1`, `2`를 수행한다.
5. `4`를 수행하며 분할된 리스트들에 대하여 다시 `1`, `2`를 수행한다.
6. 정렬이 끝날 때 까지 위 과정을 반복한다.

```python
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start>=end: # 원소가 1개일 때
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left<= end and array[left] <= array[pivot]:
            left+=1 # 피벗보다 큰 데이터를 찾았을 때
        while right>start and array[right] >= array[pivot]:
            right-=1 # 피벗보다 작은 데이터를 찾았을 때
        if left>right: # 작은 데이터/큰데이터 교체
            array[right],array[pivot] = array[pivot], array[right]
        else: # 작은 데이터/큰데이터 교체X
            array[right],array[left] = array[left], array[right]
        # 분할 이후 각각에서 정렬 수행
        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```

파이썬의 특징을 살려 좀 더 쉽게 구현할 수도 있다.

```python
array = [7,5,9,0,3,1,6,2,4,8]

def ez_quick(array):
    if len(array)<=1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return ez_quick(left_side) + [pivot] + ez_quick(right_side)

print(ez_quick(array))
```

## 계수 정렬(Count Sort)

데이터의 크기 범위가 제한되어, 정수 형태로 표현할 수 있을 때만 사용 가능

> 가장 큰 데이터 ~ 가장 작은 데이터 차이 < 1,000,000 일 때

시간복잡도 O(N+K)

1. 가장 큰 숫자 기준으로 모든 데이터가 담길 수 있는 리스트(배열)을 선언하고 0으로 초기화한다.
2. 데이터를 하나씩 확인하여, 등장하는 개수를 선언한 리스트에 적재한다.
3. 리스트에 적재된 숫자 개수에 맞게 리스트의 인덱스를 출력한다.

```python
array = [7,5,9,0,3,1,6,2,4,8]
count = [0] * (max(array)+1)
for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
```
