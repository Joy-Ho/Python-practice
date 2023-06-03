def multiply(n1, n2):
    return n1*n2

value = multiply(3, 4)
print(value)


def calculate(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

print(calculate(10))