## 시간초과

보통 반복문을 통해 입력을 받을 때에는 그냥 input으로는 시간초과가 나는 경우가 많음

```python
import sys

input = sys.stdin.readline

```

을 추가한다.  
`sys.stdin.readline` 사용 시 개행문자가 포함되기 때문에 처리해줘야한다.

```python
import sys

input = sys.stdin.readline

n = int(input())
data = [input().rstrip() for i in range(n)]

```
