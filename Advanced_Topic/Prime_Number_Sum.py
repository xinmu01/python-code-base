def prime_sum(n):
	
        if n < 2:
                raise Exception("There is no prime number for this limit!")
	

        storage = []
        indicator = []
        for i in range(n):
                storage.append(i)
                indicator.append(1)
    
        primes = []
        start = 2

        done = False

        while not done:
                primes.append(start)
                ii = 2
                start_P = ii*start
                print (start_P)

                while start_P < n:
                        indicator[start_P] = 0
                        ii+=1
                        start_P = ii*start_P
		
                for i in range(start+1, n+1):
                        if indicator[i] == 1:
                                start = i
                                break

                if start != i:
                        done = True

        print(primes)
        return len(primes), sum(primes)

if __name__ == "__main__":
	n = input("Please enter a number which is larger than 1\n")
	n = int(n)
	print (prime_sum(n))


		


