import math

data = [2, 4, 4, 4, 5, 5, 7, 9]

n = len(data)
mean = sum(data) / n

variance = sum((x - mean) ** 2 for x in data) / n #Population variance

#Sample Variance
sample_variance = sum((x-mean)**2 for x in data) / (n-1)

std_dev = math.sqrt(variance) #Population Standard Deviation
sample_std_dev = math.sqrt(sample_variance) #Sample Standard Deviation


print(f"Manually calculated Population Standard Deviation: {std_dev}")
print(f"Manually calculated Sample Standard Deviation: {sample_std_dev}")
