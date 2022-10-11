name = input('Please enter your name: ')
score = int(input('Please enter your score: '))

if score >= 70:
    print(name+'\'s score is '+str(score)+' Hence '+name+' gets A')
    #print(f"{name}'s score is {score} Hence {name} gets A")

elif score >= 60 and score < 70:
    print(name+'\'s score is '+str(score)+' Hence '+name+' gets B')
    #print(f"{name}'s score is {score} Hence {name} gets B")

elif score >= 55 and score < 60:
    print(name+'\'s score is '+str(score)+' Hence '+name+' gets C')
    #print(f"{name}'s score is {score} Hence {name} gets C")

elif score >= 50 and score < 55:
    print(name+'\'s score is '+str(score)+' Hence '+name+' gets D')
    #print(f"{name}'s score is {score} Hence {name} gets D")

elif score >= 45 and score < 50:
    print(name+'\'s score is '+str(score)+' Hence '+name+' gets E')
    #print(f"{name}'s score is {score} Hence {name} gets E")

else:
    print(name+'\'s score is '+str(score)+' Hence '+name+' gets F')
    #print(f"{name}'s score is {score} Hence {name} gets F")
