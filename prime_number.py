# Finding prime numbers wihtin a range
def isPrime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
            break
    return True
for i in range(1, 25):
    if isPrime(i+1):
        print(i+1, sep = ' ')
print()
