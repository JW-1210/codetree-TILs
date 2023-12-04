n = int(input())
client = list(map(int,input().split()))
head, crew = map(int,input().split())

# print(client)
cnt = n
for i in range(n):
    client[i] -= head
    if client[i] <= 0:
        continue
    cnt += client[i] // crew
    if client[i] % crew >0:
        cnt += 1
        
print(cnt)