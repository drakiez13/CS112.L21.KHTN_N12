class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    def isEmpty(self):
        return len(self.queue) == 0
  
    def insert(self, data):
        self.queue.append(data)
  
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[max][0]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

def core(Graph, n):

    a, b, k = map(int, input())

    queue = PriorityQueue()
    queue.insert((0, a))
    visited = set()
    count = 0
    while not queue.isEmpty():
        t, v = queue.delete()
       
        if t > k:
            break
        if v == b:
            if t == k:
                count += 1
            continue
        for u, w in Graph[v]:
            if (v, u) not in visited:
                queue.insert((w + t, u))
                visited.add((u, v))

    if count == 0:
        print(-1)
    else:
        print(count)


n, m = map(int, input())
graph = []
for i in range(n):
    A = []
    graph.append(A)
for i in range(m):
    u, v, w = map(int, input())
    graph[u].append((v, w))
    graph[v].append((u, w))
core(graph, n)