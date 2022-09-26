name = input("Enter your Name: ")
email = input("Enter your Email: ")
mobile = input("Enter your mobile: ")
city = input("Enter your City: ")

#nested if-else
if len(name) > 1:
    if '@' in email and len(email) > 11:
        if len(mobile) == 10 and mobile.isnumeric():
            if city in ['Lucknow', 'Delhi', 'Noida']:
                print("Your data is saved, Thankyou")
            else:
                print('We are not available in your city')
        else:
            print('Invalid mobile number')
    else:
        print('Invalid email address')
else:
    print('Ye kaisa naam hai')

