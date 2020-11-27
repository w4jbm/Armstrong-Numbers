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
# R=range
# S=sorted

# What time do we start?
start_time = time.time()

# Start with an empty list...
A = []

# Initialize one of the timer variaable...
t3 = 0

# Define how many digits we want to go up to (plus 1)...
for i in range(40):

# Print progress message
    t1 = int((time.time()-start_time)*10)
    t2 = t1 - t3
    print('Checking digit count of ', i, '-', t2/10, '/', t1/10, 'seconds')
    t3 = t1
    
# The original challenge allowed 'hard coding' to create the list. The
# B flag here was used because all Armstrong Numbers with 32 or more
# digits actually contain at least one of each digit (at least one 0,
# at least one 1, at least one 2, ...) which significantly reduces the
# number of combinations that neet to be checked.
#
# So far as I can determine, this is only known through observation and
# can't be proven in advance.
    B = (i>31)*10
#   B = 0
    
    for c in combinations_with_replacement(range(10),i-B):
        t=sum(d**i for d in c)
        A.extend([t]*(sorted(map(int,str(t)))==sorted(sorted(c)+list(range(B)))))
#       print(sorted(A)[1:])

# Print the results...
#
# The sorted is necessary because we do not necessarily generate the
# combinations in numeric order.
print(*sorted(A), sep='\n')

print('Run time was {:f} seconds.'.format(time.time() - start_time))
