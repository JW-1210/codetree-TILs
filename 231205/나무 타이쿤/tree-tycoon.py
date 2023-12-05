# 격자크기, 키우는 햇수
n,m = map(int, input().split())
#리브로수 맵읽기
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))


#이동규칙 정의
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, 1, -1, 0, 1, 1, 1]

#특수 영양제 맵
init_visit = [[0 for _ in range(n)] for _ in range(n)]
init_visit[n-1][0], init_visit[n-2][0], init_visit[n-1][1], init_visit[n-2][1] = 1, 1, 1, 1
# print(visit, init_visit)

# # print(visit)

#특수 영양제 이동 함수 정의
def move(d, p):
  d = d-1
  visit = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      # visit[i][j] = 0
      if init_visit[i][j] == 1:
        # print(i,j)
        nx = (i + (p*dx[d])) %n
        ny = (j + (p*dy[d])) %n
        # print(j + (p*dx[d]), i + (p*dy[d]))
        # if nx > n-1:
        #   nx -= n
        # elif ny > n-1:
        #   ny -= n
        # elif nx < 0:
        #   nx += n
        # elif ny < 0:
        #   ny += n    
          
        visit[nx][ny] = 1
  return visit
  # print(visit)

def grow(visit):
  for i in range(n):
    for j in range(n):
      if visit[i][j] == 1:
        arr[i][j] += 1

def in_range(x, y):
  return 0 <= x and x < n and 0 <= y and y < n

def get_diag_cnt(x, y):
  cnt = 0
  global dx, dy
  for i, j in zip(dx[1::2], dy[1::2]):
      nx, ny = x + i, y + j
      if in_range(nx, ny) and arr[nx][ny] >= 1:
          cnt += 1
  
  return cnt

def diagonal_grow():
  for i in range(n):
    for j in range(n):
      if visit[i][j] == 1:
        cnt = get_diag_cnt(i, j)
        arr[i][j] += cnt    

#높이가 2 이상인 나무는 잘라내고 영양제 투입
def cut_tree():
  for i in range(n):
    for j in range(n):
      if arr[i][j] >=2 and visit[i][j] == 0:
        arr[i][j] -= 2
        visit[i][j] = 1
      elif visit[i][j] == 1:
        visit[i][j] = 0
  global init_visit
  init_visit = visit

#arr 합 구하기
def all_sum():
  cnt = 0
  for i in range(n):
    cnt += sum(arr[i])
  return cnt

#키움햇수 반복
for _ in range(m):
  #이동 규칙 읽기
  d, p = map(int, input().split())
  # print(d,p)
  visit = move(d,p)
  # print(visit)
  
  grow(visit)
  # print(visit)

  diagonal_grow()
  # print(visit)
  # print(arr)
  cut_tree()
  # print(arr)
  # print(visit)
cnt = all_sum()
print(cnt)