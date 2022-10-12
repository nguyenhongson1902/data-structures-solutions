# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque([])

    def process(self, request):
        # write your code here
        if not self.finish_time: # if self.finish_time is empty
            self.finish_time.append(request.arrived_at + request.time_to_process)
            return Response(False, request.arrived_at)
        else:
            # self.finish_time = [time for time in self.finish_time if time > request.arrived_at] # doesn't pass, time limit exceeded. I guess the time complexity for this is O(S)
            
            # with the following implementation, we don't need to look for the elements that are greater than request.arrived_at to compare
            # it might be done in slower than O(S) time
            tmp = self.finish_time[0]
            while self.finish_time and tmp <= request.arrived_at:
                self.finish_time.popleft()
                if self.finish_time:
                    tmp = self.finish_time[0]

            print(self.finish_time)
            if len(self.finish_time) == self.size:
                return Response(True, -1)
            else:
                start_time = self.finish_time[-1] if self.finish_time else request.arrived_at
                self.finish_time.append(start_time + request.time_to_process)
            
        return Response(False, start_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests): # O(n)
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer) # Time slower than O(n.S)

    for response in responses: # Time O(S)
        print(response.started_at if not response.was_dropped else -1)

# Time complexity: < O(n.S)

if __name__ == "__main__":
    main()
