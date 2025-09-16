## Day-2 Srings and Conditional Statements

1. **Strings**
   - String is data type that stores a sequence of characters.
   - We can define strings in different ways, its because to have quotes within string. Refer string4.
   - Supports escape sequence such as `\n` `\t` etc..
   ```
   string1 = "I am Arhan"
   string2 = 'I am studying in 4th std'
   string3 = """I stay in Banglore"""
   string4 = "It's a plesaure meeting you"
   string5 = "This is string.\nWe started learning Python"
   print(string5)
   ```
   - **Basic Operations**
     - concatenation
     - Length of string
     - Indexing in string. The string characters in Python is indexed.
       - string object doesnt allow item assignment. Example `myCollege[4]="@"`
       - Index helps us to access the characters but we cant modify the index value.
     - Slicing
       - Accessing parts of a string. Example `myCollege[starting_idx:ending_idx]` ending_idx will not be printed.
       - Negative index supported by python. Only works with slicing.
      
   - **String FUnctions**
     - String supports multiple functions. Below are the few examples.
       - `str.endswith("er")` **er** is a substring, and function returns boolean.
       - `str.capitalize()` Capitalize the first character.
       - `str.replace(old, new)` Replace the word old with new. All the occurances.
       - `str.find(word)` Return the index of that word. First occurance
       - `str.count("am")` Count the occurance of the substring.
      

2. **Conditional Statements**
   - Checks for the statement and then statement gets executed.
   - if-elif-else
   - We have nesting conditional statement as well.
