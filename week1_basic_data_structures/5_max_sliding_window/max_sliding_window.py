# python3
from collections import deque



# naive solution
# def max_sliding_window_naive(sequence, m):
#     maximums = []
#     for i in range(len(sequence) - m + 1):
#         maximums.append(max(sequence[i:i + m]))

#     return maximums

def max_sliding_window(sequence, m):
    """
    Reference: https://www.youtube.com/watch?v=DfljaUwZsOk&ab_channel=NeetCode
    """
    maximums = []
    d = deque([])
    l = r = 0

    while r < len(sequence):
        while d and sequence[d[-1]] < sequence[r]:
            d.pop()
        d.append(r)

        if l > d[0]:
            d.popleft()
        
        if r + 1 >= m:
            maximums.append(sequence[d[0]])
            l += 1
        
        r += 1
    
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

