while True:
    message = int(input('Choose one of these numbers: 1-2-3 '))
    match message:
        case 1:
            num1 = int(input('Enter the first number: '))
            num2 = int(input('Enter the second number: '))
            result1 = num1 ** num2
            print(f'The result of {num1} raised to the power of {num2} is: {result1}')
            break
        case 2:
            frstName = input('Enter your first name: ')
            lastName = input('Enter your last name: ')
            print(f'********** {frstName} {lastName} **********')
            break
        case 3:
            numm1 = float(input('Enter the first number: '))
            numm2 = float(input('Enter the second number: '))
            result3 = numm1 * numm2
            print(f'The result is: {result3}')
            break
        case _:
            print('Invalid choice. Please choose a number between 1 and 3.')
