# python3

import sys
import threading


def  build_tree(n, parents):
    nodes = [[i] for i in range(n)] # O(n)

    for child_index in range(n): # O(n)
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].append(nodes[child_index])
    
    return nodes[root]

def height(tree):
    if len(tree) == 1:
        return 1
    
    subtree_heights = []
    for i in range(1, len(tree)): # O(#subtrees)
        subtree_heights.append(height(tree[i]))
    return 1 + max(subtree_heights)


def compute_height(n, parents):
    # Replace this code with a faster implementation
    # Starter code, O(n^2)
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1: O(n)
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height

    # Faster implementation
    tree = build_tree(n, parents) # O(n)
    return height(tree) # O(#subtrees)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

# Time: O(n + #subtrees)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
