# 2667. 단지번호붙이기
# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
def BFS(r, c, color):
    # Q선언과 동시 담아두고 방문 체크
    Q = [(r,c)]
    visited[r][c] = color
    cnt = 0

    while Q:
        curr_r, curr_c = Q.pop(0)
        cnt += 1    # 방문했으니, 카운트
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            # 범위를 벗어나면 continue
            if nr<0 or nr>=N or nc<0 or nc>=N:continue
            # 갈 수 있다면
            if apt[nr][nc]==1 and visited[nr][nc] == 0:
                Q.append((nr,nc))
                visited[nr][nc] = color
    return cnt

def DFS(r,c):
    global home_count
    home_count += 1
    visited[r][c] = color

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 범위를 벗어나면 continue
        if nr<0 or nr>=N or nc<0 or nc>=N:continue
        # 갈 수 있다면
        if apt[nr][nc]==1 and visited[nr][nc] == 0:
            DFS(nr, nc)



# 단지 N*N
N = int(input())

apt = [list(map(int, input())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]

ans = []
color = 1
# 아파트 단지 전체 순회하면서 넘버링
for i in range(N):
    for j in range(N):
        if apt[i][j] == 1 and visited[i][j] == 0:
            # DFS
            home_count = 0
            tmp = DFS(i, j)
            ans.append(home_count)
            # # BFS
            # tmp = BFS(i, j, color)
            # ans.append(tmp)
            color += 1
            for a in visited:
                print(*a)
            print("-----------------------------------------")
            
print(len(ans))
for i in ans:
    print(i)