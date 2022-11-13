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
