def palindrome(s) -> bool:
    return str(s) == str(s)[::-1]


def freq(s: str) -> dict:
    result = {}
    for char in s:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1
    return result


def prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    pass
