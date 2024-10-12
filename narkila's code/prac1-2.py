num = int(input('enter a even int number: '))

sum_dijits = 0
temp_number = num
while temp_number > 0:
    sum_dijits += temp_number % 10
    temp_number //= 10

print(f'sum of dijits is: {sum_dijits}')

is_prime = True
if num < 2:#2 is a prime number so it sould be num <= 2
    is_prime = False # 1 and 2 are prime numbers so it should be true
else:
    for i in range(2, int(num+1)):#num is int already y did u type cast it , and u can skip even numbers cuz thay are all non prime
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
