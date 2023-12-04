n = int(input())
client = list(map(int,input().split()))
head, crew = map(int,input().split())

# print(client)
cnt = n
for i in range(n):
    client[i] -= head
    while client[i] > 0:
        client[i] -= crew
        cnt += 1

print(cnt)