#!/usr/bin/python3
#
# armslimit.py - Evaluate Upper Limit for Armstrong Numbers
#
# By Jim McClanahan, W4JBM (November 2020)
#
# An Armstrong Number has the property of equaling
# the sum of its individual digits raised to the
# power of the number of digits.
#
# Some examples include:
# 7 = 7^1
# 371 = 3^3 + 7^3 + 1^3
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
#
# It turns out that an Armstrong Number cannot have more than
# 60 digits because the largest number the equation could yield
# with sixty-one 9s only has sixy digits. The following does a
# quick verification of this printing out the order of the
# evaluation, the maximum number of digits an "all 9s" number
# of that length length would yield, and the actual value for
# that number. You can see the initial cross over from all numbers
# needing to be evaluated to a subset as you move from the 33rd to
# the 34th order and the impossibility of any results as we move
# from the 60th to the 61st order.

l = 1

for x in range(1,75):
    l = l * 9
    print (x, len(str(l*x)), l*x)


