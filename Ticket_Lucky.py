#3) Дано чотирьохзначне число. Перевірити,чи є воно «щасливим квитком».
#Примітка: «щасливим квитком» називають число, в якому, при парній
#кількості цифр, сумма цифр його лівої половини рівна сумі цифр його
# правої половини. Наприклад, число 1322. Його ліва половина 13,
#а права 22, й воно є «щасливим квитком» (тому що  1 + 3 = 2 + 2).
ticket_num = int(input("Input four-digit ticket's number: "))
if 1000 > ticket_num or ticket_num >= 10000:
    print("Your number is NOT four-digit!")
else:
    num_one = ticket_num // 1000
    num_two = ticket_num % 1000 // 100
    num_three = ticket_num % 100 // 10
    num_four = ticket_num % 10 
    if num_one + num_two == num_three + num_four:
        print("Ticket is 'Lucky'!")
    else:
        print("Try again!")

