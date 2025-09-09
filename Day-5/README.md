## Day 5 Pthon Loops

1. **while Loop in Python**
   - Loops are used to repeat instructions.
   - `while` loop executes till the condition is `True`
   - `while` Loops
     - ```
       while condition:
         statements
       ```
   - **Break & Continue** With-in while loop
     - `break` used to terminate the loop when encountered.
     - `continue` terminates execution in the current iteration & continues exection of the loop with next iteration.

2. **for Loop in Python**
   - Used for sequential traversal. For traversing list, string, tuples etc.
   - Example
     ```
     lst = [1,2,3]

     for el in lst:
        print(el)
     ```
3. **range function**
   - FUnction returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
   - `range` syntax 
   ```
   range(start?, stop, step?)

   for el in range(5):
     print(el)

   for el in range(1,5):
     print(el)

   for el in range(1,5,2):
      print(el)
   ```
