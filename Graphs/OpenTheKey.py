from collections import deque


def openTheKey(deadends, target):
    def neighbours(node):
        for i in range(4):
            x = int(node[i])
            for d in (-1, 1):
                y = (x + d) % 10
                yield node[:i] + str(y) + node[i + 1:]

    dead = set(deadends)
    queue = deque([('0000', 0)])
    visited = set('0000')

    if '0000' in dead:
        return -1

    while queue:
        node, depth = queue.popleft()
        if node == target:
            return depth
        for neighbour in neighbours(node):
            if neighbour not in visited and neighbour not in dead:
                visited.add(neighbour)
                queue.append((neighbour, depth + 1))

    return -1


if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = '0202'
    print(openTheKey(deadends, target))
