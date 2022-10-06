set1={1,2,3,4} #int set
print(set1)

set2={1.0,2.1,3.2,4.3} #float set
print(set2)

set3={'1','2','3','4'} #string set
print(set3)

set4={True,False,True,False} #boolean set
print(set4)

set5={1,2.1,'3',True} #heterogeneous set
print(set5)

set6=set() #empty set
print(set6)

print(type(set6))

set7={(12,57,43),1,2.4,'great'} #set of hashable
print(set7)

#Conversion
set8=set('Sabi Programmers') #convert string to set
print(set8)

set9=set(['Sabi Programmers']) #convert list to set
print(set9)

set10=set(('Sabi Programmer'))  #convert tuple to set
print(set10)

set11=set({1:'Sabi',2:'Programmers'}) #convert
print(set11)

#Set Methods
set12=set()
#add method
set12.add(20)
set12.add('christiana')
set12.add(True)
set12.add(40.123)
print('set 12 after updating: ',set12)

#Update method
set13={'Vera','Alex','Sola','Wumi'}
set12.update(set13)
print('set 13: ',set13)
print('set 13 after updating: ',set13)

#Or Operator
set14={1,2,3,4,5}
set15={4,5,6,7,8}
print(set14 | set15, 'using |')
print(set14 or set15,'using or')

#and operator
print(set14 & set15, 'using &')
print(set14 and set15,'using and')

#- Operator
print(set14-set15,'using set14 - set15')
print(set15 -set14,'using set15 - set14')

#^ Operator
print(set14 ^ set15,'using^')

#union method
print(set14.union(set15), 'using union')

#intersection
print(set14.intersection(set15),'using intersection')

#difference
print(set14.difference(set15),'using set14.difference')
print(set15.difference(set14),'using set15.difference')

#symmetric Difference
print(set14.symmetric_difference(set15),'using symmetric_difference')

#Copy method
set16=set3.copy()
print(set16)

#clear method
set3.clear()
print('set3: ',set3)
print('set16: ',set16)

#difference update
set14={1,2,3,4,5}
set15={4,5,6,7,8}
print('set14 before difference update: ',set14)
print('set15 before difference upadte: ',set15)
set14.difference_update(set15)
print('set14 after difference update: ',set14)
print('set15 after difference update: ',set15)

#Intersection
set14={1,2,3,4,5}
set15={4,5,6,7,8}
print('set14 before intersection update: ',set14)
print('set15 before intersection update: ',set15)
set15.intersection_update(set14)
print('set14 after intersection update: ',set14)
print('set15 after intersection update: ',set15)

#symmetric _difference update
set14={1,2,3,4,5}
set15={4,5,6,7,8}
print('set14 before symmetric_difference update: ',set14)
print('set15 before symmetric_difference upadte: ',set15)
set15.difference_update(set14)
print('set14 after symmetric_difference update: ',set14)
print('set15 after symmetric_difference update: ',set15)

#discard method
set14.discard(4)

#Remove method
print(set15.remove(6))

#issubset method
set17={1,2}
print(set17.issubset(set14))

#isdisjoint method
set18={20,30}
print(set18.isdisjoint(set14))

#pop method
print('popped value: ',set16.pop())
print('new set16: ',set16)



