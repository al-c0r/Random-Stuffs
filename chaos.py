list = []

file = open("Plot.txt", "w")

for m in range(1,100000):
	n = m
	count = 0
	while(n!=1):
		if n%2==0:
			n = n/2
			count += 1
			#print(n)
		elif n%2!=0:
			n = 3*n + 1
			count += 1
			#print(n)
		elif n==1:
			count += 1
			#print(n)
			break
	list.append(count+1)
	print("The length of ", m, "chaos is", count)
	file.write(str(m))
	file.write("\t")
	file.write(str(count))
	file.write("\n")
file.close()
print("The highest no. of the iterations so far made by this sequence of number in chaos is ", max(list))
