# Calculating Pizza Order26
# 2/7/2022
# CTI-110 P1HW2 - Pizza Order
# Harold Diaz

#3.)Ask user to enter number of students she/he would like to order pizza for: (X)
numofstudents = eval(input('How many students do you want to order pizza for?'))

#4.)Calculate how many pizza slices needed
#Number of Slices (Y) = X * 3
numofslices = (numofstudents * 3)

#5.)Calculate number of pizzas needed
#Number of Pizzas (Z) = Y / 6
numofpizzas = (numofslices / 6)

#6.)Display Information as follows:

#How many students do you want to order pizza for? ##
#----Pizza Order--------
#Number of Students : ##
#Pizza Slices Needed: ##
#Pizza Slices Needed: ##
#Pizzas Needed : ##
#--------------------------

print()
print('----Pizza Order--------')
print('Number of Students :', numofstudents)
print('Pizza Slices Needed:', numofslices)
print('Pizzas Needed:', numofpizzas)
print('--------------------------')
