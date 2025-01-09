def largest_prime_factor_basic(n):
    i = 2
    largest_prime = 1
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 1
    if n > 1:
        largest_prime = n
    return largest_prime

number = 13195
largest_factor = largest_prime_factor_basic(number)
print(f"The largest prime factor of {number} is: {largest_factor}")

number = 600851475143
largest_factor = largest_prime_factor_basic(number)
print(f"The largest prime factor of {number} is: {largest_factor}")