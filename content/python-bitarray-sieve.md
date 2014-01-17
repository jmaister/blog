Some time ago, I was thinking about prime numbers and I found that it is possible to find prime numbers just with sums instead of divisions or remainders. As it was very simple approach, I thought that for sure, someone else found this solution already. And I was right, this algorith is called [Sieve of Eratostenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

This method exchanges the CPU intense calculations by storage. Instead of calculating if a number is prime with divisions, it stores which numbers are not primes until a maximum, then the prime numbers are the ones that are not on the list. Very simple.

Here is the first version of my solution made in Python.

BitArray
========

The easy option to keep all the numbers that are not primes is to use a list. It is a valid solution but not the best, as each number would use 64 bits (Assumption for big numbers, as Python takes the best type for each number representation). The first 1.000.000 numbers would be stored on 7.62 Mb of memory.

The minimum size of memory is the bit, so we can mark each number with just a bit. With this approach, a 1.000.000 would use 122 Kb of memory. Here is the implementation of a [BitArray](https://github.com/jmaister/bitarray) in Python.

It uses an array of 64 bit numbers (or 32 bits, depending on your processor) and each bit says if the number is marked or not. With bit operations it is calculated the position on the array and the bit position to set or reset. Here are the address calculations:

    ...python

        [...]
        # Depends on architecture
        if bitsstr == '64bit':
            self.bits = 64
            self.bit_mask = 0x0000003F
            self.bit_offset = 6
        [...]

    def __get_address(self, n):
        # position on the array
        bucket = n >> self.bit_offset
        # bit position on the element
        bit = n & self.bit_mask
        return bucket, bit

