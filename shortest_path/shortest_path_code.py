import heapq
import sys

def p259():
    # 9-2 미래도시
    # N 의 범위가 100이하로 시간이 넉넉하다
    # 1 -> ... -> K -> ... -> X 로 가는 최단거리 : 플로이드 워셜
    INF = int(1e9)
    n,m = map(int, input().split())
    graph = [[INF] * (n+1) for i in range(n+1)]

    for a in range(1,n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    for _ in range(m):
        a,b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    x,k = map(int, input().split())

    for k in range(1, n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    
    distance = graph[1][k] + graph[k][x]

    if distance>=INF:
        print("-1")
    else:
        print(distance)

def p262():
    # 9-3 전보
    # 한 도시에서 다른 도시까지의 최단거리 : 다익스트라 알고리즘
    input = sys.stdin.readline
    INF = int(1e9)
    
    n,m,start = map(int, input().split())
    graph = [[] for i in range(n+1)]
    distance = [INF]*(n+1)

    for _ in range(m):
        x,y,z = map(int, input().split())
        graph[x].append((y,z))

    def dijjkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now]<dist:
                continue
            for i in graph[now]:
                cost = dist+i[1]
                if cost<distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))
    dijjkstra(start)

    count = 0
    max_distance = 0
    for d in distance:
        if d!=INF: # 도달할 수 있는 노드 중에서 가장 멀리있는 노드와의 최단거리
            count+=1
            max_distance = max(max_distance,d) 

    print(count-1, max_distance)