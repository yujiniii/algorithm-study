## **탐색**

많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

### **표기**

- **인접행렬 방식**  
  각 노드가 연결된 형태를 기록
  ```python
  INF = 999999999
  [
    [0, 7, 5]  # node 0 에 대해 node 1, 2 의 거리
    [7, 0, INF], # node 1 에 대해 node 0, 2 의 거리
    [5, INF,0]  # node 2 에 대해 node 0, 1 의 거리
  ]
  ```
  노드 개수가 많을수록 불필요한 메모리 낭비  
  <br>
- **인접 리스트 방식**  
  연결된 노드에 대한 정보를 기록

  ```python
  graph = [[] for _ in range(3)] # 행이 3개인 2차원 리스트

  graph[0].append((1,7)) # node 0 에 연결된 (노드, 거리)
  graph[0].append((2,5)) # node 0 에 연결된 (노드, 거리)

  graph[1].append((0,7))  #node 1 에 연결된 (노드, 거리)

  graph[2].append((0,5))  #node 2 에 연결된 (노드, 거리)

  print(graph) # [[(1,7),(2,5)], [(0,7)], [(0,5)]]
  ```

  정보를 얻는 속도 느림
  <br>

# DFS

Depth-first Search (깊이우선탐색)  
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘  
데이터 개수가 N 개일 때 O(N) 시간 소요

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 입적 노드가 이씨으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. `2`번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
def dfs(graph, v , visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)


graph = [...] # 인접 리스트 방식으로 구현된 graph
visited = [false] * len(graph) # 방문처리, 노드의 개수만큼 만들기
v = 1 # 시작위치, 재귀를 진행하며 현재위치로 변경됨
dfs(graph, v, visited)
```

# BFS

breadth-first Search(너비우선탐색)  
가까운 노드부터 탐색하는 알고리즘  
데이터 개수가 N 개일 때 O(N) 시간 소요 _(DFS 보다 조금 빠르다)_

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노도의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. `2`번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

```python
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v=queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [...] # 인접 리스트 방식으로 구현된 graph
visited = [false] * len(graph) # 방문처리, 노드의 개수만큼 만들기
v = 1 # 시작위치
bfs(graph, start, visited)

```

<br><br><br>

<hr>

> ### **자료구조**
>
> 데이터를 표현하고 관리하고 처리하기 위한 구조
>
> #### **스택**
>
> LIKE 박스쌓기  
> 선입후출 구조, 후입선출 구조
>
> ```python
> stack = []
> stack.append(1) #push
> stack.pop() # pop
> ```
>
> #### **큐**
>
> LIKE 대기 줄  
> 선입선출 구조
>
> ```python
> from collections import deque
>
> queue = deque()
> queue.append(1) # PUSH
> queue.popleft() # POP
> ```
>
> #### **재귀함수**
>
> 자기자신을 다시 호출하는 함수
>
> ```python
> def recursive():
>    print("재귀함수를 호출합니다")
>    recursive()
>
> recursive()
> ```
