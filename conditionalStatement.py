
#writing a function about verifying the age before letting enter in the club
def firstCondition(age):
    #checkinf if the age below 16, then print message1
    if(age<16):
        print('you cannot enter, you are just a kid')
    # checkinf if the age below 16, then print message1
    elif(age>16 and age<21):
        print('you are soon to be adult, show me ID and you can enter')
    # checkinf if the age below 16, then print message1
    else:
        print('welcome to the club, enjoy your time')

firstCondition(12)
firstCondition(19)
firstCondition(31)

