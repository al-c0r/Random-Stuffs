def Fib(n):
	if n==0:
		return 0

	elif n==1:
		return 1

	else:
		return Fib(n-1) + Fib(n-2)

n = int(input("Please enter the cap of sequence to get Even Fibonacci sequence: "))
lst = []

for i in range(n):
	if Fib(i)%2==0:
		lst.append(Fib(i))
	else: pass
	print("The completion of code is", i*100/n, "%")

print("The sequence of Even Fibonacci is ", lst)
