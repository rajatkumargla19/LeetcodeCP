class Solution:
    def countPrimes(self, n: int) -> int:
        sieve=[i for i in range(0,n)]
        count=0
        for i in range(2,int(n**(0.5)+1)):
            if sieve[i]>0:
                for j in range(i**2,n,i):
                    if (j%i)==0 and sieve[j]>0:
                        # print(sieve[j])
                        # There is no need to traverse the complete sieve arr for counting the positive prime numbers, purpose of this question is to count and the same can be the done at the each step using this count variable..
                        count+=1
                        sieve[j]*=(-1)
        # count_primes=0
        # # print(sieve)
        # for i in range(2,n):
        #     if sieve[i]>0:
        #         count_primes+=1
        # return count_primes

        return n-count-2 if n-count-2>0 else 0



                


            
        
        