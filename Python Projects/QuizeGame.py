
print("\t\t\tQUIZE")
points = 0
player = input('Do you want to play : ')

def cor(points=None):
    print('Correct')

def wro():
    print('Wrong')

if player.lower() != 'yes':
    quit()
print('Ok lest Start\t\t')
#Question 1
question = input("No. of days in a Week \"tell in words\" : ")
if question.lower() == "seven":
    cor()
    points = points + 1
else:
    wro()
#Question 2
question = input("Number of oceans in the world \"tell in words\" : " )
if question.lower() == "four":
    cor()
    points = points + 1
else:
    wro()
#Question 3
question = input("Number of continents in the world \"tell in words\" : " )
if question.lower() == "seven":
    cor()
    points = points + 1
else:
    wro()
#Question 4
question = input("Number of wonders in the world \"tell in words\" : " )
if question.lower() == "seven":
   cor()
   points = points + 1
else:
   wro()
#Question 5
question = input("Capital of Tamil Nadu : " )
if question.lower() == "chennai":
    cor()
    points = points + 1
else:
    wro()

print('\tPoints = ',points,'/5')

