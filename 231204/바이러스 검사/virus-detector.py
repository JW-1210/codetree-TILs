n = int(input())
client = list(map(int,input().split()))
head, crew = map(int,input().split())

# print(client)
cnt = n
for i in range(n):
    client[i] -= head
    if client[i] <= 0:
        continue
    else:
        client[i] -= crew
        cnt += 1

print(cnt)