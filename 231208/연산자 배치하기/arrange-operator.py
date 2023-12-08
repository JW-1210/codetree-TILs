from itertools import permutations

n = int(input())
# eq = [0 for _ in range(n+(n-1))]
# print(eq)
num = list(map(int,input().split())) #['1', '5', '3']
func = ['+', '-', '*']
func_num = list(map(int, input().split()))
# print(func_num)
func_count = []

for i in range(len(func_num)):
  if func_num[i] == 1:
    func_count.append(func[i])
# print(func_count)

func_perm = list(permutations(func_count, n-1))
# print(func_combi)
# print(num[:-1])
max_result = -10e8
min_result = 10e8

for fp in func_perm:
  eq = []
  sum = num[0]
  # print(sum)
  for i,j in zip(num[1:], fp):
    # print(j, i)
    sum = eval(str(sum)+str(j)+str(i))
    # print(sum)
  max_result = max(sum, max_result)
  min_result = min(sum, min_result)
  
  if max_result >= 10e8:
    print(10e8)
  elif min_result <= -10e8:
    print(-10e8)
  else:
    print(min_result, max_result)
  # print(max_result, min_result)
    # print(i,j)
    
    # result = eval()
  



# print(num)

# for i in range(len(eq)):