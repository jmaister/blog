title: Python bitarray and Sieve of Eratosthenes 
date: 2014-01-27 21:00
author: Jordi Burgos
category: Programming
tags: python, math
slug: python-bitarray-sieve-Eratosthenes

Some time ago, I was thinking about prime numbers and I found that it is possible to find prime numbers just with sums instead of divisions or remainders. As it was very simple approach, I thought that for sure, someone else found this solution already. And I was right, this algorithm is called [Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

This method exchanges the CPU intense calculations by storage. Instead of calculating if a number is prime with divisions, it stores which numbers are not primes until a maximum, then the prime numbers are the ones that are not on the list. Very simple.

Here is the first version of my solution made in Python.

The [bitarray](https://github.com/jmaister/bitarray) started as a solution for a programming contest where the problem was to find the n-th number missing on a 8 GB file full of integers.

BitArray
========

The easy option to keep all the numbers that are not primes is to use a list. It is a valid solution but not the best, as each number would use 64 bits (Assumption for big numbers, as Python takes the best type for each number representation). The first 1.000.000 numbers would be stored on 7.62 MB of memory.

The minimum size of memory is the bit, so we can mark each number with just a bit. With this approach, a 1.000.000 would use 122 Kb of memory. Here is the implementation of a [BitArray](https://github.com/jmaister/bitarray) in Python.

The program uses an array of 64 bit numbers (or 32 bits, depending on your processor) and each bit says if the number is marked or not. For example, the number 1, goes on the element 0 of the array and the bit 1. The number 63, goes on the element 1 of the array, position bit 32.

<table class="table border">
	<tr>
	   <td>Array</td>
	   <td>32 bits</td>
	</tr>
	<tr>
	   <td>element 0</td>
	   <td>00000000000000000000000000000010</td> 
	</tr>
    <tr>
       <td>element 1</td>
       <td>10000000000000000000000000000000</td> 
    </tr>
</table>

The position of each number on the array and the position of the bit set or reset inside is calculated with bit arithmetic. Here is the code for the address calculations:

    :::python

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

For calculating all the primes until a certain number, we need to mark all those numbers in any way into memory. The bitarray just uses one bit per number. The architecture, you know 32 or 64 bits, does not affect to the amount of memory as the numbers use just 1 bit.

With 1 GB of memory, it is possible to hold the numbers from 0 to 8,589,934,592, this is **1 * 1024 * 1024 * 1024 * 8**. 

<table class="table bordered">
<tr><td>GB Memory</td><td>Numbers</td><td>Power of 2</td></tr>
<tr><td>1</td><td>8,589,934,592</td><td>2^33</td></tr>
<tr><td>2</td><td>17,179,869,184</td><td>2^34</td></tr>
<tr><td>4</td><td>34,359,738,368</td><td>2^35</td></tr>
<tr><td>8</td><td>68,719,476,736</td><td>2^36</td></tr>
<tr><td>16</td><td>137,438,953,472</td><td>2^37</td></tr>
<tr><td>32</td><td>274,877,906,944</td><td>2^38</td></tr>
<tr><td>64</td><td>549,755,813,888</td><td>2^39</td></tr>
<tr><td>128</td><td>1,099,511,627,776</td><td>2^40</td></tr>
<tr><td>1024</td><td>8,796,093,022,208</td><td>2^43</td></tr>
</table>

This calculations are aproximations, the execution of the program would take a little more memory.


How many memory would need the maximum prime number found ?
===========================================================

The [http://en.wikipedia.org/wiki/Largest_known_prime_number] (http://en.wikipedia.org/wiki/Largest_known_prime_number) is 2^57,885,161 - 1, a number with 17,425,170 digits.

Using the previous table with the comparison between numbers and memory used, calculate the memory needed for the maximum prime number found is easy.
1 Gigabyte holds from 0 to 2^33, 1 Terabyte holds from 0 to 2^43. So 2^57,885,161 - 1 can fit on (57,885,161 - 33) = 57,885,129 Gibabytes = 56,528.45 Terabytes = 55.20 Petabytes.

This sizes are unmanageable usin RAM memory, but it could be possible usin hard drives to store all the information.
What would cost to store all that information on hard drives? A 4 TB SATA hard disk costs about 150 EUR (~205 USD). That would be 14,133 drives. **About 2,119,800 EUR (2,898,025 USD)**.

Just for the hard drives. **Anyone interested on funding the project ?**

<div class="center" markdown="1">
![Not bad]({filename}/images/meme/shut_up_take_money.jpg)
</div>

Optimization
============

The storage admits some optimizations. The very easy is to skip all even numbers and change the kind of addressing of bits. All the even numbers are not primes.
That would take the cost of the project to the half. Those 2,119,800 EUR (2,898,025 USD), would turn on **1,059,900 EUR (1,449,201 USD)**.

Conclusions
===========

This method to calculate primes is more CPU efficient than the usual with divisions if all the information fits on RAM memory. Its drawback is that trades CPU by storage.

The cost for using this algorithm in the real would be huge, but we just need to let the time pass and wait for the terabyte or petabyte RAM memory or hard drives.
