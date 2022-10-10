#З клавіатури ввести шестизначне число. Перевірити, чи є воно паліндромом.

number = int(input("Input six-digit number: "))
if 100000 > number or number >= 1000000:
    print("Your number is NOT six-digit!")
else:
    num_one = number // 100000
    num_two = number % 100000 // 10000
    num_three = number % 10000 // 1000
    num_four = number % 1000 // 100
    num_five = number % 100 // 10
    num_six = number % 10 
    if num_one == num_six and num_two == num_five and num_three == num_four:
        print("Number ", number, " is a palindrome")
    else:
        print("Number ", number, " is NOT a palindrome")
