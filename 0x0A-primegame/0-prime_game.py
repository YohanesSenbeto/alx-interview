#!/usr/bin/python3


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def calculate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def isWinner(x, nums):
    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = calculate_primes(n)
        if len(primes) == 0 or len(primes) % 2 == 0:
            winners["Ben"] += 1
        else:
            winners["Maria"] += 1

    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Maria"] < winners["Ben"]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner:", isWinner(3, [4, 5, 1]))
