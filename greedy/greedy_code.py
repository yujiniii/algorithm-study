def p87():
# 3-1-1 거스름돈
# key: 가장 큰 화폐 단위부터 거슬러 주기
# 정당성: 동전간 서로 배수이기 때문에, 언제나 큰 화폐 단위를 사용하는 것이 작은 화폐단위를 사용하는 것보다 효율적이다.
# 시간복잡도 O(n)
  n= 1260 # 거슬러야 할 총 금액
  count = 0
  coin_types = [500, 100, 50, 10]
  
  for coin in coin_types:
    count += n // coin
    n%= coin
  print(count)


def p92():
# 3-2 큰 수의 법칙
# 이해 : n개의 리스트, m개를 골라 더하는 수 중 가장 큰 수 만들기
# 단, 인덱스는 "연속"해서 k번을 더할 수 없음 
# key: 가장 큰 수를 K 번 더하고 두번째로 큰 수를 한번만 더하고를 반복
  n,m,k = map(int, input().split())
  data = list(map(int, input().split()))
  
  data.sort()
  first = data[n-1]
  second = data[n-2]
#---------------------EZ-----------------
  cnt = m
  result = 0
  while True:
    for i in range(k):
      if cnt == 0:
        break
      result += first
      cnt-=1
    if cnt==0:
      break
    result += second
    cnt-=1
  print("method 1 : ", result)
#----------------------HARD------------- 
# 반복되는 수열의 점화식(규칙)을 찾아 계산하는 방법
# 가장 큰 수 (first) * k  + 두번째 큰 수(second) * 1 == (k+1)
# m//(k+1) : 수열의 반복 횟수
# m//(k+1) * k : first의 횟수
# m % (k+1)  : m이 k로 나누어 떨어지지 않을 때 남는 나머지

  # 가장 큰 수(first) 가 더해지는 횟수
  count = int(m/(k+1))*k # == m//(k+1) *k
  count += m % (k+1)  
  
  result = 0
  result += count*first
  result +=(m-count) * second
  print("method 2 : ",result)



def p96():
# 3-3 숫자 카드 게임
# key: 각 행마다 가장 작은 수를 찾은 뒤에, 그 수 중에서 가장 큰 수 찾기
  n,m = map(int, input().split())
  result1 = 0
  result2 = 0

  for i in range(n):
    data = list(map(int, input().split()))
#-----------------------------------------------min() 함수
    min_value1 = min(data)
    result1 = max(result1, min_value1)
#-----------------------------------------------2중 반복문
    min_value2 = 10002 # 나올수 없는 최대 수
    for a in data:
      min_value2 = min(min_value2, a)
    result2 = max(result2, min_value2)

  print("method 1 : ", result1)
  print("method 2 : ", result2)
def p99():
# 3-4 1이 될 때까지
# key : 최대한 많이 나누기
# (n이 k로 나눠떨어질 때 까지 1을 빼기) -> (n을 k로 나누기) 반복
  n,k = map(int, input().split())
  result1 = 0
  result2 = 0
#-------------------------------------EZ--------
  num = n
  while num>=k:
    while num%k != 0: # n이 k로 나눠떨어질 때 까지 1을 빼기
      num-=1
      result1+=1
    num//=k
    result1 +=1
  while num>1:
    num-=1
    result1 +=1
  print("method 1 :",result1)
#--------------------------------------HARD------
  while True:
    target = (n//k) *k
    result2 += (n-target)
    n=target
    if n<k:
      break
    result2 += 1
    n//=k
  result2 +=(n-1)
  print("method 2 :",result2)