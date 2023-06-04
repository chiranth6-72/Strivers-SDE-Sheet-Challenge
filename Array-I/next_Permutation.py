
#   ***  next_permutation : find next lexicographically greater permutation
# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).



# Optimal

def next_Permutation(arr: [int]):
    n = len(arr)
    idx = -1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            idx = i
            break
    
    if idx == -1:
        return arr.reverse()
    
    for i in range(n-1, idx, -1):
        if arr[i] > arr[idx]:
            arr[i], arr[idx] = arr[idx], arr[i]
            break
    
    arr[idx+1:] = reversed(arr[idx+1:])
    return arr

if __name__ == "__main__":
    arr =  [1,3,2]
    print(next_Permutation(arr))