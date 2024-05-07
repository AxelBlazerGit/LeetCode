class Solution {
public:
    int countPrimes(int n) {

        //SIEVE OF ERATOSTHENES : :::::: : TIME COMPLEXITY=> N * ( LOG (LOG N) )

        // PSEUDO:
        //declare linear array with all flags as positive(primes)
        //negate 0 and 1 because they are not primes(not required)
        //start from 2 since  its first prime and keep incrementing ans as we encounter positives
        //once a positive is found negate all its multiples ("sieving" primes)
        //ans count is number of primes strictly less than n
        if (n <= 2) return 0;
        vector<bool> isPrime(n, true);
        // isPrime[0] = isPrime[1] = false;
        int ans=0;
        // Sieve of Eratosthenes 
        for (int i = 2; i < n; i++) {
            if (isPrime[i]) {
                ans++;
                for (int j = 2 * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        // int count = 0;
        // for (int i = 2; i < n; i++) {
        //     if (isPrime[i]) {
        //         count++;
        //     }
        // }
        
        return ans;
    }
};
