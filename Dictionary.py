#1
list1=[1,2,3,4,5,6]
list2= ['a','b','c','d','e']

dict1= {}
#dict1=dict1.fromkeys(list1,list2)
for i in range(len(list2)):
    dict1[list1[i]] = list2[i]
print(dict1)

#2
dict2 ={0:10,1:20}
dict2[2]=30
print(dict2)

#3
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50, 4:40}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

#4
dict5 = {0:"zero", 1:"one"}
print(2 in dict5)

#5
dict6={1:20,2:30,3:60}
print(sum(dict6.values()))
