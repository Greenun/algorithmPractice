def digits(n, k):
    string = ""
    while n < k:
        n, m = n // k, n % k
        string = str(m) + string
    print(string)

if __name__ == '__main__':
    digits(10, 2)