# CTI-110
# P2HW2 - Score Avg
# Harold Diaz 
# 03/02/2022
#
# Ask the user to enter a series of 7 scores individually.
# Store the scores in a list, giving the list a descriptive name.
# Determine the lowest score and store in a variable.
# Drop lowest score from the list.
# Calculate score average after having dropped lowest score.
# Display (print) the following under "Results"
# Lowest score entered
# Score list after dropping lowest score
# Average of scores in modified list

score_1 = float(input('Enter score #1:'))
score_2 = float(input('Enter score #2:'))
score_3 = float(input('Enter score #3:'))
score_4 = float(input('Enter score #4:'))
score_5 = float(input('Enter score #5:'))
score_6 = float(input('Enter score #6:'))
score_7 = float(input('Enter score #7:'))

list_of_scores = [score_1, score_2, score_3, score_4, score_5, score_6, score_7]
lowest_score = min(list_of_scores)
modified_list = list_of_scores.remove(lowest_score)
average_score = sum(list_of_scores)/len(list_of_scores)

print()
print()
print()
print('------------------Results-------------')
print('Lowest Score   :  ', lowest_score)
print('Modified List  :  ', list_of_scores)
print('Scores Average :  ', average_score)
print('--------------------------------------')

