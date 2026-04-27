def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []   

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            result[prev] = i - prev

        stack.append(i)

    return result


temperatures = list(map(int, input("Enter temperatures: ").split()))
result = daily_temperatures(temperatures)
print("Output:", result)