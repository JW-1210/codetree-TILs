n = int(input())

num = list(map(int,input().split()))
sum, sub, mul = map(int,input().split())

  
def func(depth, total, sum, sub, mul):
  global MIN, MAX
  if depth == n:
    MIN = min(total, MIN)
    MAX = max(total, MAX)

  if sum != 0:
    # print(sum)
    func(depth+1, total+num[depth], sum-1, sub, mul)
  if sub != 0:
    func(depth+1, total-num[depth], sum, sub-1, mul)
  if mul != 0:
    func(depth+1, total*num[depth], sum, sub, mul-1)

MIN,MAX = 10e8, -10e8
func(1, num[0], sum, sub, mul)
print(MIN, MAX)