# Schroders

A B C D E

F G H I J

K L M N O

1 2 3

Given the above keypad find all 10 key sequences that can be keyed in given the following
constraints:
1. The initial keypress can be any key.
2. Each subsequent keypress must be a knight move from the previous key.
3. There can be at most 2 vowels in the sequence.
(Note: Given these constraints, a key can be pressed multiple times in the same sequence)
A knight move is defined as either of the following:
1. Move two keys vertically and one horizontally.
2. Move two keys horizontally and one vertically.
(Note: There is no wrapping allowed on a knight move)
Starting from “A” here is an example of a sequence of 3 valid knight moves:

“A” -> “L
“L” -> “3”
“3” -> “J”

Output: Total number of valid 10 key sequences are: 1013398
