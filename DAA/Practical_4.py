def fractionalKnapsack(W, arr):
    # Sorting items based on the profit-to-weight ratio in descending order
    arr.sort(key=lambda x: x[0] / x[1], reverse=True)

    # Result (value in the knapsack)
    finalvalue = 0.0

    # Print the table header
    print(f"{'Item':>8} {'Value':>8} {'Weight':>8} {'Taken':>8} {'Remaining Weight':>20}")
    print("-" * 60)

    # Looping through all items
    for i, (profit, weight) in arr:
        if weight <= W:
            taken_weight = weight
            W -= weight
            finalvalue += profit
            print(f"{i + 1:>8} {profit:>8.2f} {weight:>8.2f} {taken_weight:>8.2f} {W:>20.2f}")
        else:
            taken_weight = W
            finalvalue += profit * W / weight
            print(f"{i + 1:>8} {profit:>8.2f} {weight:>8.2f} {taken_weight:>8.2f} {0.00:>20.2f}")
            break

    return finalvalue

if __name__ == "__main__":
    W = int(input("Enter the total capacity of the knapsack: ")) 
    n = int(input("Enter the number of items: "))  
    
    arr = []

    for i in range(n):
        print(f"\nEnter profit and weight for item {i+1}:")
        profit = int(input("Profit: "))
        weight = int(input("Weight: "))
        arr.append((profit, weight))

    # Function call
    max_val = fractionalKnapsack(W, arr)
    print(f"\nMaximum value in the knapsack = {max_val:.2f}")
