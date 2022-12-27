def isprime(number):
    for i in range(2,number):
        if number%i==0:
            return 0
    return 1

n=int(input("Enter the number:"))
print(isprime(n))
