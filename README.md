# Armstrong-Numbers
Various notes and work related to Armstrong Numbers.

**Warning: I make a lot of 'simplifications' in places. For example, when I'm talking about "powers" of even or odd numbers, I am actually talking about integer, non-negative powers (and numbers) because that is what is relevant here. If you want more rigor (say in the case of using this to help with your homework), you should probably think about adding more qualifying statements to some of the assertations I make.**

An Armstrong Number (also referred to as Narcissistic Numbers) has the property of equaling the sum of its individual digits raised to the power of the number of digits. Some examples include:

* 7 = 7^1
* 371 = 3^3 + 7^3 + 1^3
* 1634 = 1^4 + 6^4 + 3^4 + 4^4

There are only 89 Armstrong Numbers in Base 10. The smallest is 0 (although some people seem to argue this isn't truely one even though the calculation hold for it). The largest is 115,132,219,018,763,992,565,095,597,973,971,522,401 which has 39 digits.


## The armstrong.py Program

The first approach I use is mostly "Brute Force" and would likely bog down once you get to number too high in order. But it is reasonably quick at finding results up to 7 digits (which covers the first 25 of them).


## What is the largest Armstrong Number?

Okay, I answered that before, but is there a way to put an upper boundy on our efforts?

Yes!

Think about 3 digit Armstrong Numbers. The aboslute largest one that could exist with three digits is 999 and to check whether it truly is one we would need to calculate:

x = 9^3 + 9^3 + 9^3 = 3 * (9^3)+ 9^3 = 2187

Similarly, for 6 digits we would look at:

x = 9^6 + 9^6 + 9^6 + 9^6 + 9^6 + 9^6 = 6 * (9^6) = 3188646

In these cases, evaluation of the "maximum" number  yields a number with more digits than we can have. From that, we can assume it is at least possible that Armstrong numbers exist. If we continue to look at higher and higher orders of numbers with this approach, we find something interesting.

* 32nd Order, x=109,877,882,249,360,399,509,051,170,856,992 (33 digits)
* 33rd Order, x=1,019,804,094,626,876,207,943,381,179,516,457 (34 digits)
* 34th Order, x=9,456,365,241,085,579,382,747,716,391,879,874 (34 digits)
* 35th Order, x=87,610,442,674,763,456,046,045,019,513,004,715 (35 digits)

The number of digits with lower orders is sufficient for any number in that range to be considered, but when we get to the 34th order, only about 95% of the numbers are possible to derive from the equation we need to evaluate. Moving to the 35th order, only about 88% of the numbers possible have any chance of being Armstrong Numbers. In fact, we find this continues to decline. (The largest Armstrong Number has 39 digits and only about 64% of the numbers with 39 digits could possibly fit the equation.)

Note for future consideration: I don't think the percentages are accurate because they don't take into account the lowest number in the range isn't zero. So for the 34th order, the percentage would actaully be something more like (95-10)/(100-10) or 94%.

At the 61st order, things fall apart. If you want to calculate 61 * (9^61), you will find it only has 60 digits! That means there is no number with 61 digits that can ever possibly be an Armstrong Number!

So we can stop looking once we have evaluated potential 60 digit candiates. This puts the upper boundary on how high our search needs to go.

The program armslimit.py demonstrates this.


## What else can simplify the search?

Take a look at the three and four digit Armstrong Numbers: 153, 370, 371, 407, 1,634, 8,208, and 9,474.

It probably won't jump out at anyone who isn't a math wizard or isn't looking at it, but there is a rule in play here:

* Excluding the last digit, the sum of the other digits must be **even**.

The reason behind this is a concept called parity. An odd number to any integer power will always yield an odd result and an even number to any even power will always yield an even result.

Also, a number that ends in an odd number is odd and one that ends in an even number is even.

So when we sum the power of the digits, if we exclude the last digit the other **must** be even. In other words, we need to only look at cases where:

Even first digits + Even last digit = Even result\
Even first digits + Odd last digit = Odd result

The fact that we are raising the first digits to some power is irrelevant because the result will still be odd or even just like the number before we raised it to the power. The cases we can ignore are where the results cannot possibly match the outcome of the calculations:

Odd first digits + Even last digit = Odd Result\
Odd first digits + Odd last digit = Even Result

So with 153, 1+5 is 6 which is even. We add the final number (3) and the result of the sum of the numbers is odd.

With 1,634, 1+6+3 is 10 which is even. We add the final number (4) and the result of the sum of the numbers is even.

You can do some verification on your own, but the sum of the digits excluding the last one will always be even for any Armstrong Number.


## What can speed up the calculations?

One thing that jumped out at me is that multiplication takes a lot of time and in the brute force method we do a lot of it.

For example, with the six digit Armstrong numbers, we run through 6 multiplications (taking each number to the sixth power) before we add the six numbers together. (Some programming languages use a different approach for calculating things that is faster than raw multiplication but also tends to be less accurate. From what I can tell, this is not an issue with Python and for other languages where it would be an issue the "arbitraty length" intergers we are dealing with would need to be handled differently.)

To simplify this, we can calculate the powers of the digits 0 through 9 for the number of digits we are wanting to evaluate once at the beginning of things. This will keep the other math we use down to simple additions.


## Any other ideas on speeding things up?

One other efficiency that comes to mind is that we don't have to calculate for a specific number but can, instead, calculate for a combination of digits. For example, if we check whether a 1, a 3, and a 5 could create an Armstrong Number, we get the result 153 from the addition. We now have an Armstrong number (because the result is 3 digits and made up from the three digits we used for the test), but we also know (because of the cummutative property of addition) that 135, 315, 351, 513, and 531 are all NOT Armstrong Numbers (because the cube of their digits will summ to 153). This means that testing 3 single digits gave us a result that held true for 3! (3 * 2 * 1, or 6) numbers.

I'm not sure the overhead of handling this would be worth the improvement it would yield, but it is something to consider.

Note: It isn't relevant to this, but the number 153 has some other interesting properties. It is a triangular triangular number; 1 + 2 + 3 + 4+ 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 = 153 and also 1! + 2! + 3! + 4! + 5! = 153. It even makes an appearance in the Bible: "So Simon Peter went aboard and hauled the net ashore, full of large fish, a hundred fifty-three of them; and though there were so many, the net was not torn." (John 21:11, NRSV).

Another thing that struck me as I considered this is that if we want to search for (picking a number) five digit Armstrong numbers, we can start at 11111 instead of 10000. In fact, for any length, we could start with "all ones". 10000 is going to evaluate to 1^5 or 1 which obviously will never have the same number of digits as the number being evaluated except in the case of single digit numbers. 11111 is going to evaluate to 5 * 1^5 or 5 which also will never have the same number of digits for any number consisting of all ones that has at least two digits.

At first, the algoritm I'm thinking about didn't seem to be able to make use of this because I still need to evaluate numbers with zeros so if I had a simple rule that said the digits needed to be in ascending order, starting at 11111 would ignore anything that might have any zeros in it.

But then it became clear that if I "started at the top" and had the rule instead be that the digits were in decending order, things seem to work.

So in the case above, we could start our search for unique combinations of digits with something like:

```
99999
99998
99997
...
99991
99990
99988
99987
99986
...
99981
99980
99977
99976
99975
...
...
...
22111
22110
21111
21110
11111
```

If we sort the digits of all five digit numbers greater than 11111 in decending order, that sequence should capture all possible results.

I'm still not sure how many digits we can reasonably search even with this. My gut feel is that the ability to exclude blocks of numbers because the upper digits don't sum to an even number actually saves us more evaluations.

But that might change if we built some intelligence into the algorith to narrow down to the range of numbers that give us the right number of digits in the result. In this sequence, the calculation should always yeild smaller and smaller results (which would not be the case if you just simply counted down--for example 99997, 99979, 99799, 97999, and 79999 would all give the same result but by limiting our evaluations to the squence above we'd just look at 99997 and determine if the result was a five digit number that had 4 nines and 1 seven in it).

## The resulting code...

...can be found in armsfinal.py. You can set the number of digits you want to go out to. Right now it is set to 60 but that would take a few years to run on most machines. Realistically you can get to about ten digits if you let it run overnight. It can crank through six digits in about a second on the machine I'm using right now.

If anyone ever has the horsepower to let it find all the Armstrong Numbers, I'd be interested in hearing about it.


## But wait! There's more!

I came across a snippet of code that makes use of itertools and blazes compared to the brute force approach in my original code. I've added two the use of a lookup table for the powers (as discussed earlier) and also ignore cases where the leading digit is zero. While I could get six digits in about a second before, I can now get 20 digits in about a minute (and 24 digits in about 2.5 minutes).

These are in the files armsfast#.py where the # is a version number for now. Once I settle on some final code, I'll update things more.


## Is zero an Armstrong Number

I see arguments about this, but zero clearly meets the fundamental definition: 0^1 = 0.

Some of the arguments say it isn't because there are no two digit Armstrong Numbers and zero can be expressed as 00. But 2 can be written as 02 and it is an Armstrong Number. And even if you write it as 00, the calculation still would hold: 0^2 + 0^2 = 0 or 00.

It does seem like what I would call "proper mathmaticians" sometimes talkes about "Armstrong Numbers in the range of 1 to something..." If you want to exclude zero, that seems like the proper way to do it.

Having said that, the Online Encyclopedia of Interger Sequences (OEIS) does not include zero and has added the adjective "positive" to the definition. Since Zero is neither positive nor negative (as I understand their use), their definition of the sequence would exclude zero.

Having said all of that, -1 also meets the basic definition: -1^1 = -1...

As a matter of fact, -9 through 0 and on through +9 all meet the definition.

I tend to refer to the searchs as looking for "non-trivial (more than one digit) Armstrong Numbers". That keeps you from debating about negative number or zero.


## And the fine print...

To the extent applicable, all code and other material in this repository is:

Copyright 2020 by James McClanahan and made available under the terms of The MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
