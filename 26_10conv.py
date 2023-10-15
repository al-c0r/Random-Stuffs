Numbers="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

m = int(input("To convert a base 26 to base 10, press 1. \nOr press 2 if you want to convert a base 10 to base 26 number: "))

#Base26 t0 Base10 conversion...
if m==1:
	inp = input("Enter the alphabet (in CAPs) to convert base 26 to base 10 number: ")
	out1 = 0
	inp1 = ""
	j = 0
	while j<len(inp): #Loop which extracts integral part of number
		if inp[j]==".":
			break
		else:
			inp1 = inp1 + inp[j]
		j = j+1
	for i in range(len(inp1)):
		out1 = out1 + Numbers.find(inp1[len(inp1)-i-1])*26**i

	j = 0
	inp2 = ""
	out2 = 0
	while j<len(inp): #Loop which extracts fractional part of number
		if inp[j]==".":
			for k in range(j+1,len(inp)):
				out2 = out2 + Numbers.find(inp[k])*26**(-k)
			break
		j = j+1
	print("The number in base 10 is", out1+out2)

#Base10 t0 Base26 conversion...
else:
	n = float(input("Enter the number that you wanted to converted to Base 26: "))
	m = n - int(n)
	out1=""
	out2=""
	out3 = ""
	#Loop for extracting integral part of number
	while(int(n)!=0):
		out1 = out1 + Numbers[int(n)%26]
		n = int(int(n)/26)

	for i in range(len(out1)):
		out2 = out2 + out1[len(out1)-i-1]

	#Loop for extracting fractional part of number
	a = int(input("No. of decimal number to be returned while converting: "))
	i = 0
	while i<a+1:
		m = m*26
		out3 = out3 + Numbers[int(m)%26]
		m = m-int(m)
		i = i+1
	out = out2+"."+out3
	print("The number in base 26 is", out)
