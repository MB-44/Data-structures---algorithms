# None - optiaml it mean not using DP
# highest run complexity - O(n^2)
def minSubArray(array):
    if len(array) == 0:
        return 0    
    minSum = float("inf")
    for i in range(len(array)):
        for j in range(i+1,len(array)+1):
            subArray = array[i:j]
            minSum = min(minSum,sum(subArray))
    return minSum

# Optimal solution using DP
def minSubArray(array):
    if len(array) == 0:
        return 0
    minSumUsingElement = array[0]
    minSum = array[0]

    for i in range(1,len(array)):
        num = array[i]
        currentMin = min(num,num+minSumUsingElement[i-1])
        minSumUsingElement.append(currentMin)
        minSum = min(minSum,currentMin)
    return minSum