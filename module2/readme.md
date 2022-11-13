# Week 2: If, Loops

## 1 - Electronics
The electrics company ‘The Battered Battery’ is nearly bankrupt. To avoid total disaster, the marketing branch has come up with a special sale to attract more customers. Whenever a customer buys three products, he or she receives a 15% discount on the most expensive product. Write a program that takes the prices of three products as input and prints the discount and final price as output.

Remember that the goal of making the assignments in this chapter is to practice the use of if-statements. Therefore, do not use the built-in function max or a sorting function in this assignment.

Example:
``Enter the price of the first article: 200
Enter the price of the second article: 50
Enter the price of the third article: 25
Discount: 30.00
Total: 245.00``

## 2 - Othello 2
During a game of Othello, the time a player spends thinking about his moves is recorded. Write a program that reads the times that the two players have thought, in milliseconds. One of the players is human, the other is a computer. The program determines which of the two players is human and prints the thinking time of the human in the following format: hh:mm:ss. It may be assumed that a computer always has less thinking time than a human.

Example:
``Enter the time the black player thought: 21363
Enter the time the white player thought: 36
The time the human player has spent thinking is: 00:00:21.``

## 3 - TA detector
Make a program that asks the user's name and then prints if the user is a TA. The TAs are Elisa, Rico, Stef, Khagan and Vlad.

Example:
``What is your name? 
Vlad
Hi Vlad, you seem to be a TA!
-----
What is your name? 
Johnny
Hi Johnny, you do not seem to be a TA!``

## 4 - Manny
Mobster Manny thinks he has found the perfect way to part money from their rightful owners, using a computer program. Mobster Manny secretly installs the program on someone’s computer and remains hidden in a corner, waiting for the program to finish. The program will ask the user how much he or she wants to donate to charity, Thirsty Toads in the Sahara (Manny’s Wallet). If the unsuspecting victim wants to donate less than €50, the program will ask again. The program will continue to ask for an amount until the user has agreed to donate €50 or more, after which Mobster Manny will show up to collect the money.

Example:
``Enter the amount you want to donate:
0
Enter the amount you want to donate:
10
Enter the amount you want to donate:
52
Thank you very much for your contribution of 52.00 euro.``

## 5 - Multiplication table
Write a program that reads in a number and then prints its multiplication table.

Example:
``Please enter a number 
5
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50``

## 6 - Alphabet
Write a program that prints the alphabet on a single line. Do not write the alphabet as a literal string, instead use the ord() and chr() functions. Type help(ord) or help(chr) in IPython (called python console in PyCharm, button at the bottom of the screen by default) to get info on what these functions do. 
You should get the following output:

Should get the following output:
``abcdefghijklmnopqrstuvwxyz``

## 7 - Collatz
One of the most renowned unsolved problems in mathematics is the Collatz conjecture. The problem is stated as follows:

Start out with some number n.

Apply the following rule repeatedly to the number:

if n is even, the next number is n/2
if n is odd, the next number is 3n + 1

This will give us a list of numbers. For example, when starting with 11 the list will be:
``11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 4 2 1 4 2 1 ...``

Once the sequence has reached 1, it will repeat 4, 2, 1 indefinitely. The conjecture is that no matter which starting number you pick, the sequence will reach 1 eventually.

This conjecture is probably correct. Using computers all numbers up to 2^68 have been found to reach 1. Note that 2^68 is quite a large number: it is about 40 times the number of grains of sands on earth, or 4 times the number of stars in the universe. If you can check 1 number per nanosecond, trying all 2^68 numbers takes you about 10,000 (10 thousand) years. 

This problem is very simple to state, but no one has proved the conjecture since Collatz stated it in 1937. There have even been mathematicians that have spent years of continued study on the conjecture, without success. Fortunately, writing a program that generates the Collatz sequence is a lot less challenging.

Write a program that takes any positive integer and prints the corresponding Collatz sequence up to and including the first one.

Example:
``Please enter a number: 11
34 17 52 26 13 40 20 10 5 16 8 4 2 1``

## 8 - Pyramid 
Make a program that asks for a width, and then prints a pyramid of that width. The pyramid must be of odd width, and if the user enters an even number the program should print "Please enter an odd number" and ask again. (It is ok if the program gives an error if the user enters a non-number). 

Example:
```Please enter the pyramid width 
10
Please enter an odd number
Please enter the pyramid width 
14
Please enter an odd number
Please enter the pyramid width 
13
      *
     ***
    *****
   *******
  *********
 ***********
*************
```

The first line should have 1 asterisk, the second 3, then 5, 7, 9 etc. The number of spaces before starting the asterisks is (n-i)/2

Where n is the width of the pyramid and i is the number of asterixes in the current line. Note that this is always a whole number, as n and i are odd and hence (n-i) is even.

## 9 - Table of contents
Make a program that prints the table of contents of a book where each chapter has the same number of sections, and each section has the same number of subsections.

Example:
``Please enter the number of chapters 
3
Please enter the number of sections 
3
Please enter the number of subsections 
3
Chapter 1
-Section 1.1
--Subsection 1.1.1
--Subsection 1.1.2
--Subsection 1.1.3
-Section 1.2
--Subsection 1.2.1
--Subsection 1.2.2
--Subsection 1.2.3
-Section 1.3
--Subsection 1.3.1
--Subsection 1.3.2
--Subsection 1.3.3
Chapter 2
-Section 2.1
--Subsection 2.1.1
--Subsection 2.1.2
--Subsection 2.1.3
-Section 2.2
--Subsection 2.2.1
--Subsection 2.2.2
--Subsection 2.2.3
-Section 2.3
--Subsection 2.3.1
--Subsection 2.3.2
--Subsection 2.3.3
Chapter 3
-Section 3.1
--Subsection 3.1.1
--Subsection 3.1.2
--Subsection 3.1.3
-Section 3.2
--Subsection 3.2.1
--Subsection 3.2.2
--Subsection 3.2.3
-Section 3.3
--Subsection 3.3.1
--Subsection 3.3.2
--Subsection 3.3.3
``

## 10 - Second Smallest
Take an unknown number, larger than two, of positive integers as input. Assume that the first
number is always smaller than the second, all numbers are unique and the
input consists of at least three integers. Print the second smallest integer.

Example:
``Please enter some numbers: 10 12 2 5 15
The second smallest number is: 5``

## 11 - Bubblesort
Bubble sort is a sorting algorithm: when given a list, for example [4,2,6,8], it will sort the list to become sorted, [2,4,6,8]. Bubble sort works by walking through the list, comparing adjacent elements, and swapping them if they are in the wrong order. The process of walking through the list is repeated until we have traversed the entire list and no elements were swapped (this means that all adjacent elements are in the right order, and hence the list is sorted).

Example:
First pass

( 5 1 4 2 8 ) → ( 1 5 4 2 8 ) Here, the algorithm compares the first two elements, and swaps since 5 > 1.

( 1 5 4 2 8 ) → ( 1 4 5 2 8 ) Swap since 5 > 4

( 1 4 5 2 8 ) → ( 1 4 2 5 8 ) Swap since 5 > 2

( 1 4 2 5 8 ) → ( 1 4 2 5 8 ) Now, since these elements are already in order (8 > 5), the algorithm does not swap them.

Second pass

( 1 4 2 5 8 ) → ( 1 4 2 5 8 )

( 1 4 2 5 8 ) → ( 1 2 4 5 8 ), Swap since 4 > 2

( 1 2 4 5 8 ) → ( 1 2 4 5 8 )

( 1 2 4 5 8 ) → ( 1 2 4 5 8 )

Third pass

Now, the array is already sorted, but the algorithm does not know if it is completed. The algorithm needs one additional whole pass without any swap to know it is sorted.

Bubble sort is actually quite an inefficient way of sorting: it takes a lot of steps compared to other algorithms such as mergesort.



