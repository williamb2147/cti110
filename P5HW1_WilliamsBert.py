# Program that gives a simple math quiz.
# May 3, 2022
# CTI-110 P5HW2-Math Quiz
# Bert Williams
#
#**********Pseuodo Code***********
# Random function called
# Import radom numbers
# Define menu
# Add random numbers
# User guesses what they add up to
# OR subtract what they result
# Menu loops until option 3: Exit is chosen
#*********************************
#
#

def main():
    scores=[]
    option=0
    while option !=3:
        menu()
        option=int(input('Enter your option'))
        if option==1:
            scores=createScores(scores)
        elif option== 2:
            if len(scores)== 0:
                print('You need to create a list first.')
            else:
                lowest_score, final_score, score_average,grade=scores_to_grade(scores)
                print()
                print()
                print('------MENU------')
                print('lowest Scores:', lowest_score)
                print('Modified List:', final_score)
                print('Score Average:', format(score_average, '.2f'))
                print('Grade:', grade)
                print('------------------')
                print()
        elif option == 3:
            print('Exit Code')
        else:
            print('You have entered an invalid option!')
            print()
            
#////////////////////  Menu  ///////////////////////////////

def menu():
    print('[1]Create Score List')
    print('[2]Display Results')
    print('[3] Exit')
    
#//////////////////////  Score Input  /////////////////////////
    
def createScores(scores):
    num_scores=int(input('How many scores do you want to enter?(Enter at least 2):'))
    for num in range(1, num_scores +1):
        score=float(input('Enter score #'+str(num)+':'))
        while score < 0 or score > 100:
            print('INVALID Score entered!!!!\nScore should be between 0 and 100:')
            score=float(input('Enter score #'+str(num)+':'))
        scores.append(score)
    return scores


#/////////////    Option 2     ////////////////////////////////
    
def scores_to_grade(scores):
    final_score= scores
    lowest_score=min(scores)
    final_score.remove(lowest_score)
    score_average=sum(final_score)/len(final_score)
    
    if score_average>= 90:
        grade= 'A'
    elif score_average>=80:
        grade= 'B'
    elif score_average>=70:
        grade= 'C'
    elif score_average>=65:
        grade='D'
    else:
        grade= 'F'
    return final_score, lowest_score, score_average, grade

#//////////////////////   Main  ///////////////////////////////

if __name__=="__main__":
    main()
                
                
                    
                    
