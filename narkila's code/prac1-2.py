num = int(input('enter a even int number: '))

sum_dijits = 0
temp_number = num
while temp_number > 0:
    sum_dijits += temp_number % 10
    temp_number //= 10

print(f'sum of dijits is: {sum_dijits}')

is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, int(num+1)):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
