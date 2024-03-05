
def age():
    global currentYear
    global birthYear
    birthYear = 2020
    currentAge =  currentYear - birthYear
    print(f'Your age is {currentAge}')

currentYear = int(input('Current year:'))
birthYear = int(input('Birth year:'))

age()
print(birthYear)

