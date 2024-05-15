from collections import deque
import heapq


def bfs(grid, n):
    dist = [[float('inf')] * n for _ in range(n)]
    q = deque()

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                dist[r][c] = 0
                q.append((r, c))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist


def safest_path(grid):
    n = len(grid)
    dist = bfs(grid, n)

    pq = [(-dist[0][0], 0, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while pq:
        safeness, r, c = heapq.heappop(pq)
        safeness = - safeness

        if r == n - 1 and c == n - 1:
            return safeness

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                heapq.heappush(pq, (-min(safeness, dist[nc][nr]), nr, nc))

    return 0


if __name__ == '__main__':
    grid = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]]
    print(safest_path(grid))
