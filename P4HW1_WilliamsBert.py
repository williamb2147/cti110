#Loop program the creates a score list with program altercations.
#Bert Williams
#CTI-110
#April 29, 2022
#
#********Pseuodo Code*********
# Ask doe number of scores user want to enter
# Create empty list
# Collect scores
# Evaluate entry
# Find lowest score
# Drop Lowest score from list
# Calculate average
# Determine letter grade fro average
# Display results
#*****************************


num_scores=int(input('How many scores do you want to enter?(Enter at least 2):'))
scores=[]

for num in range(1, num_scores +1):
    score=float(input('Enter score #'+str(num)+':'))
    while score < 0 or score > 100:
        print('INVALID Score entered!!!!\nScore should be between 0 and 100:')
        score=float(input('Enter score #'+str(num)+':'))
    scores.append(score)

final_scores= scores
lowest_score=min(final_scores)
final_scores.remove(lowest_score)
score_average=sum(final_scores)/len(final_scores)

if score_average >= 90:
    grade= 'A'
elif score_average >= 80:
    grade= 'B'
elif score_average >= 70:
    grade= 'C'
elif score_average >= 65:
    grade= 'D'
else:
    grade ='F'


print('------Results------')
print('Lowest Score:',lowest_score)
print('Modified List:',final_scores)
print('Score Average:',score_average)
print('Grade        :',grade)
print('--------------------')
