import heapq

h = []
heapq.heappush(h, [20, "taro"])
heapq.heappush(h, [5, "jiro"])
print(h[0][1])
heapq.heappop(h)
heapq.heappush(h, [10, "saburo"])
heapq.heappush(h, [15, "shiro"])
print(h[0][1])
