#Program that will calculate the total amount of purchaces (Receipt)
#March 16, 2022
#CTI-110 P2HW1-Total Purchases
#Bert Williams
#

print('Enter the price of item #1:')
user_item1=float(input())

print('Enter the price of item #2:')
user_item2=float(input())

print('Enter the price of item #3:')
user_item3=float(input())

print('Enter the price of item #4:')
user_item4=float(input())

print('Enter the price of item #5:')
user_item5=float(input())

user_subtotal=float(user_item1+user_item2+user_item3+user_item4+user_item5)
user_tax=float(user_subtotal*.07)
total=float(user_subtotal+user_tax)

print('------Results------')
print(f'{user_subtotal:.2f}')
print(f'{user_tax:.2f}')
print(f'{total:.2f}')

      
