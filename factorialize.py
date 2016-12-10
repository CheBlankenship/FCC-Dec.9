# Factorialize a Number

def factorialize(num):
    result = 1
    for i in range(1,num+1):
        result *= i

    return result
print factorialize(5)
