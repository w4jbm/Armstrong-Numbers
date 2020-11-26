#!/usr/bin/python3
#
# armsfinal.py - Armstrong Numbers
#
# By Jim McClanahan, W4JBM (November 2020)
#
# This is an improved set of algorithms designed to
# calculate all Armstrong Numbers in a reasonable
# amount of time. Using armslimit.py, it can be
# shown that no Armstrong Number has more than 60
# digits.
#
# An Armstrong Number has the property of equaling
# the sum of its individual digits raised to the
# power of the number of digits.
#
# Some examples include:
# 7 = 7^1
# 371 = 3^3 + 7^3 + 1^3
# 1634 = 1^4 + 6^4 + 3^4 + 4^4

# Let's see how long this takes...
import time

start_time = time.time()

# n = the number we are evaluating, we add one as we
#     enter each itteration
n = -1

# Build a table of digits to the possible exponents
# so that we only have to do that fairly intensive
# calculation once and can stick to lookups and
# addition from now on.

pwrs_table = [[dig ** pwr for dig in range(10)] for pwr in range(61)]

while True:
    n = n + 1
    s = str(n)
    l = len(s)
    
# Let's see if we're over 60 digits and, if so, let's
# quit. Note that the highest result will have 39 digits
# and that no number with more than 60 digits can be an
# Armstrong Number.
    if l>60:
        break

# Numbers from 0 to 9 are all Armstrong Numbers and
# it is easier just to print them than to have to
# build logic to handle single digit numbers.
    if n<10:
        print(n)
        continue

# The digits of the number, excluding the final digit,
# must sum to an EVEN number in all Armstrong Numbers.
# (See the readmen.md for details.) If we are starting
# a new set of leading digits, let's check if we should
# just skip over this and the next nine numbers.
#
# Note: We do this when the last number is zero, so we
#       can actually check that the sum of all digits
#       is even.
    if n % 10 == 0:
        if sum(a in "13579" for a in s) % 2 == 1:
            n = n + 9
            continue

# At this point, we need to check a viable candidate
# that we can check...

# Get the row we will be using from the table of powers
# we calculated earlier...
    row = pwrs_table[l]

# Initialize some variable for working and result...
    temp = n
    rslt = 0

    while temp>0:
        digit = temp % 10
        rslt += row[digit]
        temp //= 10

# And check it...
    if n == rslt:
        print(n)

print('Run time was {:f} seconds.'.format(time.time() - start_time))

