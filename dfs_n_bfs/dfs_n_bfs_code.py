from collections import deque
def p149():
# 5-3 음료수 얼려먹기
# DFS
  n,m = map(int, input().split())
  graph = []
  for i in range(n):
    graph.append(list(map(int, input())))

  def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
      return False
    if graph[x][y] == 0:
      graph[x][y] = 1
      dfs(x-1,y)
      dfs(x,y-1)
      dfs(x+1,y)
      dfs(x,y+1)
      return True
    return False
  
  result=0
  for i in range(n):
    for j in range(m):
      if dfs(i,j) == True:
        result += 1
  print(result)

def p152():
# 5-4 미로 탈출
  n,m = map(int, input().split())
  graph = []
  for i in range(n):
    graph.append(list(map(int, input())))
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  def  bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
      x,y = q.popleft()
      for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m :
          continue
        if graph[nx][ny] == 0:
          continue
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y]+1
          q.append((nx,ny))
    return graph[n-1][m-1]
  print(bfs(0,0))
          
def p339():
# p.339 특정 거리의 도시 찾기
# n : 도시의 개수
# m : 도로의 개수
# k : 거리 정보
# x : 출발 정보
  n,m,k,x = map(int, input().split())
  graph = [[] for _ in range(n+1)]
  for _ in range(m):
    tmp1, tmp2 = map(int, input().split())
    graph[tmp1].append(tmp2)

  dis = [-1] * (n+1)
  dis[x] = 0 # 출발도시까지 거리
  
  queue = deque([x])
  while queue:
    v = queue.popleft() # now city
    # print(v, end=' ')
    for i in graph[v]: # now 와 연결된 next city
      if dis[i] == -1: # visited==False
        queue.append(i)
        dis[i] = dis[v]+1

  check = False
  for i in range(1, n+1):
    if dis[i] == k:
      print(i)
      check = True

  if check == False : 
    print(-1)
      
      