def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor_optimized(n):
    largest_prime = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime

number = 13195
largest_factor = largest_prime_factor_optimized(number)
print(f"The largest prime factor of {number} is: {largest_factor}")

number = 600851475143
largest_factor = largest_prime_factor_optimized(number) #This will be slow
print(f"The largest prime factor of {number} is: {largest_factor}")