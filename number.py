#INTEGERS
'''num1= 100 #Assigning a positive integer to num1
print(num1)

num2=-10 #Assigning negative integer to num2
print(num2)

#num3 = 1_000_000  #Seperating numbers with _
#print(num3)

print(type(num1), type(num2)) #printing the data type
num4=int(5.0345) #converting float to int
num5=int("100") #converting string to int
print(num4)
print(num5)

num6=int("100", 2) #converting string 100 to int base 2
print(num6)
num7=int("3234", 8) #converting string to int in base 8
print(num7)'''

#BINARY
num8=0b111101110101 #assigning binary number to num8
print(num8)
print(type(num8)) #printing out the type of variable
#num9=0b1_001_111_101 seperating binary with _
#print(num9) printing num9 to base 10

#OCTAL
num10= 0o12 #assigning octal number to num10
print(num10) #printing num10

num11= 0O12344567 #assigning oct to num11
print(num11) #printing num11 in base10

#HEXADECIMAL
num12=0x123Afde #assigning hex to num12
print(num12)
print(type(num12))
num13=0X1234567adefcb #assigning hex to num13
print(num13)

#FLOAT
num14=1.23356734 #assigning num14 to float
print(num14)
print(type(num14))

num15= -1234542.12456
print(num15)

#num16=123_234.732_357 #Seperating flaot with _
#print(num16)#

num17= 2e400 #exceeding memory size
print(num17)

num18= 1e3 #using scientific notation
print(num18)

num19= 3.14234232e3 #using scientific notation
print(num19)

#FLOAT CONVERSION
num20= float("5.5") #converting negative float string#
print(num20)

num21=float("5") #converting +ve int string to float
print(num21)

num22=float("        -5") #converting string
print(num22)

num23=float("1e3") #converting scientific notation
print(num23)

num24=float("-Infinity") #converting -Infinity to float
print(num24)

num25=float("inf") #converting inf to float
print(num25)



#ARITHMETIC OPERATIONS
num26=1500
num27=20
print(num26+num27) #addition
print(num26-num27) #subtraction
print(num26*num27) #multiplication
print(num26/num27) #division
print(num26%num27) #modulus prints out reminder
print(num26**num27) #exponent or power
print(num26//num27) #floor division
print(str(hex(num26))) #converting num26 to hex
print(str(oct(num26))) #converting 26 to oct
print(str(bin(num26))) #converting num26 to bin
print(pow(num27,3)) #num27^3
print(abs(-1245432)) #absolute
print(round(123.345678)) #round to nearest whole number
