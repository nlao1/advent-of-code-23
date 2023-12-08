# advent-of-code-23

## Day 1:

I was quite annoyed seeing part 2, and even more annoyed that the problem statement
was unclear, and did not specify what `twone` was meant to be parsed as. So I happened
to choose wrong, and wrote a trie from scratch only to realize that it was all for naught.

## Day 6:

Day 6 part 2 was interesting. My solution from part 1 worked, but after further
reflection I realized that it's a quadratic equation. The function is representable
by distance = x(time-x), and then you just need to find the roots of the function
and multiply everything between them together. Luckily, the input is small enough that you
can just brute force it.

# Day 7

I can describe my code for today in 1 word: bad. What would have been better
would be to make a hand class and to test a bunch of cases classifying hands.
I did not give myself enough room to debug originally which led to a lot of time lost.

# Day 8

Not a fan of this one. Requires a decent amount of math knowledge and I don't like the fact that
the input is rigged so that its solvable by LCM.
