converter = input('What do you want to convert to:\nC for Celscius\nF for Fahrenheit\nEnter: ')
value = int(input('What is the value: '))

if converter.lower() == 'c':
    ans = (value - 32)* 5/9
    print(f"{value}F is {int(ans)}C")
    #print(str(value)+'F is '+str(int(ans))+'C')
elif converter.lower() == 'f':
    ans = (value * 9)/5 + 32
    print(f"{value}C is {int(ans)}F")
    #print(str(value)+'C is '+str(int(ans))+'F')
else:
    print('Invalid Input')
