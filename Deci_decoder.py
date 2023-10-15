inp = input("Enter the binary string that you want to decode: ")
num_str = ""
ls = []

#converting string and storing as a number in list
for i in range(len(inp)):
	if inp[i]==" ":
		for j in range(1,9):
			num_str = num_str + inp[i+j]
		ls.append(int(num_str))
		num_str = ""

deci = 0
decimal = []

#converting number to base 10
for i in range(len(ls)):
	for j in range(len(str(ls[i]))):
		if str(ls[i])[len(str(ls[i]))-j-1]=="0":
			x = 0
		elif str(ls[i])[len(str(ls[i]))-j-1]=="1":
			x = 1
		deci = deci + x*2**j
	decimal.append(deci)
	deci = 0

#Using ASCII code align character with decimal code
message = ""
for i in range(len(decimal)):
	message = message + chr(decimal[i])

print("The encoded message in binary is:", message)
