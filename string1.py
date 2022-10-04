str1='My name is Vera' #assigning a single quote to str1
print(str1)
str2="My name is Vera" #assigning double quote to str2
print(str2)
str3='''My name is Vera''' #assigning triple quote to str3
print(str3)
str4="""My name is Vera""" #assigning triple double quote to str4
print(str4)

#MULTILINE STRING
str5= '''This is My
own Multi-line string
using single quote
''' #assigning tripple single quote multi-line to str5
print(str5)
str6="""This is My
second multi-line string
using double quote""" #assigning triple double quote to str6
print(str6)

#Quote in a quote
str7='Welcome to Engineer-D`s" Class' #including double quote in a single quote string
print(str7)
str8="Welcome to 'Engineer-D`s' class" #including single quote in double quote string
print(str8)

#String length and indexing
str9= 'Sabi Programmer'
print(len(str9)) #return length of str9

print(str9[0]) #return first index using +ve indexing
print(str9[-15]) #return first index using -ve indexing

print(str9[14]) #return last index using +ve indexing
print(str9[-15]) #return last index using -ve indexing

print(str9[7]) #return the 8th index using +ve indexing
print(str9[-8]) #return 8th index using -ve indexing

#String Conversion
print(str(100)) #converting an int to a string
print(str(12.2342)) #converting a float to a str
print(str(False)) #converting a boolean to a str

#Escape Sequences
str10='Welcome to \'Engineer-D`s\' Class' #escape sequence using single quote
print(str10)

str11= "Welcome to \"Engineer-D's\" Class" #escape sequence using double quote
print(str11)

str12= r'Welcome to \'Engineer-D\' Class' #ignoring escape sequence
print(str12)

str13='https:\\sabiprogrammers.org\\home' #escape sequence to include double backslash
print(str13)

str14='Including\tDistance' #include tab in a sentence
print(str14)

str15='Go to \nNext Line' #include newline
print(str15)

#String operators
str16= 'Catherine'
str17= 'Welcome'
print(str16+str17) #concatenating two strings
print(str16*3) #Kate how many times would i call you
print(str16[0:4]) #slicing
print(str16[5:9])
print('Kate' in str16) #check if kate is in str16
print('Back' in str17) #is back in str17
print('Kate' not in str16) #check if kate is not in str16
print('come' not in str17) #is come not in str17
