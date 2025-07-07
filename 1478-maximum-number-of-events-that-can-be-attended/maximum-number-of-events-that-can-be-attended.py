class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        event_heap = []
        day = 0
        i = 0
        res = 0
        n = len(events)

        while i < n or event_heap:
            if not event_heap:
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heapq.heappush(event_heap, events[i][1])
                i += 1

            while event_heap and event_heap[0] < day:
                heapq.heappop(event_heap)

            if event_heap:
                heapq.heappop(event_heap)
                res += 1

            day += 1

        return res
