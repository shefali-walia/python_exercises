
nums = [10, 21, 4, 45, 66, 93, 11]

evenCount = 0
oddCount = 0

for i in range(len(nums)):
    if nums[i]%2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print(f"Even numbers: {evenCount}")
print(f"Odd numbers: {oddCount}")