#PRACTICE PROBLEM 3.3
#a)
year = eval(input('Enter the year:'))
if year%4==0 and (year%100!=0 or year%400==0):
    print('Could be a leap year')
else:
    print('Definitely not a leap year')
