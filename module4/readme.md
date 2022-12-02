# Week 4: More functions, Wordle

## 1 - Anagram 
Make a method is_anagram_of(a,b) that tests if a is an anagram of b. A string a is an anagram of a string b, if it uses exactly the same letters, but the order can be different. Spaces are ignored, as well as capitalization.

Examples of anagrams:

- "eleven plus two" - "twelve plus one"
- "William Shakespeare" - "I am a weakish speller"
- "Tom Marvolo Riddle" - "I am Lord Voldemort"
- "Anagrams" - "Ars manga" 
- "television ads" - "enslave idiots"

Counter examples:

- "bla" - "aalb"
- "cat" - "tact"

Hint: Make a dictionary that holds how often a letter occurs in a word. 


## 2 - Merge sorted arrays 
 Program a method merge_sorted(a,b) that when given two sorted arrays a and b, returns a new sorted array c that has the elements from array a and array b. For example when given
a = [1,3,5,6,10]
b = [1,4,6,8]

the resulting array should be:

c = [1,1,3,4,5,6,6,8,10]

This method should not call a sorting method. Instead, the resulting array should be produced by "zipping" the two input arrays together: we repeatedly select the least element that we did not consider before from a and b and include this in c.

For example:
```
     a = [1,3,5,6,10]
              ^
     b = [1,4,6,8]
            ^
     c = [1,1,3,...]
      
```
the arrows (^) point to the lowest element we did not consider before. Of these, element 4 from b is less than element 5 from a. For this reason, we select 4 as the next element and advance the arrow ^ for b to point to 6.


## 3 - Sieve of Eratosthenes 
The sieve of Eratosthenes is a way of computing all the prime numbers below a certain number. (A prime number is a number that is only divisible by itself and 1). This algorithm is explained excellently in video, or you can read about this ancient algorithm on Wikipedia.

https://www.youtube.com/watch?v=klcIklsWzrY

Implement this algorithm:

Implement a function cross_out_multiples that takes as arguments a list of boolean values (true/false) called is_prime and a number n. The function sets the boolean values at all multiples of n (2*n, 3*n, 4*n ...) that are in the list to false.
Implement a function sieve(n)  which gives back a list of all primes below n. 


## 4 - Wordle
In this exercise, you'll be recreating the game Wordle. For Dutch students: this is the same game as seen in the Dutch TV-program Lingo (5 letter variant).  You can play the official version of it here: https://www.nytimes.com/games/wordle/index.html. In Wordle the user has to guess a secret five-letter word. On each guess, each letter in the word you guessed will be marked as one of the following:

- correct: the letter occurs in the secret word and is in the right position; green color
- wrong position: the letter occurs in the secret word, but at a different position; yellow color
- fully incorrect: the letter does not appear in the secret word; gray color
As an example, suppose the secret word is "peace". If the user guesses "angle", the coloring will be: angle

In the official version, the words you are allowed to guess must be actually existing words. In our version, we do not have this requirement, allowing you to guess any sequence of five characters. (We also do not implement hard mode, only normal mode.)


> Coloring
You will have to specify the colors of each of the characters in a guess. You might expect to compare the letters in the guess one by one with the secret word and then color them accordingly. The actual coloring is slightly more sophisticated. Imagine the secret word is "razor" and you guessed "honor". The coloring then should be honor. Since the second 'o' is a full match, it gets priority and will be colored first. The first 'o' will be gray, because, even though there is an 'o' in the secret word, it has already been matched with the second 'o', and so there are no remaining 'o's left.

This priority system is the key to correctly implementing this algorithm. First, we color the full matches green, then the remaining characters that still appear are matched yellow and the remaining characters will be matched gray. See the following steps:

1. Assume all characters are gray (incorrect) first.
2. Check for any correct characters and mark them as green.
3. Get rid of these characters so you don't accidentally match them again (e.g., assign them some arbitrary value - make sure the arbitrary value is different between the secret word and the guessed word, otherwise you might still accidentally match them in step 4.)
4. Check for any characters in the wrong position and mark them as yellow. Make sure you replace the matched characters in the (copy) of the secret to ensure that you do not match them again (for example, suppose the secret is "earth", and the guess is "tense", then only the first e should be marked as yellow)
5. Now you're done, this is the correct coloring.

Note that the secret and the guesses are stored in the example program as strings, but for this algorithm, you need a copy of the secret in which you are able to edit to remove characters. Since strings are immutable (they cannot be changed), you will need a list of the characters in the secret. You can convert a string to a list of characters by using the string_to_list_of_chars function that is already provided.

(Alternatively, you can also use a dictionary to hold the number of occurrences of each letter in the secret, remove occurrences from the dictionary when checking for correct positions, and then use the dictionary to do the yellow coloring.) 
