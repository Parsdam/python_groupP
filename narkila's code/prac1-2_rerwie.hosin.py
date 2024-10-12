def is_prime (num):
    if num > 0:
        if  num == 2 or num == 3:
            return True # 2 and 3 are prime numbers so it should be true
        elif num > 3:
            for i in range(4, (num ** 0.5)+1 , 2):#https://youtu.be/dl7LLYw-xbQ whatch this if u have questions XD and num ** 0.5 == math.sqrt(num) == num power 1\2
                
                """the end of a for is not inclusive and we want to check the square root itself 
                The range function generates a sequence of numbers starting from 3 up to, but not including, int(num**0.5) + 1. The +1 is there to ensure that the square root of num is included in the range.

                Here's why:

                int(num**0.5) gives the integer part of the square root of num.
                Without the +1, the range would stop at int(num**0.5) - 1, which might exclude the square root itself if it's an integer.
                By adding +1, we ensure that the range includes the square root, even if it's an integer.
                For example, if num = 25, then int(num**0.5) = 5. Without the +1, the range would be range(3, 5), which would only include 3 and 4, but not 5. By adding +1, the range becomes range(3, 6), which includes 5.

                If you delete the +1, the code would still work for most cases, but it would fail for perfect squares (e.g., num = 25, num = 36, etc.). In these cases, the square root would be excluded from the range, and the function might incorrectly return True for non-prime numbers.
                """

                if num % i == 0:
                    return False

                    """ for is inclucive 
                    for i in range(1, 6):  # note the 6 instead of 5
                    print(i)
                    ==> 1,2,3,4,5  not 6 but 1 is included
                    thats y i started with 4 cuz we already checked 3
                    """
        else:
            print("a -numbers and 1 cant be prime")

def sum_digits(temp_number):
    sum_digits = 0
    while temp_number > 0:
        sum_digits += temp_number % 10
        temp_number //= 10
    print(f'sum of digits is: {sum_digits}')
def main():
    num = int(input('enter a even int number: '))
    sum_digits(num)

    if is_prime(num):
        print(f"the number {num} is a prime number")
    else:
        print(f"the number {num} is not a prime number")

if __name__ == '__main__':
    main()