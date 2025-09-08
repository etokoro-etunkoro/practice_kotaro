import collections
queue = collections.deque()

def bfs(i, root):
    while queue:
        yield root[i]
        if i < (len(root) >> 1):
            left = (i << 1) + 1
            if root[left] is not None:
                queue.append(left) 
            
            right = (i << 1) + 2
            if root[right] is not None:
                queue.append(right)

root = list(map(int, input().split()))
print(list(bfs(0, root)))