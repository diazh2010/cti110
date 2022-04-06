# CTI-110
# P2HW1 - Score List
# Harold Diaz 
# 04/05/2022
#
# Ask the user to enter the number of scores.
# Store the scores in a list, giving the list a descriptive name.
# Determine the lowest score and store in a variable.
# Drop lowest score from the list.
# Calculate score average after having dropped lowest score.
# Display (print) the following under "Results"
# Lowest score entered
# Score list after dropping lowest score
# Average of scores in modified list
# Determine Letter grade for calculated Average

list_of_scores=[]
i = 1
number_scores=int(input("How many scores do you want to enter?"))

while i <= number_scores:
    print('Enter score',f'#{i}: ',end='')
    entered_score = int(input())
    
    if entered_score <0 or entered_score >100:
        print('INVALID score')
        print('Score should be between 0 and 100')
        print('Enter score' ,f' #{i} again.')
    else:
       list_of_scores.append(entered_score)
       i += 1

    
lowest_score = min(list_of_scores)
modified_list = list_of_scores.remove(lowest_score)
average_score = sum(list_of_scores)/len(list_of_scores)

if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print('------------------Results-------------')
print('Lowest Score   :  ', lowest_score)
print('Modified List  :  ', list_of_scores)
print('Scores Average :  ', average_score)
print('Grade          :  ', grade)
print('--------------------------------------')

