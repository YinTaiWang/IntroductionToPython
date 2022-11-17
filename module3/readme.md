# Week 3: Functions

## 1 - Nuclear Power Plant 
The nuclear powerplant at Threeyedfish will automatically run a program to print a warning message when the reactor core becomes unstable. The warning message reads:
```
NUCLEAR CORE UNSTABLE!!! 
Quarantine is in effect. 
Surrounding hamlets will be evacuated. 
Anti-radiationsuits and iodine pills are mandatory.
```

Since the message contains crucial information, it should be printed three times. To do this, write a function that prints this message. This function has to be used three times.

## 2 - Palindrome 1
Write a program that will print the following string:
```
abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba
```

It is not allowed to do this hardcoded.

Hint: This line consists of three parts:

- a to y
- z
- y to a

Use ord() and chr() to loop over the alfabet.

## 3 - Palindrome 2
This assignment continues where Palindrome 1 has finished. Make a program that:

reads a letter from standard input
print the string from Palindrome 1 up to this letter
For example, if the letter was c, the output would be:
```
abcba
```

## 4 - Pyramid
Write a program that prints a pyramid made of letters in the middle of the screen. Use functions with parameters for this assignment. The base width of the pyramid is determined by a character the user enters. If the user enters the letter o, the following pyramid will be printed. It can be assumed that the screen width is 80 characters.
```
                                       a                                        
                                      aba                                       
                                     abcba                                      
                                    abcdcba                                     
                                   abcdedcba                                    
                                  abcdefedcba                                   
                                 abcdefgfedcba                                  
                                abcdefghgfedcba                                 
                               abcdefghihgfedcba                                
                              abcdefghijihgfedcba                               
                             abcdefghijkjihgfedcba                              
                            abcdefghijklkjihgfedcba                             
                           abcdefghijklmlkjihgfedcba                            
                          abcdefghijklmnmlkjihgfedcba                           
                         abcdefghijklmnonmlkjihgfedcba
```

The following assignments make use of functions with return values ("fruitful functions"). The automated (unit) tests check the input/output behavior of functions via tests.py (you can run the tests from pycharm yourself, go tests.py and press the play button next to class Tests(unittest.TestCase)). Sometimes we also test the input/output behavior of the whole program as we did before, this is indicated per assignment.

## 5 - Sum numbers
Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to and including n. So sum_to(10) would be 1+2+3...+10 which would return the value 55.

## 6 - Time to seconds 
Write a function to_seconds that takes three parameters: hours, minutes and seconds, and converts them to a total number of seconds.

## 7 - Palindrome 3
Make a function is_palindrome that takes a string as an argument that returns True if the given string is a palindrome, and False otherwise. A string is a palindrome if it is the same if you reverse it.

For example:
```
"racecar"
"kayak"
"otto"
"redivider"
"wontloversrevoltnow"
```

## 8 - Pizza

Mario owns a pizzeria. Mario makes all of his pizzas from 10 different ingredients, using 3 ingredients on each pizza. Mario’s cousin Luigi owns a pizzeria as well. Luigi makes all his pizzas from 9 ingredients, using 4 ingredients on each pizza. Mario and Luigi have made a bet: Mario believes that customers can order a larger selection of pizzas in his pizzeria than they can order in Luigi’s pizzeria. Use functions for this assignment.

- Implement a factorial() function yourself (do not use the one from the math module)
- When choosing k items from n possible items, the number of possibilities can be obtained using the following formula: n!/k!(n-k)!

Make a function called choose with two parameters n and k, that implements the above formula.

- Write a program that calculates the number of pizzas Mario and Luigi can make. The outcome should look like this:
```
Mario can make 120 pizzas.
Luigi can make 126 pizzas. 
Luigi has won the bet.
```

## 9 - Selection sort

NOTE: You must implement the algorithm described here, not some other algorithm or use a call to sort!

Selection sort is a sorting algorithm, like Bubble sort which you saw in the previous module. Selection sort works as follows:

Selection sort divides the input list into two parts: a sublist of sorted items (left part) and a sublist of still unsorted items (right part). Initially, the sorted sublist is empty and the whole input consists of the unsorted sublist. To fill the sorted sublist, the algorithm computes the (index of) the minimum of the unsorted sublist and swaps the first unsorted element and the minimum element (if the minimum is already the first element, nothing happens). Afterward, the sorted sublist is one bigger. This continues until the unsorted sublist is empty and the entire input is sorted.

Example:

| Sorted sublist       | Unsorted sublist    | Least element in unsorted list |
| -------------------- | ------------------- | ------------------------------ |
| ()                   | (11, 25, 12, 22, 64)| 11                             |
| (11)                 | (25, 12, 22, 64)    | 12                             |
| (11, 12)             | (25, 22, 64)        | 22                             |
| (11, 12, 22)         | (25, 64)            | 25                             |
| (11, 12, 22, 25)     | (64)                | 64                             |
| (11, 12, 22, 25, 64) | ()                  |                                |


Implement this algorithm. 

- Implement a function called index_of_min with two parameters, l and start_index, which computes the index of the minimum of the sublist starting at index start_index. Do not use methods from the library such as min(), sort() etc. 
- Implement a function called selection_sort which sorts the input list (in place). This function must use index_of_min and must not use methods from the library such as min(), sort() etc. 





