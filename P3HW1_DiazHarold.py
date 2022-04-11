#P3HW1 - Debugging
#03/17/2022
#CTI-110
#Harold Diaz
#-------------------------------------------------------
#Take user input grade number and output a letter grade
#Configure grade scale to 10-point grading system
#Take user grade score
#Print user grade letter

def main():
   
    score = int(input('Please enter score: '))

    if score >= 90:
        print('Grade is A')
    elif score >= 80 and score < 90:
        print('Grade is B')
    elif score >= 70 and score < 80:
        print('Grade is C')
    elif score >= 60 and score < 70:
        print('Grade is D')
    elif score >= 0 and score < 60:
        print('Grade is F')


main()
