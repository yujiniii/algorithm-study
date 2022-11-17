## 시간초과

보통 반복문을 통해 입력을 받을 때에는 그냥 input으로는 시간초과가 나는 경우가 많다

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

## 런타임 에러(recursion depth Error)

재귀함수의 스택 깊이 초과 에러  
dfs나 DP의 탑다운을 작성할 때 만날 수 있는 오류  
대부분이 파이썬의 재귀 최대 깊이의 기본 설정이 1,000회이기 때문에 그걸 임의로 늘려주면 된다

```python
import sys

sys.setrecursionlimit(10 ** 6) # pypy에선 불가능

```
