# CTI-110
# P4HW2 - Pizza Order
# Harold Diaz
# 4/6/2022
#Ask user for number of students they would like to order pizza for
#Ask user for number of people that will be sharing each pizza (1.5, 2, or 3)
#Depending on user input for number of people that will be sharing:
#Program is to calculate the number of whole pizzas user needs to buy
#Number of people sharing will dictate how many people per pizza
#Round pizzas up to whole pizza
#If user enters other value than 1.5, 2 or 3 students sharing, loop back to asking number of people that will be sharing.
#Advise they should have entered 1.5,2, or 3 and request input again.
#Otherwise, calculate price for number of pizzas needed assuming price per pizza is $5
#Calculate tax of 6%
#Finally, ask user to type "y" to run program again, or type anything else to quit.

def main():

    import math

    num_students = int(input('How many students do you want to order pizza for? '))
      
    while num_students >0:
        print('Enter number of people per pizza ( 1.5, 2, or 3): ', end='')
        num_sharing = float(input())
        if num_sharing == 1.5 or num_sharing == 2 or num_sharing == 3:
            num_pizzas = num_students / num_sharing
            rounded_pizzas = math.ceil(num_pizzas)
            subtotal = (rounded_pizzas * 5)
            tax = (subtotal * 0.06)
            total = (subtotal + tax)
            print()
            print('----Pizza Order-------')
            print('Number of Students:',num_students)
            print('Pizzas Needed:',rounded_pizzas)
            print('Price:',f'${total:.2f}')
            print('-----------------------')
            print('Would you like to run program again (y for yes):',end='')
            restart = input()
            if restart != 'y':
                break
            else:
                 main()

        else:
            print('INVALID ENTRY!!!!')
            print('Should have entered 1.5, 2, or 3')

main()
