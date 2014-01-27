Some time ago, I was thinking about prime numbers and I found that it is possible to find prime numbers just with sums instead of divisions or remainders. As it was very simple approach, I thought that for sure, someone else found this solution already. And I was right, this algorith is called [Sieve of Eratostenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

This method exchanges the CPU intense calculations by storage. Instead of calculating if a number is prime with divisions, it stores which numbers are not primes until a maximum, then the prime numbers are the ones that are not on the list. Very simple.

Here is the first version of my solution made in Python.

BitArray
========

The easy option to keep all the numbers that are not primes is to use a list. It is a valid solution but not the best, as each number would use 64 bits (Assumption for big numbers, as Python takes the best type for each number representation). The first 1.000.000 numbers would be stored on 7.62 Mb of memory.

The minimum size of memory is the bit, so we can mark each number with just a bit. With this approach, a 1.000.000 would use 122 Kb of memory. Here is the implementation of a [BitArray](https://github.com/jmaister/bitarray) in Python.

The program uses an array of 64 bit numbers (or 32 bits, depending on your processor) and each bit says if the number is marked or not. For example, the number 1, goes on the element 0 of the array and the bit 1. The number 63, goes on the element 1 of the array, position bit 32.

| array | 32 bits |
| element 0 | 0 (number 31) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 (number 1)| 0 (number 0)|
| element 1 | 1 (number 63) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 (number 32) |

The position of each number on the array and the position of the bit set or reset inside is calculated with bit arithmetic. Here is the code for the address calculations:

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


How many numbers can hold ?
===========================

For calculating all the primes until a certain number, we need to mark all those numbers in any way into memory. The bitarray just uses one bit per number. The architecture, you know 32 o 64 bits, does not affect to the ammount of memory as the numbers use just 1 bit.

With 1 GB of memory, it is possible to hold the numbers from 0 to 8,589,934,592, this is *1 * 1024 * 1024 * 1024 * 8*. 

|	GB Memory	|	Numbers	|	Power of 2	|
|	1	|	8,589,934,592	|	2^33	|
|	2	|	17,179,869,184	|	2^34	|
|	4	|	34,359,738,368	|	2^35	|
|	8	|	68,719,476,736	|	2^36	|
|	16	|	137,438,953,472	|	2^37	|
|	32	|	274,877,906,944	|	2^38	|
|	64	|	549,755,813,888	|	2^39	|
|	128	|	1,099,511,627,776	|	2^40	|
|	1024	|	8,796,093,022,208	|	2^43	|


This calculations are aproximations, the execution of the program would take a little more memory.


How many memory would need the maximum prime number found ?
===========================================================

The [http://en.wikipedia.org/wiki/Largest_known_prime_number] (http://en.wikipedia.org/wiki/Largest_known_prime_number) is 2^57,885,161 - 1, a number with 17,425,170 digits.

Using the previous table with the comparation between numbers and memory used, calculate the memory needed for the maximum prime number found is easy.
1 Gigabyte holds from 0 to 2^33, 1 Terabyte holds from 0 to 2^43. So 2^57,885,161 - 1 can fit on (57,885,161 - 33) = 57,885,129 Gibabaytes = 56,528.45 Terabytes = 55.20 Petabytes.



Conclusions
===========

