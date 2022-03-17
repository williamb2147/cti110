#Program that will calculate the total number of scorers average
#CTI-110 P2HW1-Score Average
#Bert Williams
#March 16, 2022
#

#This program is to calculate the final results of the scores.
#It will find the Average, Lowest, and Create a modified list.
#The user enteries will allow the code to finalize the output.
#The score input will use the float to add decimal places.

print('Enter score #1:')
score1=float(input())

print('Enter score #2:')
score2=float(input())

print('Enter score #3:')
score3=float(input())

print('Enter score #4:')
score4=float(input())

print('Enter score #5:')
score5=float(input())

print('Enter score #6:')
score6=float(input())

print('Enter score #7:')
score7=float(input())

#The code below allows the calculations for the results.
#If you are to add new amount or delete the amount of scores above make sure to do the same to the final scores

final_scores=[score1,score2,score3,score4,score5,score6,score7]
lowest_score=min(final_scores)
final_scores.remove(lowest_score)
score_average=sum(final_scores)/len(final_scores)

#The print code below will produce the final output for the calculations above.
#If anything is to change make sure that the calculations match the results below.

print('------Results------')
print('Lowest Score:',lowest_score)
print('Modified List:',final_scores)
print('Score Average:',score_average)
print('--------------------')

      
