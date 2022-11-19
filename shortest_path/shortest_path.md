# 최단경로(Shortest Path)

가장 짧은 경로를 찾는 알고리즘  
길 찾기 문제라고도 불림  
보통 최단경로를 모두 구하는건 X, 최단 거리는?? 이런식으로 나온다함

## 다익스트라(dijkstra) 최단 경로 알고리즘

그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘  
그리디 알고리즘 _(가장 비용이 적은 노드를 선택)_ 에 포함  
음의 간선이 없을 때 정상적으로 동작

> **음의 간선??**  
> 0보다 작은 값을 가지는 간선, GPS소프트웨어의 기본 알고리즘

1. 출발 노드를 설정한다
2. 최단 거리 테이블을 초기화한다.
   > **최단 거리 테이블**  
   > 각 노드에서 현재까지의 최단 거리를 보관하는 1차원 리스트
3. (현재 노드 기준으로) 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
5. 위 과정에서 `3` 과 `4` 를 반복한다.

```python
# 간단하게 다익스트라 알고리즘 구현하기
# 시간복잡도 O(V^2)로, 추천하지 않는 방식
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]

visited = [false] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())  # a->b 비용 c
    graph[a].append((b,c))

# 방문하지 않은 근처 노드 중 최단거리 노드 찾기
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i]<min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = 0
    for j in graph[start]:
        distance[j[0]] = j[1]  # 최단거리 테이블
        # distance[현재 기준 연결 노드] = 현재 기준 연결 노드까지 거리
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now]+j[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리
            if cost<distance[j[0]]: # 현재 위치에서 다음 노드까지의 거리가 cost보다 크면?
                distance[j[0]] = cost # 해당하는 다음 노드에 cost 담기

dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1,n+1):
    if distance[i]:
        print("INFINITY")
    else:
        print(distance[i])

```

```python
# heapq를 이용해 구현한 다익스트라 알고리즘
# 시간복잡도 O(ElogV) E:간선개수, V:노드개수
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())  # a->b 비용 c
    graph[a].append((b,c))

    def dijkstra(start):
        q = []
        heapq.heappush(q,(0,start)) # (거리, 인덱스)
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리
                if cost<distance[i[0]]:
                    distance[i[0]]=cost
                    # 해당하는 다음 노드에 cost 담기
                    heapq.heappush(q, (cost,i[0]))
                    # 다음에 방문하기 위해 heapq에 추가하기

dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1,n+1):
    if distance[i]:
        print("INFINITY")
    else:
        print(distance[i])

```

## 프로이드 워셜 알고리즘

모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우  
모든 노드에 대해서 다른 모든 노드로 가는 최단거리를 2차원 리스트에 보관  
다이나믹 프로그래밍 알고리즘에 포함  
시간복잡도 O(N^3)

> 점화식 : D_ab = min(D_ab, D_ak+D_kb)

```python
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신-> 자기자신 은 0으로 초기화
for a in range(1,  n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

# 간선에 대한 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

# 점화식 수행하기
for k in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 수행된 결과물 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINTY", end=' ' )
        else:
            print(graph[a][b], end=' ')
    print()
```
