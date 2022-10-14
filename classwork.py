nums=[1,5,20,60,200,2] #adding a list
sumtotal=0
for num in nums:
    sumtotal +=num
print(sumtotal)

nums=[1,5,20,60,200,2] #adding a list
print(sum(nums))


nums=[1,5,20,60,200,2] #multiplying a list
multotal=1
for num in nums:
    multotal *=num
print(multotal)

nums=[1,5,20,60,200,2] #highest number in a list
print(max(nums))

nums=[1,5,20,60,200,2] #highest 
nums=nums
largest=0
for num in nums:
    if num > largest:
        largest=num
print(largest)

nums=[1,5,20,60,200,2]
print(nums[-1])

nums=[1,5,20,60,200,2]
print(min(nums))

nums=[1,5,20,60,200,2]
smallest=0
for num in nums:
    if num > smallest:
        smallest=num
print(smallest)

nums=[1,5,20,60,200,2]
smallest=max(nums)
for num in nums:
    if num < smallest:
        smallest=num
print(smallest)

str_list=['abc','xyz','aba','1221']
count=0
for i in str_list:
    if len(i) >= 2:
        if i[0]== i[-1]:
            count += 1
print(count)
        





