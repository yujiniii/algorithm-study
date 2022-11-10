def p110():
# 4-1-1 상하좌우
# 시뮬레이션 유형: 일련의 명령에 따라 개체를 차례대로 이동
  n=int(input())
  x,y = 1,1
  plans = input().split()

  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  move_types = ['L','R','U','D']
  # (0,-1) : left-> list[a][b-1] 이기 때문에 x/y 축과는 반대
  for plan in plans:
    for i in range(len(move_types)):
      if plan == move_types[i]:
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<1 or ny<1 or nx>n or ny>n:
          continue
        x,y = nx,ny
  print(x,y)
def p113():
# 4-1-2 시각
# 하루는 86,400초로, 100,000의 경우의 수를 넘지 않으므로 그냥 문자열 연산 기
# 완전탐색: 가능한 경우의 수를 모두 검사해보는 탐색 방법
# 대충 100만개 이하로 탐색이 가능하면 완전탐색을 써도 된다
  h = int(input())
  count = 0
  for i in range(h+1):
    for j in range(60):
      for k in range(60):
        if '3' in str(i)+str(j)+str(k):
          count += 1
  print(count)
def p115():
# 4-2 왕실의 나이트
# 상하좌우와 유사, 나이트의 이동 경우의 수만 잘 파악하기
  input_data = input()
  row=int(input_data[1])
  col = int(ord(input_data[0]))-int(ord('a')) +1 # ASCII 이용

  steps = [(-2,1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
  result = 0
  for step in steps:
    next_low = row+step[0]
    next_col = col+step[1]
    if next_low>=1 and next_low<=8 and next_col >=1 and next_col<=8:
      result+=1
  print(result)
def p118():
# 4-3 게임 개발
# 전형적인 시뮬레이션
  n,m = map(int, input().split())

  d = [[0]*m for _ in range(n)] # 방문 처리를 위한 리스트
  x,y,dir = map(int,input().split())
  d[x][y] = 1 # 현재 좌표 방문처리

  array = [] # 전체 맵 정보
  for i in range(n):
    array.append(list(map(int,input().split())))
  # 북(-1,0) 동(0,1) 남(1,0) 서(0,-1)
  dx = [-1,0,1,0] 
  dy = [0,1,0,-1]

  def turn_left(): # 북동남서 반복
    nonlocal  dir  # 함수 밖에서 선언한 변수를 사용하기 위한 global/nonlocal keyword
    dir -= 1
    if dir == -1:
      dir = 3
  count = 1
  turn_time = 0
  while True:
    turn_left()
    nx = x+dx[dir]
    ny = y+dy[dir]
    if d[nx][ny] ==0 and array[nx][ny] == 0: # 방문하지 않은, 육지
      d[nx][ny] = 1
      x = nx
      y = ny
      count += 1
      turn_time = 0
      continue
    else: # 방문했거나, 바다일 때
      turn_time += 1
      
    if turn_time == 4: # 뒤로가기
      nx = x - dx[dir]
      ny = y - dy[dir]
      if array[nx][ny] == 0:
        x=nx
        y=ny
      else:
        break
      turn_time = 0
  print(count)