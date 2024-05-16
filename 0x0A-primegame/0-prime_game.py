#!/usr/bin/python3

"""Check if a number is prime."""


def is_prime(num):
    """Check if a number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


"""Generate prime numbers up to a given limit."""


def calculate_primes(n):
    """Generate prime numbers up to a given limit.

    Args:
        n (int): The upper limit.

    Returns:
        list: A list of prime numbers up to n.
    """
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes


"""Determine the winner of the Prime Game."""


def isWinner(x, nums):
    """Determine the winner of the Prime Game.

    Args:
        x (int): The number of rounds.
        nums (list): An array of n for each round.

    Returns:
        str: The name of the player who won the most rounds.
             None if the winner cannot be determined.
    """
    winners = {"Maria": 0, "Ben": 0}

    """Iterate over the rounds"""
    for n in nums:
        """Calculate prime numbers up to n"""
        primes = calculate_primes(n)

        """Determine the winner of the round based on the number of primes"""
        if len(primes) == 0 or len(primes) % 2 == 0:
            winners["Ben"] += 1
        else:
            winners["Maria"] += 1

    """Determine the player with the most wins"""
    if winners["Maria"] > winners["Ben"]:
        return "Maria"
    elif winners["Maria"] < winners["Ben"]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
