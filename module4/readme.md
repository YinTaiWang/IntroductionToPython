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
