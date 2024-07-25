# https://www.geeksforgeeks.org/problems/huffman-encoding3345/1
# Huffman Encoding


import heapq



from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffmanCodes(S, f, N):
    if N == 0:
        return []
    
    # Build the Huffman Tree
    min_heap = [Node(S[i], f[i]) for i in range(N)]
    heapq.heapify(min_heap)
    
    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(min_heap, merged)
    
    # Root of the Huffman Tree
    root = min_heap[0]
    
    # Generate Huffman Codes
    huffman_codes = {}
    
    def generate_codes(node, code):
        if node is not None:
            if node.char is not None:
                huffman_codes[node.char] = code
            generate_codes(node.left, code + '0')
            generate_codes(node.right, code + '1')
    
    generate_codes(root, '')
    
    # Collect codes in preorder traversal
    def preorder_traversal(node):
        codes = []
        if node is not None:
            if node.char is not None:
                codes.append(huffman_codes[node.char])
            codes.extend(preorder_traversal(node.left))
            codes.extend(preorder_traversal(node.right))
        return codes
    
    return preorder_traversal(root)

# Example usage:
S = "abcdef"
f = [5, 9, 12, 13, 16, 45]
print(huffmanCodes(S, f, len(S)))  # Output: ['0', '100', '101', '1100', '1101', '111']
