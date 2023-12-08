from itertools import combinations
from pprint import pprint

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

# n/2 만큼의 조합 구하기
work_combi = list(combinations(range(n), n//2))
# print(work_combi)
work = []
for i in range(len(work_combi)//2):
  # print(work_combi[i],work_combi[len(work_combi)-1-i])
  work.append([work_combi[i],work_combi[len(work_combi)-1-i]])
# print(work)

result = 999

# #work 좌표 set 마다 차 구하기
for i in work: #[(0, 1, 2), (3, 4, 5)]]
  # print(i[0])
#   sum = 0
  for morning, night in zip([i[0]], [i[1]]):
    # print(morning)
  #   print(morning, night)
    #자표 콤비네이션 구하기
    morning_temp = list(combinations(morning,2))
    night_temp = list(combinations(night, 2))

    # print(morning_temp)

    m_sum = 0
    n_sum=0
    for x,y in morning_temp:
      # print(x,y)
      m_sum += arr[x][y] + arr[y][x]
    
    for x,y in night_temp:
      n_sum += arr[x][y] + arr[y][x]

    # # result = abs(m_sum - n_sum)

    result = min(result, abs(m_sum - n_sum))
print(result)