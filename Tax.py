print("Hello, how are you\nWhat is your name")
user=input(" ")
print('Please enter the price of your bicycle: ')
cost=int(input(' '))
if cost >=100000:
    tax=(15/100)*cost
    print("You are to pay 15% : ", + tax)
elif cost >50000 and cost <100000:
    tax=(10/100)*cost
    print("You are to pay 10% : ", + tax)
elif cost <=50000 and cost>10000:
    tax = (5/100)*cost
    print('Kindly pay 5% which is' ,+ tax)
else :
    print ('invalid Error')
         
