# def find_smallest(arr):
#     return min(arr)

# arr = list(map(int, input().strip("[]").split(',')))
# print(find_smallest(arr))

# def find_largest(arr):
#     return max(arr)

# arr = list(map(int, input().split()))
# print(find_largest(arr))

# def second_smallest_largest(arr):
#     unique_arr = sorted(set(arr))
#     if len(unique_arr) < 2:
#         return -1, -1  # Not enough elements
#     return unique_arr[1], unique_arr[-2]

# arr = list(map(int, input().strip("[]").split(",")))
# print(second_smallest_largest(arr))


# def reverse_array(arr):
#     return arr[::-1]

# arr = list(map(int, input().split()))
# print(reverse_array(arr))

# def rearrange_inc_dec(arr):
#     arr.sort()
#     mid = len(arr) // 2
#     return arr[:mid] + arr[mid:][::-1]

# arr = list(map(int, input().split()))
# print(rearrange_inc_dec(arr))

# from collections import Counter

# def frequency_count(arr):
#     return dict(Counter(arr))

# arr = list(map(int, input().split()))
# print(frequency_count(arr))

# def rotate_array(arr, k):
#     k = k % len(arr)  # Handle cases where k > length
#     return arr[k:] + arr[:k]

# arr = list(map(int, input().split()))
# k = int(input())
# print(rotate_array(arr, k))


# def remove_duplicates_sorted(arr):
#     return list(set(arr))  # Preserves order

# arr = list(map(int, input().split()))
# print(remove_duplicates_sorted(arr))

# from collections import Counter

# def find_repeating_elements(arr):
#     count = Counter(arr)
#     return [num for num in count if count[num]==1]

# arr = list(map(int, input().split()))
# print(find_repeating_elements(arr))
