def optCost(freq, i, j, root):
    # Base cases 
    if j < i:  # no elements in this subarray
        return 0
    if j == i:  # one element in this subarray
        root[i][j] = i
        return freq[i]
    
    # Initialize the sum of frequencies in the range [i, j]
    fsum = sum(freq[i:j + 1])
    Min = float('inf')
    
    # One by one consider all elements as root and recursively find cost of BST
    for r in range(i, j + 1):
        cost = (optCost(freq, i, r - 1, root) + optCost(freq, r + 1, j, root))
        
        # Update minimum cost and store the root
        if cost < Min:
            Min = cost
            root[i][j] = r
    
    return Min + fsum

def printTree(root, i, j, keys, position="Root"):
    # Recursive function to print the structure of the Optimal BST
    if j < i:
        return
    # Get the root index for the current subarray
    r = root[i][j]
    
    print(f"{position}: {keys[r]}")
    
    # Print left subtree
    printTree(root, i, r - 1, keys, "Left Child of " + str(keys[r]))
    
    # Print right subtree
    printTree(root, r + 1, j, keys, "Right Child of " + str(keys[r]))

# Driver Code
if __name__ == '__main__':
    keys = [10, 12, 20, 40] 
    freq = [34, 8, 50, 12]
    n = len(keys)
    
    # Create a 2D array to store the root indices of the subtrees
    root = [[-1 for _ in range(n)] for _ in range(n)]
    
    # Compute the cost and store the root indices
    print("Cost of Optimal BST is", optCost(freq, 0, n - 1, root))
    
    # Print the structure of the Optimal BST
    print("\nStructure of Optimal BST:")
    printTree(root, 0, n - 1, keys)
