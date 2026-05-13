def max_avg_subarray(arr, k):
    curr_sum = sum(arr[:k])
    best_sum = curr_sum

    for idx in range(k, len(arr)):
        curr_sum += arr[idx] - arr[idx - k]
        if curr_sum > best_sum:
            best_sum = curr_sum

    return best_sum / k


numbers = list(map(int, input("Enter array elements: ").split()))
window = int(input("Enter window length: "))

answer = max_avg_subarray(numbers, window)
print("Maximum average subarray:", answer)
