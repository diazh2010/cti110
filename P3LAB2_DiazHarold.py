req_service = input('Enter desired auto service:\n')
print('You entered:', req_service)

if req_service == 'Oil change':
    print('Cost of oil change: $35')
elif req_service == 'Tire rotation':
    print('Cost of tire rotation: $19')
elif req_service == 'Car wash':
    print('Cost of car wash: $7')
else:
    print('Error: Requested service is not recognized')