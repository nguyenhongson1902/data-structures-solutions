# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def  build_tree(self):
                nodes = [[i] for i in range(self.n)] # O(n)

                for child_index in range(self.n): # O(n)
                        parent_index = self.parent[child_index]
                        if parent_index == -1:
                                root = child_index
                        else:
                                nodes[parent_index].append(nodes[child_index])
                
                return nodes[root]

        def height(self, tree):
                if len(tree) == 1:
                        return 1
                
                subtree_heights = []
                for i in range(1, len(tree)): # O(#subtrees)
                        subtree_heights.append(self.height(tree[i]))
                return 1 + max(subtree_heights)

        def compute_height(self):
                # Replace this code with a faster implementation
                # maxHeight = 0
                # for vertex in range(self.n):
                #         height = 0
                #         i = vertex
                #         while i != -1:
                #                 height += 1
                #                 i = self.parent[i]
                #         maxHeight = max(maxHeight, height);
                # return maxHeight;
                tree = self.build_tree() # O(n)
                return self.height(tree) # O(#subtrees)
        

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
