tpl1=(10.5,3.5,4.6,7.8) #float tuple
print(tpl1)

tpl2=('vera','joy','michael') #string tuple
print(tpl2)

tpl3=(True,False) #boolean tuple
print(tpl3)

tpl4=('1','2','3','4','5')#int tuple
print(tpl4)

tpl5=(1,'2',3.0,True) #Heterogenous tuple
print(tpl5)

tpl6=()
print(tpl6)

print(type(tpl6))

tpl7=10.5,3.5,4.6,7.8
print(tpl7)

tpl8='vera','joy','michael'
print(tpl8)

tpl9=True,False
print(tpl9)

tpl10='1','2','3','4','5'
print(tpl10)

tpl11=1,'2',3.0,True #Heterogenous tuple
print(tpl5)

#INDEXING
print(tpl11[0]) #first index tuple using +ve indexing
print(tpl11[-4]) #last index using -ve indexing

print(tpl11[3]) #last index using +ve indexing
print(tpl11[-1]) #last index using -ve indexing

print(tpl11[1]) #second index using +ve indexing
print(tpl1[-3]) #second index using -ve indexing

#Deleting
del tpl10  #delete tpl10

#Conversion
tpl12=tuple('!Sabi Programmers') #convert string to tpl
print(tpl12)

tpl13=tuple(['Sabi Programmers']) #convert list to tpl
print(tpl13)

tpl14=tuple({1,2,3,4,5,6}) #convert set to tuple
print(tpl14)

tpl15=tuple({1:'one',2:'two'}) #convert dict to tuple

#Operators
print(tpl1+tpl3) #+ operator
print(tpl4*4) #* operator
print(tpl2[1:3]) #slicing
print(2.4 in tpl3) #in operator
print(2.4 not in tpl3) #not in operator

