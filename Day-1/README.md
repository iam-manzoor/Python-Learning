# Python Zero to Hero Programming.

## Day-1 Introduction to python

1. **What is Programming?**
  - Programming is the way we communicate with computer, and ask them to perform tasks.
  - We have multiple programming languages to communicate with computer.
    1. **Java**
    2. **Python**
    3. **C**
    4. **C++**
    5. **React** and many more
  - We write the code in python language and the system uses translator (**Compiler/Interpreter**) to convert them into machine readable form(**0's and 1's**).

2. **What is Python?**
   - **Python is simple & easy:** One of the easiest language to start programming 
   - **Free & Open Source:** Free to use 
   - **HLL:** Python is high-level language because its syntax is clear and close to english.
   - **Developed by Guido van Rossum:** The person who developed Python.
   - **Portable:** The code written on windows can be run on any other OS platform provided with necessary libraries.
  
3. **Writing the First line of code in python:** `print("Hello World!!!")`
   - **print:** It's an in-built python function. Its function is to print the statement given inside the parenthesis to the stdout.
     - We can also perform operation using **print** function `print(41+31) O/P = 72`, `print(2*3) O/P = 6`. We can perform other operation as well.

4. **Python Character Set**
   - Letters - `A-Z, a - z`
   - Digits - `0 - 9`
   - Special Symbols - `+ - * / etc..`
   - Whitespaces - Blank Space, tab, carriage return, newline, formfeed.
   - Other characters - ASCII and Unicode characters.
  
5. **Variables**
   - A variable is a name given to a memory location in a program.
   - Variables means a value that can be changed/overwritten.
   - Below are a few example of Variables
     - `name = "Arhan"` Left-hand side is variable name and the Right-hand side is variable value
     - `age = 09`         Left-hand side is variable name and the Right-hand side is variable value
   - variable name it picks up a random location in memory and store the value in the memory. Variable name is an address to the memory location to access the value.
   - Access the variable `print(name)` `print(age)`
   - Value of one variable can be assigned to the other variables with the help of Assignment operator `=`. Whatever the value of **a** will become value of **b**.
     ```
     a = 25
     b = a
     print(a, b)
     ```
6. **Rules for Identifiers**
   - Identifiers/Variables (Will discuss the naming convention).
   - Variable name can be combination of uppercase and lowercase letters, digits or an underscore(_). `myName, phone_1, list_of_phones` all are valid python identifiers.
   - Variable can not start with digit `phone1` is valid, but `1phone` is not valid.
   - special symbols like `!,@,#,$,%` etc.. can not be used in variables.
   - Identifiers can be of any length.
