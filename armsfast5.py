#!/usr/bin/python3
#
# armsfast.py - Fast Armstrong Number Finder
#
# This originally came from here:
#
# https://codegolf.stackexchange.com/questions/83272/all-armstrong-numbers
#
# The challenge presented was to minimize the size of the code an
# the answer in Python2 by Felipe Nardi Batista (with some help tweaking
# it by Jonathan Frech) was:
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
# I have moved it to Python3 (fairly trivial) and am trying to make it
# a bit easier to follow, but the key thing that makes it blaze compared
# to other examples I've found is the use of the itertools library. This
# handles a lot of the work creating combinations that I knew needed to
# be done far more efficiently than anything I could have coded myself.
# 
from itertools import combinations_with_replacement
import time

# What time do we start?
start_time = time.time()

# Start with a list with only zero...
#
# This value has to be 'brute forced' onto the list as the 'cost' of
# checking for and ignoring tuples that have a leading zero.
A = [0]

# If you enable the checking of number with only zeros and ones, you
# will also need to force a 1 into the list to start with.
# A = [0, 1]


# Initialize one of the timer variaable...
t3 = 0

# Build a table of digits to the possible exponents so that we
# only have to do that fairly intensive calculation once and
# can stick to lookups and addition from now on.
#
# When I ran this up to 19 digits, it took 168.4 seconds using
# the original approach. Adding the table for the powers and
# using it instead cut execution time to 93.8 seconds.

pwrs_table = [[dig ** pwr for dig in range(10)] for pwr in range(61)]


# Define how many digits we want to go up to (plus 1)...
#
# The original coded started at zero and that didn't make any difference
# with things, but it did generate an empty tuple which broke the logic
# where I check the first element of the tuple to see if it is zero.
#
# The goal of the original code was to be compact--the goal of my changes
# is to see if I can realisticly do an exhaustive search to find all of
# the Armstrong Numbers in a reasonable amount of time (days, not weeks).
for i in range(1,20):

# Print progress message
    t1 = int((time.time()-start_time)*10)
    t2 = t1 - t3
    print('Checking digit count of ', i, '-', t2/10, '/', t1/10, 'seconds')
    t3 = t1
    
    row = pwrs_table[i]

    l=0
    if i > 13:
        l = 7
    if i > 24:
        l = 8
        
# Create a tuple containing the combinations of the 
#    
    for c in filter(lambda x: x[-1]>l, combinations_with_replacement(range(10),i)):
        t=sum(row[d] for d in c)
        if sorted(map(int,str(t))) == c:
            A.extend([t])
            
# Print the results...
#
# The sorted is necessary because we do not necessarily generate the
# combinations in numeric order.
print(*sorted(A), sep='\n')

print('Run time was {:f} seconds.'.format(time.time() - start_time))

