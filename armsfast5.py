#!/usr/bin/python3
#
# armsfast.py - Fast Armstrong Number Finder
#
# By Jim McClanahan, W4JBM (Dec 2020)
#
# I suggest running using:
#     pypy3 armsfast.py
#
# A much faster approach to finding Armstrong Numbers. I had considered
# using a similar approach but had no idea that libraries existed to
# generate the combinations of digits and filter out ones that did not
# need to be evaluated. These libraries are much, much faster than the
# coding I was doing.
#
# A significant amount of the implementation of this concept originally
# came from here:
#
# https://codegolf.stackexchange.com/questions/83272/all-armstrong-numbers
#
# The challenge presented was to minimize the size of the code to generate
# the list of Armstrong Numbers and the answer in Python2 by Felipe Nardi
# Batista (with some help tweaking it by Jonathan Frech) was:
#
# from itertools import*
# R=range
# S=sorted
# A=[]
# for i in R(40):
#  B=(i>31)*10
#  for c in combinations_with_replacement(R(10),i-B):t=sum(d**i for d in c);A+=[t]*(S(map(int,str(t)))==S(S(c)+R(B)))
# print S(A)[1:]
#
# I have made some changes, but the approach is very similar. It uses
# the itertools library to generate the combination of all digits that
# could make up a number of a certain length. These are in an ordered
# tuple.
#
# So it generate something like (1, 3, 5), calculated 1**3 + 3**3 +
# 5**3 to get 153, then it sorts the digits in the resulting sum (so
# 153 is sorted to 135) and compares that to the numbers it used to
# calculated the sum (1, 3, 5). If they match, the calculated number
# is added to the results which are stored in A[].
#
# One trick used to speed things up is based on the observed results.
# (The program just had to make the list of number, it didn't need to
# be rigerous in its approach, it just needed to give you correct
# results.)
#
# For Armstrong Numbers with more than 31 digits, they contain at
# least one of all the digits from 0 to 9. The code above reduces
# the number of combinations by a factor of ten using this fact.
# Then, in the comparison, the digits 0 through 9 are added back
# to what the sum is compared to. This saves a significant amount
# of computing effort, but I have pulled the logic out of my code
# since it can't be demonstrated in advance.
#
# Load the libraries and functions we'll need...
from itertools import combinations_with_replacement
import time

# What time do we start?
start_time = time.time()

# Start with a list with zero and one...
#
# These values must be 'brute forced' onto the list as the 'cost'
# of checking for and ignoring tuples that are not at larger than
# "all ones". (That is, numbers below 11, 111, 1111, etc are not
# checked because they can be shown to never sum to a value that
# would make them an Armstrong Number.
#
# To do that, I check the last digit x[-1] to be greater than 1.
# I also found (and it can be demonstrated) that for all Armstrong
# numbers with 14 or more digits, there must be at least one 8 (so
# we can check x[-1]>7 and for all Armstrong numbers with 25 or
# more digits, there must be at least one 9 (so we can check
# x[-1]>8. Eventually we find that for numbers with more than 60
# digits, even if all the digits were 9, the sum still would not
# be high enough to ever be an Armstrong Number.
A = [0, 1]

# Initialize one of the timer variaable...
t3 = 0

# Build a table of digits to the possible exponents so that we
# only have to do that fairly intensive calculation once and
# can stick to lookups and addition from now on.
#
# When I ran this up to 19 digits, it took 168.4 seconds using
# the original approach (calculations done as needed and on the
# fly). Adding the table for the powers and using it instead
# cut execution time to 93.8 seconds. (That was several versions
# ago.)
pwrs_table = [[dig ** pwr for dig in range(10)] for pwr in range(61)]


# Define how many digits we want to go up to (plus 1)...
#
# The original coded started at zero and that didn't make any difference
# with things, but it did generate an empty tuple which broke the logic
# where I check the last element of the tuple during filtering of
# combinations that can never sum to a high enough value.
#
# The goal of the original code was to be compact--the goal of my changes
# is to see if I can realisticly do an exhaustive search to find all of
# the Armstrong Numbers in a reasonable amount of time (days, not weeks).
for i in range(1,40):

# Print progress message
    t1 = int((time.time()-start_time)*10)
    t2 = t1 - t3
    print('Checking digit count of ', i, '-', t2/10, '/', t1/10, 'seconds')
    t3 = t1

# Pull the appropriate row of powers of the digits 0 through 9...
    row = pwrs_table[i]

# Not pretty, but basically we can check the last digit of the combination
# to be greater than these value as a condition to filter out combinations
# that can never work. For example 111 only sums to 3 (and anything made
# up of zeros and ones will never be an Armstrong Number with two or more
# digits). For this check, we make sure there is at lease one number >=2
# in the tuple. At 14 digits, we actually must have at least one 8 and at
# 25 digits we must have at least one 9.
#
# (There are more variation possible between 1 and 14 digits, but the
# program calculated all the Armstrong Numbers up to 19 digits in under
# a minute, so more optimization isn't worth the effort.)
    l=1
    if i > 13:
        l = 7
    if i > 24:
        l = 8
        
# Create a tuple containing the combinations of the digits 0 thru 9. Also
# filter out any values that can't sum to a high enough value (that is,
# they won't have enough digits).
    for c in filter(lambda x: x[-1]>l, combinations_with_replacement(range(10),i)):

# Now sum the powers of the digits.
        t=sum(row[d] for d in c)

# Pulling the conversion to the string ouf of the later check and doing a
# quick check of only the length shave run time for up to 19 digits from
# 32.6 seconds down to 26.8 seconds.
        st = str(t)
        if len(st) != i:
            continue

# And this is the meat of the program. If the digits in the sum match the
# digits in the combination we are testing, then we have an Armstrong
# Number and need to add it to the list.            
        if tuple(sorted(map(int,st))) == c:
            A.extend([t])
            
# Print the results...
#
# The sorted is necessary because we do not necessarily generate the
# combinations in numeric order.

print(*sorted(A), sep='\n')
#print sorted(A[1:])

print('Run time was {:f} seconds.'.format(time.time() - start_time))

