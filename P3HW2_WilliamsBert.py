#Calculate Pizza price using if and else statements
#CTI-110 P3HW2 Pizza Order
#Bert Williams
#April 11, 2022
#
#*****************Pseudocode********************
# Display "Please enter number of students"
# Input number of students
# Display "Please enter number of students sharing a pizza"
# Input number of students sharing a pizza of either 1.5, 2, 3
# If statement 1.5 continue to calculation
# elif statement 2 continue to calculation
# elif statement 3 continue to calculation
# else statement not in within if statemnet
# Display "INVALID ENTRY!!!", "Should have entered 1.5, 2, or 3", "Run Program again"
# Set pizza price= pizza number*5
# Set tax=pizza price*.06
# Set total price=pizza price + tax
# Display "-------Pizza order-----"
# Display "Number of students"
# Display "Pizzas Needed"
# Display "Price"
# Display "-----------------------"
#************************************************

print('Please enter number of students.')
guest_num= int(input())

print('Please enter number of students sharing a pizza.')
guest_piz= float(input())

if guest_piz== 1.5:
    pizza_num=(guest_num/ guest_piz)
elif guest_piz== 2:
    pizza_num=(guest_num/ guest_piz)
elif guest_piz== 3:
    pizza_num=(guest_num/ guest_piz)
else:
     print('INVALID ENTRY!!!')
     print('Should have entered 1.5, 2, or 3')
     print('Run Program again')
     exit()
za_price= pizza_num*5
tax= za_price*.06
price= za_price+ tax
print('------Pizza Order------')
print('Number of Students:', format(guest_num,'.2f'))
print('Pizzas Needed:',format(pizza_num,'.2f'))
print('Price $',format(price,'.2f'))
print('-----------------------')
