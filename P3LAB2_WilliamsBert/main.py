user_choice= ['Oil change', 'Tire rotation', 'Car wash']
user_entered=input('Enter desired auto service:')

if 'Oil change' in user_entered:
    print('\nYou entered: Oil change')
    print('Cost of oil change: $35')
    
elif 'Tire rotation' in user_entered:
    print('\nYou entered: Tire rotation')
    print('Cost of tire rotation: $19')
    
elif 'Car wash' in user_entered: 
    print('\nYou entered: Car wash')
    print('Cost of car wash: $7')
    
else:
    print('\nYou entered:',user_entered)
    print('Error: Requested service is not recognized') 
