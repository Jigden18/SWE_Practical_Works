# Exercises for Students
# Modify the linear search function to return all indices where the target appears, not just the first one.
# Implement a function that uses binary search to find the insertion point for a target value in a sorted list.
# Create a function that counts the number of comparisons made in each search algorithm.
# Implement a jump search algorithm and compare its performance with linear and binary search.



# SOLUTION :

# Modify Linear Search to return all indices
def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)  # Add index if the target is found
    return indices if indices else -1  # Return -1 if the target is not found

# Test the modified function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 5)
print(f"Modified Linear Search: Indices of 5 are {result}")


# Implement function to find the insertion point for binary search
def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left  # left us the insertion point

# Test the function
sorted_list = [1, 2, 3, 4, 5, 6]
insertion_index = binary_search_insertion_point(sorted_list, 4)
print(f"Insertion Point for 4 in sorted list: {insertion_index}")


# Count comparisons in search algorithms
def linear_search_count(arr, target):
    indices = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            indices.append(i)
    return (indices if indices else -1), comparisons

def binary_search_count(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1, comparisons  # -1 if target is not in the list

def binary_search_recursive_count(arr, target, left, right):
    if left > right:
        return -1, 0  # 0 for no comparison
    
    mid = (left + right) // 2
    comparisons = 1  # Counting comparison
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        result, sub_comparisons = binary_search_recursive_count(arr, target, mid + 1, right)
        return result, comparisons + sub_comparisons
    else:
        result, sub_comparisons = binary_search_recursive_count(arr, target, left, mid - 1)
        return result, comparisons + sub_comparisons


# Implement Jump Search
import math

def jump_search(arr, target):
    n = len(arr)
    jump = int(math.sqrt(n))
    prev = 0

    while arr[min(jump, n) - 1] < target:
        prev = jump
        jump += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search for target in the block defined by prev and jump
    while arr[prev] < target:
        prev += 1
        if prev == min(jump, n):
            return -1

    if arr[prev] == target:
        return prev
    return -1

import time

# Compare performance of all search algorithms
def compare_search_algorithms_with_comparisons(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search_count(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search_count(arr_sorted, target)
    binary_time = time.time() - start_time
    
    # Jump Search
    start_time = time.time()
    jump_result = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time

    print(f"Linear Search: Found at indices {linear_result}, Time: {linear_time:.6f} seconds, Comparisons: {linear_comparisons}")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds, Comparisons: {binary_comparisons}")
    print(f"Jump Search: Found at index {jump_result}, Time: {jump_time:.6f} seconds")


# Create a Main Function
def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    sorted_test_list = sorted(test_list)
    print("Sorted list:", sorted_test_list)
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result, comparisons = linear_search_count(test_list, target)
    print(f"Linear Search: Found at indices {result}, Comparisons: {comparisons}")
    
    # Binary Search (iterative)
    result, comparisons = binary_search_count(sorted_test_list, target)
    print(f"Binary Search (iterative): Found at index {result}, Comparisons: {comparisons}")
    
    # Binary Search (recursive)
    result, comparisons = binary_search_recursive_count(sorted_test_list, target, 0, len(sorted_test_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}, Comparisons: {comparisons}")
    
    # Jump Search
    jump_result = jump_search(sorted_test_list, target)
    print(f"Jump Search: Found at index {jump_result}")

    # Compare performance
    print("\nPerformance Comparison with a large list:")
    compare_search_algorithms_with_comparisons(list(range(100000)), 99999)

if __name__ == "__main__":
    main()
